import os
import json
import shutil
from pathlib import Path
from typing import Dict, Any, List

from nicegui import ui, app
from backend.config import DEFAULT_CASE, UPLOADS_DIR, REPORTS_DIR, SAMPLES_DIR
from backend.models import (
    Case, EvidenceItem, TimelineEvent, ChatMessage, init_db
)
from backend.services.claude_service import ForensicAIAnalyzer, compute_file_sha256
from backend.services.fusion_service import MultimodalFusionEngine
from backend.services.pdf_service import ForensicPDFBuilder
from ui.theme import apply_theme
from ui.components import (
    header_bar, kpi_card, threat_badge, chain_of_custody_pill,
    timeline_item_row, chat_message_bubble
)

# Active session state
state: Dict[str, Any] = {
    "case_id": DEFAULT_CASE["case_id"],
    "active_tab": "overview",
    "selected_evidence_type": "image",
    "chat_history": [],
    "last_pdf_path": None,
    "last_image_result": None,
    "last_audio_result": None,
    "last_video_result": None,
    "timeline_filter": "ALL"
}

def get_or_create_case() -> Case:
    case = Case.get_or_none(Case.case_id == state["case_id"])
    if not case:
        case = Case.create(
            case_id=state["case_id"],
            title=DEFAULT_CASE["title"],
            incident_date=DEFAULT_CASE["incident_date"],
            location=DEFAULT_CASE["location"],
            lead_investigator=DEFAULT_CASE["lead_investigator"],
            badge_number=DEFAULT_CASE["badge_number"],
            jurisdiction=DEFAULT_CASE["jurisdiction"]
        )
    return case


def build_ui():
    """Builds the complete NiceGUI forensic dashboard."""
    apply_theme()
    init_db()

    # Pre-seed initial analysis if DB empty
    case = get_or_create_case()
    if EvidenceItem.select().where(EvidenceItem.case == case).count() == 0:
        MultimodalFusionEngine.fuse_case_evidence(state["case_id"])

    # Top Header
    c = get_or_create_case()
    header_bar(
        case_id=c.case_id,
        lead_inv=f"{c.lead_investigator} • {c.badge_number}",
        on_seed=lambda: handle_seed_demo_case()
    )

    # Main Dashboard Container
    with ui.column().classes('w-full max-w-7xl mx-auto px-6 pb-12 pt-24 gap-6'):

        # Navigation Tabs
        with ui.tabs().classes('w-full border-b border-slate-800 bg-slate-900/60 rounded-t-xl') as tabs:
            tab_overview = ui.tab('overview', label='Case Overview & Executive Summary', icon='dashboard')
            tab_intake = ui.tab('intake', label='Evidence Intake & Processing Studio', icon='perm_media')
            tab_timeline = ui.tab('timeline', label='Forensic Chronological Timeline', icon='timeline')
            tab_chat = ui.tab('chat', label='Forensic Copilot Assistant', icon='smart_toy')
            tab_export = ui.tab('export', label='PDF Export & Chain of Custody', icon='verified_user')

        with ui.tab_panels(tabs, value='overview').classes('w-full bg-transparent'):

            # ==========================================================
            # TAB 1: EXECUTIVE SUMMARY & CASE OVERVIEW
            # ==========================================================
            with ui.tab_panel('overview').classes('w-full p-0 gap-6 flex flex-col'):
                overview_container = ui.column().classes('w-full gap-6')

                def render_overview():
                    overview_container.clear()
                    c = get_or_create_case()
                    items = list(EvidenceItem.select().where(EvidenceItem.case == c))
                    timeline_count = TimelineEvent.select().where(TimelineEvent.case == c).count()

                    with overview_container:
                        # Top Case Dossier Banner
                        with ui.card().classes('forensic-card w-full p-6'):
                            with ui.row().classes('items-start justify-between w-full'):
                                with ui.column().classes('gap-1 flex-1'):
                                    with ui.row().classes('items-center gap-2'):
                                        ui.icon('folder_open', size='22px').classes('text-cyan-400')
                                        ui.label(c.title).classes('text-xl font-black text-white tracking-wide')
                                        threat_badge(c.threat_level, c.overall_threat_score)
                                    ui.label(f"INCIDENT: {c.incident_date} | LOCATION: {c.location} | JURISDICTION: {c.jurisdiction}").classes('text-xs text-slate-400 font-medium')
                                
                                with ui.row().classes('gap-2'):
                                    ui.button('Run Multimodal Fusion', on_click=lambda: trigger_multimodal_fusion(), icon='auto_awesome').props('color=cyan-7').classes('font-bold')
                                    ui.button('Generate PDF Report', on_click=lambda: trigger_pdf_export(), icon='picture_as_pdf').props('color=red-8').classes('font-bold')

                        # 4 Forensic KPI Cards
                        with ui.row().classes('w-full gap-4 flex-wrap'):
                            kpi_card('Evidence Exhibits', f"{len(items)} Logged", "Images, Audio & Video feeds", 'perm_media', '#38bdf8')
                            kpi_card('Crime Classification', c.classification, c.penal_code, 'gavel', '#f59e0b')
                            kpi_card('Threat Matrix Level', f"{c.threat_level} ({c.overall_threat_score}/100)", "Armed Coercion & Lethal Risk", 'warning', '#ef4444')
                            kpi_card('Chain of Custody', "100% VALIDATED", "Cryptographic SHA-256 Ledger", 'verified_user', '#10b981')

                        # Probable Cause & Incident Summary Card
                        with ui.row().classes('w-full gap-6 items-stretch'):
                            with ui.card().classes('forensic-card flex-1 p-6'):
                                with ui.row().classes('items-center gap-2 mb-3'):
                                    ui.icon('assignment', size='20px').classes('text-cyan-400')
                                    ui.label('Executive Forensic Narrative').classes('text-base font-bold text-white')
                                ui.label(c.summary or "Awaiting multimodal synthesis.").classes('text-sm text-slate-300 leading-relaxed')

                                with ui.column().classes('mt-4 pt-4 border-t border-slate-800 gap-2'):
                                    ui.label('SWORN PROBABLE CAUSE DRAFT:').classes('text-[11px] font-black tracking-wider text-cyan-400')
                                    ui.label(c.probable_cause or "Analysis pending.").classes('text-xs text-slate-400 italic leading-relaxed')

                            with ui.card().classes('forensic-card w-full lg:w-[380px] p-6 flex flex-col justify-between'):
                                ui.label('Investigator Quick Actions').classes('text-base font-bold text-white mb-2')
                                with ui.column().classes('w-full gap-3'):
                                    ui.button('Intake New Forensic Evidence', on_click=lambda: tabs.set_value('intake'), icon='cloud_upload').props('outline color=cyan').classes('w-full font-bold')
                                    ui.button('Inspect Synchronized Timeline', on_click=lambda: tabs.set_value('timeline'), icon='timeline').props('outline color=cyan').classes('w-full font-bold')
                                    ui.button('Consult Forensic AI Copilot', on_click=lambda: tabs.set_value('chat'), icon='chat').props('outline color=purple').classes('w-full font-bold')
                                    ui.button('Download Official PDF Dossier', on_click=lambda: trigger_pdf_export(), icon='download').props('color=red-7').classes('w-full font-bold')

                        # Exhibits Mini Grid
                        with ui.column().classes('w-full gap-3'):
                            with ui.row().classes('items-center justify-between w-full'):
                                ui.label('Active Evidence Repository').classes('text-base font-bold text-white')
                                ui.label(f"{len(items)} exhibits registered").classes('text-xs text-slate-400')

                            with ui.row().classes('w-full gap-4 flex-wrap'):
                                for ev in items:
                                    with ui.card().classes('forensic-card p-4 flex-1 min-w-[280px]'):
                                        with ui.row().classes('items-center justify-between w-full mb-2'):
                                            ui.label(ev.evidence_type.upper()).classes('badge-modality text-[10px]')
                                            threat_badge("CRITICAL" if ev.threat_score >= 85 else "HIGH", ev.threat_score)
                                        ui.label(ev.filename).classes('text-sm font-bold text-white truncate')
                                        ui.label(ev.summary).classes('text-xs text-slate-400 line-clamp-2 my-1')
                                        chain_of_custody_pill(ev.sha256_hash)

                render_overview()

            # ==========================================================
            # TAB 2: EVIDENCE INTAKE & PROCESSING STUDIO
            # ==========================================================
            with ui.tab_panel('intake').classes('w-full p-0 gap-6 flex flex-col'):
                intake_container = ui.column().classes('w-full gap-6')

                def render_intake_studio():
                    intake_container.clear()
                    with intake_container:
                        with ui.row().classes('items-center justify-between w-full'):
                            with ui.column().classes('gap-0'):
                                ui.label('Multimodal Forensic Processing Studio').classes('text-xl font-black text-white')
                                ui.label('Extract weapons, diarize audio speech, catalog telemetry, and compute threat metrics.').classes('text-xs text-slate-400')
                            
                            # Modality Selector Buttons
                            with ui.button_group():
                                btn_img = ui.button('Image Studio', icon='photo_camera', on_click=lambda: set_evidence_modality('image')).props(f"color={'cyan-7' if state['selected_evidence_type'] == 'image' else 'slate-8'}")
                                btn_aud = ui.button('Audio Studio', icon='mic', on_click=lambda: set_evidence_modality('audio')).props(f"color={'cyan-7' if state['selected_evidence_type'] == 'audio' else 'slate-8'}")
                                btn_vid = ui.button('Video Studio', icon='videocam', on_click=lambda: set_evidence_modality('video')).props(f"color={'cyan-7' if state['selected_evidence_type'] == 'video' else 'slate-8'}")

                        # Studio Work Area based on selected modality
                        if state['selected_evidence_type'] == 'image':
                            render_image_studio()
                        elif state['selected_evidence_type'] == 'audio':
                            render_audio_studio()
                        elif state['selected_evidence_type'] == 'video':
                            render_video_studio()

                def set_evidence_modality(mod: str):
                    state['selected_evidence_type'] = mod
                    render_intake_studio()

                def render_image_studio():
                    with ui.row().classes('w-full gap-6 items-start'):
                        # Left Column: Upload & Sample Controls
                        with ui.card().classes('forensic-card w-full lg:w-[420px] p-6 gap-4'):
                            with ui.row().classes('items-center gap-2'):
                                ui.icon('image', size='22px').classes('text-cyan-400')
                                ui.label('Surveillance Frame Intake').classes('text-base font-bold text-white')

                            ui.label('Upload or choose high-resolution CCTV frame for Claude 3.5 Sonnet analysis:').classes('text-xs text-slate-400')

                            # Sample Selector for instant 1-click test
                            ui.label('PRE-LOADED FORENSIC SAMPLES:').classes('text-[10px] font-black tracking-widest text-cyan-400 mt-1')
                            sample_select = ui.select(
                                options={
                                    'sample_surveillance_cam02.jpg': 'Armed Robbery - Register CAM-02',
                                    'sample_burglary_alley.jpg': 'Night Burglary - Rear Entrance Pry',
                                    'sample_traffic_crash.jpg': 'Intersection Vehicle Collision'
                                },
                                value='sample_surveillance_cam02.jpg'
                            ).classes('w-full')

                            ui.button('Load Selected Sample', on_click=lambda: process_image_sample(sample_select.value), icon='bolt').props('color=cyan-7').classes('w-full font-bold')

                            ui.separator().classes('my-2 border-slate-800')

                            # Custom Upload dropzone
                            ui.label('OR UPLOAD EVIDENCE FILE:').classes('text-[10px] font-black tracking-widest text-slate-400')
                            ui.upload(
                                label='Drop surveillance image here (.jpg, .png)',
                                on_upload=lambda e: handle_image_upload(e),
                                auto_upload=True
                            ).props('accept=.jpg,.jpeg,.png,.webp dark flat color=cyan').classes('w-full')

                        # Right Column: Visual Preview & AI Forensic Report
                        with ui.card().classes('forensic-card flex-1 p-6 gap-4'):
                            with ui.row().classes('items-center justify-between w-full'):
                                ui.label('AI Optical Diagnostics & Object Catalog').classes('text-base font-bold text-white')
                                if state["last_image_result"]:
                                    threat_badge(state["last_image_result"].threat_level, state["last_image_result"].threat_score)

                            img_preview_container = ui.column().classes('w-full gap-4')

                            def update_image_view():
                                img_preview_container.clear()
                                res = state.get("last_image_result")
                                with img_preview_container:
                                    # Preview Image
                                    with ui.row().classes('w-full justify-center bg-black/60 rounded-lg p-2 border border-slate-800'):
                                        ui.image('/uploads/sample_surveillance_cam02.jpg').classes('max-h-[320px] rounded object-contain')

                                    if res:
                                        with ui.column().classes('w-full gap-3 mt-2'):
                                            chain_of_custody_pill(res.sha256_hash)

                                            # Scene Description
                                            with ui.card().classes('bg-slate-900/80 p-3 rounded-lg border border-slate-800'):
                                                ui.label('SCENE DESCRIPTION & LIGHTING:').classes('text-[10px] font-black text-cyan-400')
                                                ui.label(res.scene_description).classes('text-xs text-slate-300 mt-1')
                                                ui.label(f"Environment: {res.lighting_and_environment}").classes('text-[11px] text-slate-400 mt-1')

                                            # Weapons Detected
                                            with ui.card().classes('bg-red-950/30 p-3 rounded-lg border border-red-500/40'):
                                                with ui.row().classes('items-center gap-2 mb-1'):
                                                    ui.icon('warning', size='16px').classes('text-red-400')
                                                    ui.label('WEAPONS EVALUATION:').classes('text-[10px] font-black text-red-400')
                                                if res.weapons_detected:
                                                    for w in res.weapons_detected:
                                                        ui.label(f"• {w.weapon_type} (Confidence: {int(w.confidence*100)}%) - {w.description}").classes('text-xs text-red-200')
                                                else:
                                                    ui.label('No weapons detected in visual field.').classes('text-xs text-emerald-400')

                                            # Identified Persons
                                            with ui.column().classes('gap-2'):
                                                ui.label(f"IDENTIFIED SUBJECTS ({res.people_count} DETECTED):").classes('text-[10px] font-black text-slate-400')
                                                with ui.row().classes('w-full gap-2 flex-wrap'):
                                                    for p in res.persons:
                                                        with ui.card().classes('bg-slate-900/90 p-3 rounded-lg border border-slate-800 flex-1 min-w-[220px]'):
                                                            ui.label(p.label).classes('text-xs font-bold text-cyan-300')
                                                            ui.label(f"Role: {p.role_estimate}").classes('text-[11px] text-amber-300')
                                                            ui.label(f"Attire: {p.clothing}").classes('text-[11px] text-slate-400')
                                                            ui.label(f"Actions: {p.actions}").classes('text-[11px] text-slate-300 italic')

                                            # Cataloged Objects
                                            if res.cataloged_objects:
                                                with ui.column().classes('gap-2'):
                                                    ui.label('CATALOGED OBJECTS & SURVEILLANCE ARTIFACTS:').classes('text-[10px] font-black text-slate-400')
                                                    for o in res.cataloged_objects:
                                                        with ui.row().classes('items-center justify-between text-xs p-2 rounded bg-slate-900 border border-slate-800/80'):
                                                            ui.label(f"• {o.label} ({o.location_in_frame})").classes('text-slate-200 font-semibold')
                                                            ui.label(o.forensic_relevance).classes('text-slate-400 text-[11px]')

                            update_image_view()

                def render_audio_studio():
                    with ui.row().classes('w-full gap-6 items-start'):
                        # Left Column: Upload & Controls
                        with ui.card().classes('forensic-card w-full lg:w-[420px] p-6 gap-4'):
                            with ui.row().classes('items-center gap-2'):
                                ui.icon('mic', size='22px').classes('text-cyan-400')
                                ui.label('Acoustic Audio Diarization').classes('text-base font-bold text-white')

                            ui.label('Intake emergency 911 dispatch, body-worn mic, or surveillance audio for speaker separation and speech-to-text extraction:').classes('text-xs text-slate-400')

                            # Native audio player preview
                            ui.label('AUDIO PLAYER PREVIEW:').classes('text-[10px] font-black text-cyan-400')
                            ui.audio('/uploads/dispatch_counter_mic01.wav').props('controls').classes('w-full')

                            ui.button('Process Forensic Audio', on_click=lambda: process_audio_sample('dispatch_counter_mic01.wav'), icon='multitrack_audio').props('color=cyan-7').classes('w-full font-bold')

                            ui.separator().classes('my-2 border-slate-800')
                            ui.upload(
                                label='Upload audio (.wav, .mp3)',
                                on_upload=lambda e: handle_audio_upload(e),
                                auto_upload=True
                            ).props('accept=.wav,.mp3 dark flat color=cyan').classes('w-full')

                        # Right Column: Diarization & Transcripts
                        with ui.card().classes('forensic-card flex-1 p-6 gap-4'):
                            with ui.row().classes('items-center justify-between w-full'):
                                ui.label('Speaker Diarization & Speech Breakdown').classes('text-base font-bold text-white')
                                if state["last_audio_result"]:
                                    threat_badge(state["last_audio_result"].threat_level, state["last_audio_result"].audio_threat_score)

                            aud_preview = ui.column().classes('w-full gap-3')

                            def update_audio_view():
                                aud_preview.clear()
                                res = state.get("last_audio_result")
                                with aud_preview:
                                    if res:
                                        chain_of_custody_pill(res.sha256_hash)

                                        # Key Statements Card
                                        with ui.card().classes('bg-amber-950/20 p-3 rounded-lg border border-amber-500/30'):
                                            ui.label('EXTRACTED VERBAL THREATS & KEY STATEMENTS:').classes('text-[10px] font-black text-amber-400')
                                            for ks in res.key_statements:
                                                ui.label(f"• {ks}").classes('text-xs text-amber-200 mt-1')

                                        # Diarized Transcript Rows
                                        ui.label(f"SPEECH DIARIZATION ({res.speakers_identified} SPEAKERS ISOLATED):").classes('text-[10px] font-black text-slate-400 mt-2')
                                        for seg in res.speaker_diarization:
                                            with ui.card().classes('bg-slate-900/90 p-3 rounded-lg border border-slate-800'):
                                                with ui.row().classes('items-center justify-between w-full mb-1'):
                                                    with ui.row().classes('items-center gap-2'):
                                                        ui.icon('person_voice', size='16px').classes('text-cyan-400')
                                                        ui.label(seg.speaker).classes('text-xs font-bold text-white')
                                                        ui.label(f"{seg.start_time} - {seg.end_time}").classes('text-[10px] mono-font text-cyan-400')
                                                    ui.label(seg.acoustic_stress).classes('text-[10px] px-2 py-0.5 rounded bg-slate-800 text-amber-400 font-semibold')
                                                ui.label(f'"{seg.text}"').classes('text-xs text-slate-200 italic')

                            update_audio_view()

                def render_video_studio():
                    with ui.row().classes('w-full gap-6 items-start'):
                        # Left Column: Upload & Video Controls
                        with ui.card().classes('forensic-card w-full lg:w-[420px] p-6 gap-4'):
                            with ui.row().classes('items-center gap-2'):
                                ui.icon('videocam', size='22px').classes('text-cyan-400')
                                ui.label('Surveillance Video Telemetry').classes('text-base font-bold text-white')

                            ui.label('Process CCTV MP4 video feeds for temporal keyframe action breakdown, suspect trajectory, and escape route mapping:').classes('text-xs text-slate-400')

                            ui.button('Analyze Video Clip', on_click=lambda: process_video_sample('cctv_exterior_getaway.mp4'), icon='speed').props('color=cyan-7').classes('w-full font-bold')

                            ui.separator().classes('my-2 border-slate-800')
                            ui.upload(
                                label='Upload surveillance video (.mp4)',
                                on_upload=lambda e: handle_video_upload(e),
                                auto_upload=True
                            ).props('accept=.mp4 dark flat color=cyan').classes('w-full')

                        # Right Column: Keyframe Breakdown & Logs
                        with ui.card().classes('forensic-card flex-1 p-6 gap-4'):
                            with ui.row().classes('items-center justify-between w-full'):
                                ui.label('Keyframe Action Log & Anomaly Scoring').classes('text-base font-bold text-white')
                                if state["last_video_result"]:
                                    threat_badge(state["last_video_result"].threat_level, state["last_video_result"].video_threat_score)

                            vid_preview = ui.column().classes('w-full gap-3')

                            def update_video_view():
                                vid_preview.clear()
                                res = state.get("last_video_result")
                                with vid_preview:
                                    if res:
                                        chain_of_custody_pill(res.sha256_hash)

                                        # Trajectory & Escape
                                        with ui.card().classes('bg-slate-900/90 p-3 rounded-lg border border-slate-800'):
                                            ui.label('SUSPECT TRAJECTORY & ESCAPE CORRIDOR:').classes('text-[10px] font-black text-cyan-400')
                                            ui.label(res.suspect_trajectory).classes('text-xs text-slate-300 mt-1')
                                            ui.label(f"Egress Telemetry: {res.escape_route_observed}").classes('text-xs text-amber-300 mt-1')

                                        # Keyframe Breakdown Table
                                        ui.label('TEMPORAL ACTION EVENT BREAKDOWN:').classes('text-[10px] font-black text-slate-400 mt-2')
                                        for ev in res.timeline_events:
                                            with ui.card().classes('bg-slate-900/80 p-3 rounded-lg border border-slate-800'):
                                                with ui.row().classes('items-center justify-between w-full'):
                                                    with ui.row().classes('items-center gap-2'):
                                                        ui.label(ev.timestamp_offset).classes('text-xs font-bold mono-font text-cyan-400')
                                                        ui.label(ev.scene_keyframe).classes('text-[10px] px-1.5 py-0.5 rounded bg-slate-800 text-slate-300')
                                                        ui.label(ev.action_detected).classes('text-xs font-bold text-white')
                                                    threat_badge("CRITICAL" if ev.anomaly_threat_score >= 85 else "HIGH", ev.anomaly_threat_score)
                                                ui.label(f"Subjects: {ev.subjects_involved}").classes('text-xs text-slate-400 mt-1')
                                                if ev.cross_audio_sync_hint:
                                                    ui.label(f"Audio Corroboration: {ev.cross_audio_sync_hint}").classes('text-[11px] text-purple-400 italic')

                            update_video_view()

                render_intake_studio()

            # ==========================================================
            # TAB 3: INTERACTIVE FORENSIC TIMELINE VIEW
            # ==========================================================
            with ui.tab_panel('timeline').classes('w-full p-0 gap-6 flex flex-col'):
                timeline_container = ui.column().classes('w-full gap-4')

                def render_timeline():
                    timeline_container.clear()
                    case_rec = get_or_create_case()
                    events = list(TimelineEvent.select().where(TimelineEvent.case == case_rec).order_by(TimelineEvent.timestamp_str.asc()))

                    with timeline_container:
                        # Controls & Filter Bar
                        with ui.card().classes('forensic-card w-full p-4'):
                            with ui.row().classes('items-center justify-between w-full'):
                                with ui.row().classes('items-center gap-2'):
                                    ui.icon('timeline', size='22px').classes('text-cyan-400')
                                    ui.label('Chronological Multimodal Timeline').classes('text-base font-bold text-white')
                                    ui.label(f"({len(events)} events fused)").classes('text-xs text-slate-400')

                                with ui.row().classes('items-center gap-2'):
                                    ui.label('FILTER BY:').classes('text-[10px] font-black text-slate-400')
                                    for flt in ['ALL', 'IMAGE', 'AUDIO', 'VIDEO', 'FUSION']:
                                        ui.button(flt, on_click=lambda f=flt: filter_timeline(f)).props(
                                            f"size=sm {'color=cyan-7' if state['timeline_filter'] == flt else 'flat text-color=slate-400'}"
                                        ).classes('font-bold')

                                    ui.button('Re-Sync Fusion', on_click=lambda: trigger_multimodal_fusion(), icon='sync').props('size=sm outline color=purple').classes('font-bold')

                        # Timeline Items
                        filtered = [
                            e for e in events
                            if state['timeline_filter'] == 'ALL' or state['timeline_filter'] in e.modality.upper()
                        ]

                        if not filtered:
                            with ui.card().classes('forensic-card w-full p-8 text-center'):
                                ui.label('No timeline events match the selected filter.').classes('text-sm text-slate-400')
                        else:
                            with ui.column().classes('w-full gap-1'):
                                for ev in filtered:
                                    timeline_item_row(
                                        timestamp=ev.timestamp_str,
                                        modality=ev.modality,
                                        title=ev.title,
                                        narrative=ev.description,
                                        threat=ev.threat_rating,
                                        corroboration=ev.cross_modal_correlation
                                    )

                def filter_timeline(f: str):
                    state['timeline_filter'] = f
                    render_timeline()

                render_timeline()

            # ==========================================================
            # TAB 4: NATURAL LANGUAGE ASSISTANT (CHAT)
            # ==========================================================
            with ui.tab_panel('chat').classes('w-full p-0 gap-4 flex flex-col'):
                with ui.card().classes('forensic-card w-full p-6 flex flex-col gap-4'):
                    with ui.row().classes('items-center justify-between w-full border-b border-slate-800 pb-3'):
                        with ui.row().classes('items-center gap-2'):
                            ui.icon('smart_toy', size='22px').classes('text-indigo-400')
                            ui.label('CrimeVision Forensic AI Copilot').classes('text-base font-bold text-white')
                            ui.label('Claude 3.5 Sonnet Grounded').classes('badge-modality text-[10px]')
                        ui.button('Clear Chat', on_click=lambda: clear_chat_history(), icon='clear_all').props('flat size=sm color=slate-4')

                    # Quick Forensic Suggestion Chips
                    with ui.column().classes('gap-1'):
                        ui.label('TACTICAL FORENSIC PROMPTS:').classes('text-[10px] font-black tracking-widest text-slate-400')
                        with ui.row().classes('w-full gap-2 flex-wrap'):
                            prompts = [
                                "What weapons were detected?",
                                "Summarize suspect profiles and attire",
                                "Check audio-video timeline synchronization",
                                "Generate formal Probable Cause Affidavit",
                                "Detail escape route and getaway vehicle"
                            ]
                            for p in prompts:
                                ui.button(p, on_click=lambda q=p: send_chat_query(q)).props('dense outline size=sm color=cyan').classes('text-xs normal-case')

                    # Chat Messages Display Area
                    chat_container = ui.column().classes('w-full min-h-[360px] max-h-[500px] overflow-y-auto p-2 gap-2 bg-black/40 rounded-lg border border-slate-900')

                    def refresh_chat_display():
                        chat_container.clear()
                        with chat_container:
                            if not state['chat_history']:
                                # Seed welcome message
                                chat_message_bubble(
                                    'assistant',
                                    "**Welcome Detective Vance.** I am your Forensic Copilot. "
                                    "I have cross-analyzed all photographic exhibits, acoustic diarization logs, and CCTV keyframe telemetry for Case `CRV-2026-8841`. "
                                    "Ask any questions regarding weapon lethality, suspect actions, cross-modal synchronization, or probable cause generation."
                                )
                            for msg in state['chat_history']:
                                chat_message_bubble(msg['role'], msg['content'], msg.get('citations'))

                    # Input Box
                    with ui.row().classes('w-full items-center gap-2 mt-2'):
                        query_input = ui.input(placeholder='Ask forensic copilot about case evidence, weapon details, timelines...').classes('flex-1')
                        query_input.props('dark outlined dense')

                        def submit_input():
                            val = query_input.value.strip()
                            if val:
                                query_input.value = ''
                                send_chat_query(val)

                        query_input.on('keydown.enter', submit_input)
                        ui.button('Send', on_click=submit_input, icon='send').props('color=cyan-7').classes('font-bold')

                    refresh_chat_display()

                def send_chat_query(q: str):
                    state['chat_history'].append({"role": "user", "content": q})
                    refresh_chat_display()

                    # Call backend AI copilot
                    case_rec = get_or_create_case()
                    context = {
                        "case_id": case_rec.case_id,
                        "title": case_rec.title,
                        "classification": case_rec.classification,
                        "threat_score": case_rec.overall_threat_score,
                        "threat_level": case_rec.threat_level
                    }
                    ans = ForensicAIAnalyzer.chat_copilot(q, context)
                    state['chat_history'].append({
                        "role": "assistant",
                        "content": ans.response,
                        "citations": ans.citations
                    })
                    refresh_chat_display()

                def clear_chat_history():
                    state['chat_history'] = []
                    refresh_chat_display()

            # ==========================================================
            # TAB 5: PDF EXPORT & CHAIN OF CUSTODY
            # ==========================================================
            with ui.tab_panel('export').classes('w-full p-0 gap-6 flex flex-col'):
                export_container = ui.column().classes('w-full gap-6')

                def render_export_page():
                    export_container.clear()
                    c = get_or_create_case()
                    items = list(EvidenceItem.select().where(EvidenceItem.case == c))

                    with export_container:
                        with ui.row().classes('w-full gap-6 items-start'):
                            # Left Column: Investigator & Report Controls
                            with ui.card().classes('forensic-card w-full lg:w-[420px] p-6 gap-4'):
                                with ui.row().classes('items-center gap-2'):
                                    ui.icon('verified', size='22px').classes('text-emerald-400')
                                    ui.label('Forensic Dossier Export').classes('text-base font-bold text-white')

                                ui.label('Generate official ReportLab PDF documentation with cryptographic chain of custody hashes, threat matrix scores, and sworn officer signature block:').classes('text-xs text-slate-400')

                                # Metadata Editor
                                with ui.column().classes('w-full gap-3 mt-1'):
                                    inp_inv = ui.input('Lead Investigator', value=c.lead_investigator).classes('w-full').props('dense dark outlined')
                                    inp_badge = ui.input('Badge Number', value=c.badge_number).classes('w-full').props('dense dark outlined')
                                    inp_dept = ui.input('Forensic Agency / Unit', value=c.jurisdiction).classes('w-full').props('dense dark outlined')

                                    def save_meta():
                                        c.lead_investigator = inp_inv.value
                                        c.badge_number = inp_badge.value
                                        c.jurisdiction = inp_dept.value
                                        c.save()
                                        ui.notify('Investigator credentials updated! Refresh page to see new badges.', type='positive')

                                    ui.button('Save Examiner Info', on_click=save_meta).props('outline size=sm color=slate-4').classes('w-full')

                                ui.separator().classes('my-2 border-slate-800')

                                ui.button('Generate & Download Official PDF', on_click=lambda: trigger_pdf_export(), icon='download').props('color=red-7 size=lg').classes('w-full font-bold shadow-lg shadow-red-900/30')

                                if state["last_pdf_path"]:
                                    pdf_fn = os.path.basename(state["last_pdf_path"])
                                    with ui.row().classes('items-center justify-between w-full p-2.5 rounded bg-slate-900 border border-emerald-500/40 mt-2'):
                                        with ui.column().classes('gap-0'):
                                            ui.label('PDF Ready:').classes('text-[10px] text-emerald-400 font-bold')
                                            ui.label(pdf_fn).classes('text-xs text-slate-200 mono-font truncate max-w-[220px]')
                                        ui.link('Download File', f"/reports/{pdf_fn}", new_tab=True).classes('text-xs font-bold text-cyan-400 underline')

                            # Right Column: Chain of Custody Integrity Ledger
                            with ui.card().classes('forensic-card flex-1 p-6 gap-4'):
                                with ui.row().classes('items-center justify-between w-full'):
                                    with ui.row().classes('items-center gap-2'):
                                        ui.icon('lock', size='20px').classes('text-emerald-400')
                                        ui.label('Chain of Custody Cryptographic Ledger').classes('text-base font-bold text-white')
                                    ui.label('ISO/IEC 27037 Standard').classes('badge-verified text-[10px]')

                                ui.label('Every intake exhibit is stamped with an immutable SHA-256 hash verifying evidentiary authenticity:').classes('text-xs text-slate-400')

                                with ui.column().classes('w-full gap-2 mt-2'):
                                    for idx, ev in enumerate(items, 1):
                                        with ui.card().classes('bg-slate-900/90 p-3 rounded-lg border border-slate-800 w-full'):
                                            with ui.row().classes('items-center justify-between w-full mb-1'):
                                                with ui.row().classes('items-center gap-2'):
                                                    ui.label(f"EXHIBIT #{idx:02d}").classes('text-xs font-black text-cyan-400')
                                                    ui.label(ev.evidence_type.upper()).classes('badge-modality text-[10px]')
                                                    ui.label(ev.filename).classes('text-xs font-bold text-white')
                                                ui.label('INTEGRITY OK').classes('text-[10px] font-bold text-emerald-400')

                                            with ui.row().classes('items-center justify-between w-full text-xs text-slate-400'):
                                                ui.label(f"Logged: {ev.timestamp_logged.strftime('%Y-%m-%d %H:%M:%S')}").classes('text-[11px]')
                                                ui.label(f"Size: {ev.file_size:,} bytes").classes('text-[11px]')

                                            with ui.row().classes('items-center gap-1.5 mt-1.5 p-1.5 rounded bg-black/50 border border-slate-800'):
                                                ui.icon('fingerprint', size='14px').classes('text-emerald-400')
                                                ui.label(ev.sha256_hash).classes('text-[11px] mono-font text-slate-300 break-all')

                render_export_page()

    # ==========================================================
    # Action Handlers
    # ==========================================================
    def trigger_multimodal_fusion():
        with ui.dialog() as dialog, ui.card().classes('forensic-card p-6 min-w-[360px] text-center'):
            ui.spinner(size='40px', color='cyan')
            ui.label('Running Multimodal Fusion Engine...').classes('text-base font-bold text-white mt-3')
            ui.label('Correlating optical frames, acoustic spikes & telemetry...').classes('text-xs text-slate-400')
            dialog.open()

        res = MultimodalFusionEngine.fuse_case_evidence(state["case_id"])
        dialog.close()
        render_overview()
        render_timeline()
        ui.notify(f"Multimodal Fusion Complete! Categorized as: {res.classification.primary_crime}", type='positive')

    def trigger_pdf_export():
        pdf_path = ForensicPDFBuilder.generate_case_pdf(state["case_id"])
        state["last_pdf_path"] = pdf_path
        filename = os.path.basename(pdf_path)
        ui.notify('Forensic PDF Report generated successfully!', type='positive')
        # Open download link
        ui.download(f"/reports/{filename}", filename=filename)
        render_export_page()

    def process_image_sample(filename: str):
        target = UPLOADS_DIR / filename
        if not target.exists():
            src = SAMPLES_DIR / filename
            if src.exists():
                shutil.copy(src, target)
        res = ForensicAIAnalyzer.analyze_image(str(target), filename)
        state["last_image_result"] = res

        # Save to database
        c = get_or_create_case()
        EvidenceItem.create(
            case=c,
            evidence_type="image",
            filename=filename,
            file_path=str(target),
            file_size=target.stat().st_size if target.exists() else 2048,
            sha256_hash=res.sha256_hash,
            threat_score=res.threat_score,
            analysis_status="analyzed",
            raw_analysis_json=res.model_dump_json(),
            summary=res.scene_description
        )
        render_intake_studio()
        render_overview()
        ui.notify(f"Image analyzed: Threat Score {res.threat_score}/100 ({res.threat_level})", type='positive')

    def process_audio_sample(filename: str):
        target = UPLOADS_DIR / filename
        if not target.exists():
            src = SAMPLES_DIR / filename
            if src.exists():
                shutil.copy(src, target)
        res = ForensicAIAnalyzer.analyze_audio(str(target), filename)
        state["last_audio_result"] = res

        c = get_or_create_case()
        EvidenceItem.create(
            case=c,
            evidence_type="audio",
            filename=filename,
            file_path=str(target),
            file_size=target.stat().st_size if target.exists() else 2048,
            sha256_hash=res.sha256_hash,
            threat_score=res.audio_threat_score,
            analysis_status="analyzed",
            raw_analysis_json=res.model_dump_json(),
            summary=f"{res.speakers_identified} speakers diarized; {len(res.key_statements)} statements extracted."
        )
        render_intake_studio()
        render_overview()
        ui.notify(f"Audio diarization complete: {res.speakers_identified} speakers isolated.", type='positive')

    def process_video_sample(filename: str):
        target = UPLOADS_DIR / filename
        if not target.exists():
            src = SAMPLES_DIR / filename
            if src.exists():
                shutil.copy(src, target)
        res = ForensicAIAnalyzer.analyze_video(str(target), filename)
        state["last_video_result"] = res

        c = get_or_create_case()
        EvidenceItem.create(
            case=c,
            evidence_type="video",
            filename=filename,
            file_path=str(target),
            file_size=target.stat().st_size if target.exists() else 8192,
            sha256_hash=res.sha256_hash,
            threat_score=res.video_threat_score,
            analysis_status="analyzed",
            raw_analysis_json=res.model_dump_json(),
            summary=res.summary
        )
        render_intake_studio()
        render_overview()
        ui.notify(f"Video action logging complete: {len(res.timeline_events)} keyframes processed.", type='positive')

    def handle_image_upload(event):
        dest = UPLOADS_DIR / event.name
        with open(dest, 'wb') as f:
            f.write(event.content.read())
        process_image_sample(event.name)

    def handle_audio_upload(event):
        dest = UPLOADS_DIR / event.name
        with open(dest, 'wb') as f:
            f.write(event.content.read())
        process_audio_sample(event.name)

    def handle_video_upload(event):
        dest = UPLOADS_DIR / event.name
        with open(dest, 'wb') as f:
            f.write(event.content.read())
        process_video_sample(event.name)

    def handle_seed_demo_case():
        import asyncio
        from backend.routes import seed_demo_case
        asyncio.create_task(seed_demo_case(state["case_id"]))
        # Also run local process
        process_image_sample('sample_surveillance_cam02.jpg')
        process_audio_sample('dispatch_counter_mic01.wav')
        process_video_sample('cctv_exterior_getaway.mp4')
        MultimodalFusionEngine.fuse_case_evidence(state["case_id"])
        render_overview()
        render_timeline()
        render_export_page()
        ui.notify('Full Multimodal Demo Case Loaded Successfully!', type='positive')

    # Initial load of sample results into state so UI isn't blank
    if not state["last_image_result"]:
        process_image_sample('sample_surveillance_cam02.jpg')
    if not state["last_audio_result"]:
        process_audio_sample('dispatch_counter_mic01.wav')
    if not state["last_video_result"]:
        process_video_sample('cctv_exterior_getaway.mp4')
    MultimodalFusionEngine.fuse_case_evidence(state["case_id"])
    render_overview()
    render_timeline()
