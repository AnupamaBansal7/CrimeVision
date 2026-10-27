from nicegui import ui

FORENSIC_THEME_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

:root {
    --bg-dark: #070a13;
    --card-bg: rgba(15, 23, 42, 0.75);
    --card-border: rgba(56, 189, 248, 0.18);
    --accent-cyan: #38bdf8;
    --accent-red: #ef4444;
    --accent-amber: #f59e0b;
    --accent-emerald: #10b981;
    --accent-purple: #a855f7;
    --text-primary: #f8fafc;
    --text-muted: #94a3b8;
}

body {
    background-color: var(--bg-dark) !important;
    color: var(--text-primary) !important;
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
    margin: 0;
    padding: 0;
    overflow-x: hidden;
}

.mono-font {
    font-family: 'JetBrains Mono', monospace !important;
}

/* Glassmorphism Tactical Cards */
.forensic-card {
    background: var(--card-bg) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border: 1px solid var(--card-border) !important;
    border-radius: 12px !important;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.45) !important;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}

.forensic-card:hover {
    border-color: rgba(56, 189, 248, 0.4) !important;
    box-shadow: 0 12px 40px 0 rgba(56, 189, 248, 0.12) !important;
}

.forensic-card-critical {
    border-color: rgba(239, 68, 68, 0.4) !important;
}
.forensic-card-critical:hover {
    box-shadow: 0 12px 40px 0 rgba(239, 68, 68, 0.18) !important;
}

/* Top Navigation Bar */
.forensic-header {
    background: rgba(11, 17, 32, 0.92) !important;
    backdrop-filter: blur(16px) !important;
    border-bottom: 1px solid rgba(56, 189, 248, 0.2) !important;
}

/* Custom Tactical Badges */
.badge-threat-critical {
    background: rgba(239, 68, 68, 0.15) !important;
    color: #ef4444 !important;
    border: 1px solid rgba(239, 68, 68, 0.4) !important;
    padding: 3px 10px !important;
    border-radius: 6px !important;
    font-size: 0.75rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.05em !important;
    text-transform: uppercase !important;
}

.badge-threat-high {
    background: rgba(245, 158, 11, 0.15) !important;
    color: #f59e0b !important;
    border: 1px solid rgba(245, 158, 11, 0.4) !important;
    padding: 3px 10px !important;
    border-radius: 6px !important;
    font-size: 0.75rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.05em !important;
}

.badge-verified {
    background: rgba(16, 185, 129, 0.15) !important;
    color: #10b981 !important;
    border: 1px solid rgba(16, 185, 129, 0.4) !important;
    padding: 3px 10px !important;
    border-radius: 6px !important;
    font-size: 0.75rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.05em !important;
}

.badge-modality {
    background: rgba(56, 189, 248, 0.15) !important;
    color: #38bdf8 !important;
    border: 1px solid rgba(56, 189, 248, 0.35) !important;
    padding: 3px 10px !important;
    border-radius: 6px !important;
    font-size: 0.75rem !important;
    font-weight: 700 !important;
}

/* Scrollbars */
::-webkit-scrollbar {
    width: 6px;
    height: 6px;
}
::-webkit-scrollbar-track {
    background: #0b1120;
}
::-webkit-scrollbar-thumb {
    background: #1e293b;
    border-radius: 3px;
}
::-webkit-scrollbar-thumb:hover {
    background: #38bdf8;
}

/* Pulse animation for Live Forensic Indicator */
@keyframes pulseGlow {
    0% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.7); }
    70% { box-shadow: 0 0 0 8px rgba(239, 68, 68, 0); }
    100% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0); }
}

.live-pulse {
    animation: pulseGlow 2s infinite;
}

/* Quasar Component Overrides for NiceGUI */
.q-tab {
    color: #94a3b8 !important;
    font-weight: 600 !important;
    letter-spacing: 0.03em !important;
    text-transform: none !important;
    font-size: 0.95rem !important;
    padding: 0 18px !important;
    min-height: 48px !important;
}
.q-tab--active {
    color: #38bdf8 !important;
    background: rgba(56, 189, 248, 0.08) !important;
    border-bottom: 2px solid #38bdf8 !important;
}
.q-field__control {
    background: rgba(15, 23, 42, 0.8) !important;
    border: 1px solid rgba(56, 189, 248, 0.2) !important;
    border-radius: 8px !important;
}
.q-field__native {
    color: #f8fafc !important;
}
.q-chip {
    background: rgba(30, 41, 59, 0.9) !important;
    color: #e2e8f0 !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
}
</style>
"""

def apply_theme():
    """Injects dark cyber-forensic styling into NiceGUI head."""
    ui.add_head_html(FORENSIC_THEME_CSS)
