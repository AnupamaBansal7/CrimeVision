import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from fastapi.testclient import TestClient
from backend.main import app
from backend.models import init_db, Case, EvidenceItem, TimelineEvent
from backend.services.claude_service import ForensicAIAnalyzer, compute_file_sha256
from backend.services.fusion_service import MultimodalFusionEngine
from backend.services.pdf_service import ForensicPDFBuilder

def run_tests():
    print("=" * 60)
    print("RUNNING CRIMEVISION AI ENTERPRISE VERIFICATION TEST SUITE")
    print("=" * 60)

    # 1. DB Init
    print("[1/7] Testing Database Initialization...")
    init_db()
    case = Case.get_or_none(Case.case_id == "CRV-2026-8841")
    assert case is not None, "Case CRV-2026-8841 should exist"
    print(f" -> DB OK: Found Case '{case.title}'")

    # 2. Image Analysis
    print("[2/7] Testing Image Analysis Service...")
    sample_img = "samples/sample_surveillance_cam02.jpg"
    img_res = ForensicAIAnalyzer.analyze_image(sample_img, "sample_surveillance_cam02.jpg")
    assert img_res.threat_score > 0, "Threat score should be calculated"
    assert len(img_res.sha256_hash) == 64, "SHA-256 hash must be 64 characters"
    print(f" -> Image OK: Threat Score {img_res.threat_score}/100, SHA: {img_res.sha256_hash[:12]}...")

    # 3. Audio Analysis
    print("[3/7] Testing Audio Analysis Service...")
    sample_aud = "samples/dispatch_counter_mic01.wav"
    aud_res = ForensicAIAnalyzer.analyze_audio(sample_aud, "dispatch_counter_mic01.wav")
    assert aud_res.speakers_identified >= 1, "Speakers should be identified"
    assert len(aud_res.speaker_diarization) > 0, "Diarization segments present"
    print(f" -> Audio OK: {aud_res.speakers_identified} speakers diarized, {len(aud_res.key_statements)} key statements")

    # 4. Video Analysis
    print("[4/7] Testing Video Analysis Service...")
    sample_vid = "samples/cctv_exterior_getaway.mp4"
    vid_res = ForensicAIAnalyzer.analyze_video(sample_vid, "cctv_exterior_getaway.mp4")
    assert len(vid_res.timeline_events) > 0, "Video timeline events detected"
    print(f" -> Video OK: {len(vid_res.timeline_events)} temporal events parsed, Threat: {vid_res.threat_level}")

    # 5. Multimodal Fusion Engine
    print("[5/7] Testing Multimodal Fusion & Crime Classifier...")
    fusion_res = MultimodalFusionEngine.fuse_case_evidence("CRV-2026-8841")
    assert fusion_res.classification.primary_crime != "", "Crime must be classified"
    assert len(fusion_res.fused_timeline) >= 4, "Fused timeline must have multiple events"
    print(f" -> Fusion OK: Classified as '{fusion_res.classification.primary_crime}' ({fusion_res.classification.statutory_code})")
    print(f"    Fused Timeline Events: {len(fusion_res.fused_timeline)}, Composite Threat: {fusion_res.composite_threat_score}/100")

    # 6. ReportLab PDF Generation
    print("[6/7] Testing ReportLab PDF Generation...")
    pdf_path = ForensicPDFBuilder.generate_case_pdf("CRV-2026-8841")
    assert os.path.exists(pdf_path), f"PDF file must exist at {pdf_path}"
    pdf_size = os.path.getsize(pdf_path)
    assert pdf_size > 1000, "PDF must not be empty"
    print(f" -> PDF OK: Generated {pdf_path} ({pdf_size:,} bytes)")

    # 7. FastAPI REST Endpoints via TestClient
    print("[7/7] Testing FastAPI REST Endpoints via TestClient...")
    client = TestClient(app)

    # Health
    r = client.get("/api/health")
    assert r.status_code == 200, f"Health check failed: {r.text}"
    assert r.json()["status"] == "healthy"

    # Case dossier
    r = client.get("/api/cases/CRV-2026-8841")
    assert r.status_code == 200, f"Case fetch failed: {r.text}"
    case_data = r.json()
    assert case_data["case_id"] == "CRV-2026-8841"

    # Chat Copilot
    r = client.post("/api/chat", json={"case_id": "CRV-2026-8841", "query": "What weapons were detected?"})
    assert r.status_code == 200, f"Chat failed: {r.text}"
    chat_data = r.json()
    assert "response" in chat_data and len(chat_data["response"]) > 10

    # PDF Download
    r = client.get("/api/pdf/CRV-2026-8841")
    assert r.status_code == 200, f"PDF endpoint failed: {r.text}"
    assert r.headers["content-type"] == "application/pdf"
    print(" -> REST API OK: All endpoints returned 200 OK with valid JSON/PDF payloads!")

    # 8. Vercel Serverless Entrypoint & Web Assets
    print("[8/8] Testing Vercel Serverless Entrypoint & Web Dashboard Assets...")
    import api.index
    vercel_client = TestClient(api.index.app)
    r_html = vercel_client.get("/", headers={"Accept": "text/html"})
    assert r_html.status_code == 200 and "CRIMEVISION AI" in r_html.text
    r_css = vercel_client.get("/styles.css")
    assert r_css.status_code == 200 and "forensic-card" in r_css.text
    r_js = vercel_client.get("/app.js")
    assert r_js.status_code == 200 and "loadCaseDossier" in r_js.text
    r_gen = vercel_client.post("/api/reports/generate", data={"case_id": "CRV-2026-8841"})
    assert r_gen.status_code == 200 and r_gen.json()["status"] == "success"
    print(" -> Vercel OK: Serverless entrypoint and all static web assets verified!")
    print("=" * 60)
    print("ALL 8 CRIMEVISION VERIFICATION TESTS PASSED SUCCESSFULLY!")
    print("=" * 60)

if __name__ == "__main__":
    run_tests()
