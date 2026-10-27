import os
import re
import datetime
import shutil
import json
from pathlib import Path
from typing import Optional, List
from fastapi import APIRouter, UploadFile, File, Form, HTTPException, Query
from fastapi.responses import FileResponse, JSONResponse

from backend.config import UPLOADS_DIR, REPORTS_DIR, SAMPLES_DIR, DEFAULT_CASE
from backend.models import (
    Case, EvidenceItem, TimelineEvent, ChatMessage,
    ImageAnalysisResponse, AudioAnalysisResponse, VideoAnalysisResponse,
    FusionAnalysisResponse, ChatQueryRequest, ChatQueryResponse,
    init_db, get_or_create_case
)
from backend.services.claude_service import ForensicAIAnalyzer, compute_file_sha256
from backend.services.fusion_service import MultimodalFusionEngine
from backend.services.pdf_service import ForensicPDFBuilder
api_router = APIRouter(prefix="/api", tags=["Forensic Microservices"])


@api_router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "CrimeVision AI Forensic Engine",
        "version": "2.4.0-Enterprise",
        "multimodal_modalities": ["image", "audio", "video", "fusion"]
    }


@api_router.get("/cases/{case_id}")
async def get_case_dossier(case_id: str):
    init_db()
    case = get_or_create_case(case_id)
    evidence = list(EvidenceItem.select().where(EvidenceItem.case == case))
    timeline = list(TimelineEvent.select().where(TimelineEvent.case == case).order_by(TimelineEvent.timestamp_str.asc()))
    return {
        "case_id": case.case_id,
        "title": case.title,
        "incident_date": case.incident_date,
        "location": case.location,
        "lead_investigator": case.lead_investigator,
        "badge_number": case.badge_number,
        "jurisdiction": case.jurisdiction,
        "classification": case.classification,
        "classification_confidence": case.classification_confidence,
        "penal_code": case.penal_code,
        "threat_level": case.threat_level,
        "overall_threat_score": case.overall_threat_score,
        "summary": case.summary,
        "probable_cause": case.probable_cause,
        "evidence_items": [
            {
                "id": ev.id,
                "type": ev.evidence_type,
                "filename": ev.filename,
                "sha256": ev.sha256_hash,
                "threat_score": ev.threat_score,
                "timestamp": ev.timestamp_logged.strftime("%Y-%m-%d %H:%M:%S"),
                "analysis": ev.get_analysis_data()
            }
            for ev in evidence
        ],
        "timeline_events": [
            {
                "id": t.id,
                "timestamp": t.timestamp_str,
                "modality": t.modality,
                "title": t.title,
                "description": t.description,
                "actor": t.actor,
                "threat_rating": t.threat_rating,
                "correlation": t.cross_modal_correlation
            }
            for t in timeline
        ]
    }


@api_router.post("/image", response_model=ImageAnalysisResponse)
async def analyze_image_endpoint(
    file: Optional[UploadFile] = File(None),
    case_id: str = Form("CRV-2026-8841"),
    sample_name: Optional[str] = Form(None)
):
    init_db()
    case = get_or_create_case(case_id)
    UPLOADS_DIR.mkdir(parents=True, exist_ok=True)

    clean_filename = "evidence_image.jpg"
    target_path = UPLOADS_DIR / clean_filename

    if file and file.filename:
        safe_name = re.sub(r'[^a-zA-Z0-9_.-]', '_', Path(file.filename).name) or "evidence_image.jpg"
        timestamp = int(datetime.datetime.now().timestamp())
        clean_filename = f"{timestamp}_{safe_name}"
        target_path = UPLOADS_DIR / clean_filename
        target_path.parent.mkdir(parents=True, exist_ok=True)
        file_bytes = await file.read()
        with open(target_path, "wb") as buffer:
            buffer.write(file_bytes)
    elif sample_name:
        clean_filename = sample_name
        target_path = UPLOADS_DIR / clean_filename
        target_path.parent.mkdir(parents=True, exist_ok=True)
        sample_source = SAMPLES_DIR / clean_filename
        if sample_source.exists():
            try:
                shutil.copyfile(sample_source, target_path)
            except Exception:
                target_path = sample_source
        elif not target_path.exists():
            with open(target_path, "wb") as f:
                f.write(b"\xFF\xD8\xFF\xE0\x00\x10JFIF\x00\x01\x01\x01\x00H\x00H\x00\x00\xFF\xDB\x00C\x00")
    else:
        target_path.parent.mkdir(parents=True, exist_ok=True)
        if not target_path.exists():
            with open(target_path, "wb") as f:
                f.write(b"\xFF\xD8\xFF\xE0\x00\x10JFIF\x00\x01\x01\x01\x00H\x00H\x00\x00\xFF\xDB\x00C\x00")

    result = ForensicAIAnalyzer.analyze_image(str(target_path), clean_filename)
    file_size = target_path.stat().st_size if target_path.exists() else 1024

    try:
        EvidenceItem.create(
            case=case,
            evidence_type="image",
            filename=clean_filename,
            file_path=str(target_path),
            file_size=file_size,
            sha256_hash=result.sha256_hash,
            threat_score=result.threat_score,
            analysis_status="analyzed",
            raw_analysis_json=result.model_dump_json(),
            summary=result.scene_description
        )
    except Exception as e:
        print(f"[EvidenceItem DB Insert Error]: {e}")

    return result


@api_router.post("/audio", response_model=AudioAnalysisResponse)
async def analyze_audio_endpoint(
    file: Optional[UploadFile] = File(None),
    case_id: str = Form("CRV-2026-8841"),
    sample_name: Optional[str] = Form(None)
):
    init_db()
    case = get_or_create_case(case_id)
    UPLOADS_DIR.mkdir(parents=True, exist_ok=True)

    clean_filename = "evidence_audio.wav"
    target_path = UPLOADS_DIR / clean_filename

    if file and file.filename:
        safe_name = re.sub(r'[^a-zA-Z0-9_.-]', '_', Path(file.filename).name) or "evidence_audio.wav"
        timestamp = int(datetime.datetime.now().timestamp())
        clean_filename = f"{timestamp}_{safe_name}"
        target_path = UPLOADS_DIR / clean_filename
        target_path.parent.mkdir(parents=True, exist_ok=True)
        file_bytes = await file.read()
        with open(target_path, "wb") as buffer:
            buffer.write(file_bytes)
    elif sample_name:
        clean_filename = sample_name
        target_path = UPLOADS_DIR / clean_filename
        target_path.parent.mkdir(parents=True, exist_ok=True)
        sample_source = SAMPLES_DIR / clean_filename
        if sample_source.exists():
            try:
                shutil.copyfile(sample_source, target_path)
            except Exception:
                target_path = sample_source
        elif not target_path.exists():
            with open(target_path, "wb") as f:
                f.write(b"RIFF\x24\x00\x00\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00\x44\xac\x00\x00")

    result = ForensicAIAnalyzer.analyze_audio(str(target_path), clean_filename)
    file_size = target_path.stat().st_size if target_path.exists() else 2048

    try:
        EvidenceItem.create(
            case=case,
            evidence_type="audio",
            filename=clean_filename,
            file_path=str(target_path),
            file_size=file_size,
            sha256_hash=result.sha256_hash,
            threat_score=result.audio_threat_score,
            analysis_status="analyzed",
            raw_analysis_json=result.model_dump_json(),
            summary=f"Audio diarization of {result.speakers_identified} speakers; {len(result.key_statements)} key statements extracted."
        )
    except Exception as e:
        print(f"[EvidenceItem Audio Insert Error]: {e}")

    return result


@api_router.post("/video", response_model=VideoAnalysisResponse)
async def analyze_video_endpoint(
    file: Optional[UploadFile] = File(None),
    case_id: str = Form("CRV-2026-8841"),
    sample_name: Optional[str] = Form(None)
):
    init_db()
    case = get_or_create_case(case_id)
    UPLOADS_DIR.mkdir(parents=True, exist_ok=True)

    clean_filename = "surveillance_cctv.mp4"
    target_path = UPLOADS_DIR / clean_filename

    if file and file.filename:
        safe_name = re.sub(r'[^a-zA-Z0-9_.-]', '_', Path(file.filename).name) or "surveillance_cctv.mp4"
        timestamp = int(datetime.datetime.now().timestamp())
        clean_filename = f"{timestamp}_{safe_name}"
        target_path = UPLOADS_DIR / clean_filename
        target_path.parent.mkdir(parents=True, exist_ok=True)
        file_bytes = await file.read()
        with open(target_path, "wb") as buffer:
            buffer.write(file_bytes)
    elif sample_name:
        clean_filename = sample_name
        target_path = UPLOADS_DIR / clean_filename
        target_path.parent.mkdir(parents=True, exist_ok=True)
        sample_source = SAMPLES_DIR / clean_filename
        if sample_source.exists():
            try:
                shutil.copyfile(sample_source, target_path)
            except Exception:
                target_path = sample_source
        elif not target_path.exists():
            with open(target_path, "wb") as f:
                f.write(b"\x00\x00\x00 ftypisom\x00\x00\x02\x00isomiso2avc1mp41")

    result = ForensicAIAnalyzer.analyze_video(str(target_path), clean_filename)
    file_size = target_path.stat().st_size if target_path.exists() else 8192

    try:
        EvidenceItem.create(
            case=case,
            evidence_type="video",
            filename=clean_filename,
            file_path=str(target_path),
            file_size=file_size,
            sha256_hash=result.sha256_hash,
            threat_score=result.video_threat_score,
            analysis_status="analyzed",
            raw_analysis_json=result.model_dump_json(),
            summary=result.summary
        )
    except Exception as e:
        print(f"[EvidenceItem Video Insert Error]: {e}")

    return result


@api_router.post("/fuse", response_model=FusionAnalysisResponse)
async def fuse_multimodal_timeline(case_id: str = Form("CRV-2026-8841")):
    return MultimodalFusionEngine.fuse_case_evidence(case_id)


@api_router.post("/chat", response_model=ChatQueryResponse)
async def forensic_chat_copilot(req: ChatQueryRequest):
    case = Case.get_or_none(Case.case_id == req.case_id)
    evidence_count = EvidenceItem.select().where(EvidenceItem.case == case).count() if case else 3
    classification = case.classification if case else "Armed Robbery"

    context = {
        "case_id": req.case_id,
        "title": case.title if case else DEFAULT_CASE["title"],
        "classification": classification,
        "threat_score": case.overall_threat_score if case else 92,
        "threat_level": case.threat_level if case else "CRITICAL",
        "evidence_count": evidence_count,
        "location": case.location if case else DEFAULT_CASE["location"]
    }

    # Record message in DB
    ChatMessage.create(case_id=req.case_id, role="user", content=req.query)
    response = ForensicAIAnalyzer.chat_copilot(req.query, context)
    ChatMessage.create(case_id=req.case_id, role="assistant", content=response.response)

    return response


@api_router.get("/pdf/{case_id}")
async def download_forensic_pdf(case_id: str):
    pdf_path = ForensicPDFBuilder.generate_case_pdf(case_id)
    if not os.path.exists(pdf_path):
        raise HTTPException(status_code=500, detail="PDF generation failed")

    return FileResponse(
        pdf_path,
        media_type="application/pdf",
        filename=os.path.basename(pdf_path)
    )



@api_router.post("/reports/generate")
async def generate_forensic_pdf_endpoint(case_id: str = Form("CRV-2026-8841")):
    pdf_path = ForensicPDFBuilder.generate_case_pdf(case_id)
    filename = os.path.basename(pdf_path)
    return {
        "status": "success",
        "case_id": case_id,
        "filename": filename,
        "download_url": f"/api/pdf/{case_id}"
    }
@api_router.post("/demo/seed")
async def seed_demo_case(case_id: str = "CRV-2026-8841"):
    """Pre-populates a complete multimodal investigation with Image, Audio, Video, and Fused Timeline."""
    case = get_or_create_case(case_id)

    # 1. Seed Image Evidence
    img_res = ForensicAIAnalyzer.analyze_image("sample_surveillance_cam02.jpg", "sample_surveillance_cam02.jpg")
    EvidenceItem.create(
        case=case,
        evidence_type="image",
        filename="sample_surveillance_cam02.jpg",
        file_path="samples/sample_surveillance_cam02.jpg",
        file_size=245890,
        sha256_hash=img_res.sha256_hash,
        threat_score=img_res.threat_score,
        analysis_status="analyzed",
        raw_analysis_json=img_res.model_dump_json(),
        summary=img_res.scene_description
    )

    # 2. Seed Audio Evidence
    aud_res = ForensicAIAnalyzer.analyze_audio("dispatch_counter_mic01.wav", "dispatch_counter_mic01.wav")
    EvidenceItem.create(
        case=case,
        evidence_type="audio",
        filename="dispatch_counter_mic01.wav",
        file_path="samples/dispatch_counter_mic01.wav",
        file_size=1048576,
        sha256_hash=aud_res.sha256_hash,
        threat_score=aud_res.audio_threat_score,
        analysis_status="analyzed",
        raw_analysis_json=aud_res.model_dump_json(),
        summary=f"3 speakers diarized; vocal stress detected in clerk and armed suspect."
    )

    # 3. Seed Video Evidence
    vid_res = ForensicAIAnalyzer.analyze_video("cctv_exterior_getaway.mp4", "cctv_exterior_getaway.mp4")
    EvidenceItem.create(
        case=case,
        evidence_type="video",
        filename="cctv_exterior_getaway.mp4",
        file_path="samples/cctv_exterior_getaway.mp4",
        file_size=5242880,
        sha256_hash=vid_res.sha256_hash,
        threat_score=vid_res.video_threat_score,
        analysis_status="analyzed",
        raw_analysis_json=vid_res.model_dump_json(),
        summary=vid_res.summary
    )

    # 4. Run Timeline Fusion
    fusion_res = MultimodalFusionEngine.fuse_case_evidence(case_id)

    return {
        "status": "success",
        "message": f"Case {case_id} seeded with 3 multimodal exhibits and fused timeline.",
        "case_id": case_id,
        "classification": fusion_res.classification.primary_crime,
        "threat_score": fusion_res.composite_threat_score,
        "timeline_events_count": len(fusion_res.fused_timeline)
    }
