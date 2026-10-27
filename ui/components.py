from typing import Optional, Callable, Dict, Any, List
from nicegui import ui

def header_bar(case_id: str, lead_inv: str, on_seed: Optional[Callable] = None):
    """Renders the top enterprise tactical header."""
    with ui.header().classes('forensic-header w-full px-6 py-3 flex items-center justify-between z-50'):
        # Brand & Title
        with ui.row().classes('items-center gap-3'):
            with ui.avatar(icon='security', color='transparent', text_color='cyan-400').classes('border border-cyan-500/40 shadow-lg shadow-cyan-500/20'):
                ui.icon('radar', size='28px').classes('text-cyan-400')
            with ui.column().classes('gap-0'):
                with ui.row().classes('items-center gap-2'):
                    ui.label('CRIMEVISION AI').classes('text-lg font-black tracking-wider text-white')
                    ui.label('ENTERPRISE FORENSICS').classes('badge-modality text-[10px]')
                ui.label('Multimodal Forensic Analysis & Chronological Fusion Platform').classes('text-xs text-slate-400')

        # Status & Case Metadata
        with ui.row().classes('items-center gap-4'):
            # Live Status Indicator
            with ui.row().classes('items-center gap-2 px-3 py-1.5 rounded-full bg-slate-900/90 border border-slate-700/60'):
                ui.element('div').classes('w-2.5 h-2.5 rounded-full bg-red-500 live-pulse')
                ui.label('LIVE EVIDENCE STREAM').classes('text-xs font-bold text-red-400 tracking-wider')

            # Active Case Badge
            with ui.column().classes('gap-0 text-right'):
                ui.label(f'CASE: {case_id}').classes('text-xs font-bold text-cyan-400 mono-font')
                ui.label(lead_inv).classes('text-[11px] text-slate-400')

            # AI Engine Indicator
            with ui.row().classes('items-center gap-1.5 px-3 py-1.5 rounded-lg bg-indigo-950/60 border border-indigo-500/30'):
                ui.icon('psychology', size='18px').classes('text-indigo-400')
                ui.label('Claude 3.5 Sonnet Multimodal').classes('text-xs font-semibold text-indigo-300')

            if on_seed:
                ui.button('Load Full Demo Case', on_click=on_seed, icon='auto_fix_high').props('outline size=sm color=cyan').classes('font-bold tracking-wide')


def kpi_card(title: str, value: str, subtitle: str, icon: str, color_hex: str = "#38bdf8"):
    """Renders a forensic KPI metric card."""
    with ui.card().classes('forensic-card p-5 flex flex-col justify-between flex-1 min-w-[200px]'):
        with ui.row().classes('items-center justify-between w-full'):
            ui.label(title).classes('text-xs font-bold uppercase tracking-wider text-slate-400')
            ui.icon(icon, size='24px').style(f'color: {color_hex};')
        with ui.column().classes('gap-1 my-2'):
            ui.label(value).classes('text-2xl font-black tracking-tight text-white mono-font')
            ui.label(subtitle).classes('text-xs font-medium text-slate-400')


def threat_badge(level: str, score: int):
    """Renders a threat level badge with color coding."""
    lvl = level.upper()
    if lvl in ["CRITICAL", "EXTREME"]:
        css = "badge-threat-critical"
    elif lvl in ["HIGH", "ELEVATED"]:
        css = "badge-threat-high"
    else:
        css = "badge-verified"
    return ui.label(f"{lvl} • {score}/100").classes(css)


def chain_of_custody_pill(sha256: str):
    """Renders a verified cryptographic hash pill."""
    truncated = f"{sha256[:10]}...{sha256[-8:]}" if len(sha256) > 20 else sha256
    with ui.row().classes('items-center gap-1.5 px-2.5 py-1 rounded bg-slate-900 border border-emerald-500/30'):
        ui.icon('verified', size='14px').classes('text-emerald-400')
        ui.label('SHA-256:').classes('text-[11px] font-bold text-emerald-400')
        ui.label(truncated).classes('text-[11px] mono-font text-slate-300')


def timeline_item_row(timestamp: str, modality: str, title: str, narrative: str, threat: str, corroboration: str):
    """Renders a single chronological timeline item."""
    with ui.card().classes('forensic-card w-full p-4 mb-3 border-l-4 border-l-cyan-400'):
        with ui.row().classes('items-center justify-between w-full mb-1'):
            with ui.row().classes('items-center gap-2'):
                ui.icon('schedule', size='16px').classes('text-cyan-400')
                ui.label(timestamp).classes('text-sm font-bold mono-font text-cyan-300')
                ui.label(modality).classes('badge-modality text-[10px]')
            with ui.row().classes('items-center gap-2'):
                threat_badge(threat, 90 if threat == 'CRITICAL' else 75)

        ui.label(title).classes('text-base font-bold text-white mt-1')
        ui.label(narrative).classes('text-sm text-slate-300 leading-relaxed mt-1')

        if corroboration:
            with ui.row().classes('items-center gap-1.5 mt-2.5 pt-2 border-t border-slate-800 text-xs text-slate-400'):
                ui.icon('sync_alt', size='14px').classes('text-purple-400')
                ui.label(f"Cross-Modal Corroboration: {corroboration}").classes('text-purple-300')


def chat_message_bubble(role: str, content: str, citations: Optional[List[str]] = None):
    """Renders a styled chat bubble for the Forensic Copilot."""
    is_user = role == 'user'
    align = 'items-end' if is_user else 'items-start'
    bg_style = 'bg-cyan-950/40 border border-cyan-500/40 text-cyan-50' if is_user else 'bg-slate-900/90 border border-slate-700/70 text-slate-100'

    with ui.column().classes(f'w-full {align} my-2'):
        with ui.row().classes('items-center gap-2 mb-1 px-1'):
            ui.icon('person' if is_user else 'smart_toy', size='14px').classes('text-cyan-400' if is_user else 'text-indigo-400')
            ui.label('Investigator' if is_user else 'CrimeVision Copilot (Claude 3.5)').classes('text-[11px] font-bold tracking-wider uppercase text-slate-400')

        with ui.card().classes(f'{bg_style} p-4 rounded-xl max-w-[85%] shadow-md'):
            ui.markdown(content).classes('text-sm leading-relaxed')

            if citations and len(citations) > 0:
                with ui.column().classes('mt-3 pt-2.5 border-t border-slate-800 w-full gap-1'):
                    ui.label('EVIDENTIARY CITATIONS:').classes('text-[10px] font-black tracking-widest text-cyan-400')
                    for cit in citations:
                        with ui.row().classes('items-center gap-1 text-[11px] text-slate-400'):
                            ui.icon('link', size='12px').classes('text-cyan-400')
                            ui.label(cit)
