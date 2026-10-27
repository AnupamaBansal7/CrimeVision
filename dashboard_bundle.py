# Generated bundle for CrimeVision AI dashboard
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PUBLIC_DIR = BASE_DIR / "public"

CSS_CONTENT = """@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

:root {
  --bg-dark: #070a13;
  --bg-panel: rgba(15, 23, 42, 0.85);
  --bg-card: rgba(17, 24, 39, 0.7);
  --border-subtle: rgba(56, 189, 248, 0.15);
  --border-focus: rgba(56, 189, 248, 0.45);
  --accent-cyan: #38bdf8;
  --accent-blue: #0284c7;
  --accent-red: #ef4444;
  --accent-amber: #f59e0b;
  --accent-emerald: #10b981;
  --accent-purple: #a855f7;
  --text-primary: #f8fafc;
  --text-secondary: #94a3b8;
  --text-muted: #64748b;
  --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  background-color: var(--bg-dark);
  color: var(--text-primary);
  font-family: var(--font-sans);
  min-height: 100vh;
  overflow-x: hidden;
  background-image:
    radial-gradient(ellipse 80% 50% at 50% -20%, rgba(14, 165, 233, 0.15), transparent),
    radial-gradient(circle at 100% 100%, rgba(168, 85, 247, 0.06), transparent 30%);
}

.mono {
  font-family: var(--font-mono);
}

/* Custom Scrollbar */
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}
::-webkit-scrollbar-track {
  background: rgba(15, 23, 42, 0.6);
}
::-webkit-scrollbar-thumb {
  background: rgba(56, 189, 248, 0.25);
  border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover {
  background: rgba(56, 189, 248, 0.5);
}

/* Header Bar */
.forensic-header {
  position: sticky;
  top: 0;
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.85rem 2rem;
  background: rgba(10, 15, 30, 0.94);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--border-subtle);
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.5);
}

.brand-section {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.brand-icon {
  width: 42px;
  height: 42px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(14, 165, 233, 0.12);
  border: 1px solid rgba(56, 189, 248, 0.4);
  box-shadow: 0 0 16px rgba(56, 189, 248, 0.2);
  color: var(--accent-cyan);
}

.brand-text h1 {
  font-size: 1.15rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  display: flex;
  align-items: center;
  gap: 0.6rem;
}

.brand-text p {
  font-size: 0.72rem;
  color: var(--text-secondary);
}

.header-status-group {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.status-pill {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.35rem 0.85rem;
  border-radius: 9999px;
  background: rgba(15, 23, 42, 0.9);
  border: 1px solid rgba(51, 65, 85, 0.8);
  font-size: 0.75rem;
  font-weight: 700;
}

.pulse-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background-color: var(--accent-red);
  box-shadow: 0 0 8px var(--accent-red);
  animation: pulse-ring 1.8s infinite;
}

@keyframes pulse-ring {
  0% { transform: scale(0.95); opacity: 0.8; }
  50% { transform: scale(1.25); opacity: 1; box-shadow: 0 0 12px var(--accent-red); }
  100% { transform: scale(0.95); opacity: 0.8; }
}

.ai-engine-chip {
  display: flex;
  align-items: center;
  gap: 0.45rem;
  padding: 0.35rem 0.85rem;
  border-radius: 8px;
  background: rgba(88, 28, 135, 0.25);
  border: 1px solid rgba(168, 85, 247, 0.35);
  color: #d8b4fe;
  font-size: 0.75rem;
  font-weight: 600;
}

.btn-tactical {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.45rem 1rem;
  border-radius: 8px;
  font-size: 0.8rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s ease;
  border: 1px solid var(--accent-cyan);
  background: rgba(14, 165, 233, 0.12);
  color: var(--accent-cyan);
}
.btn-tactical:hover {
  background: rgba(14, 165, 233, 0.25);
  box-shadow: 0 0 14px rgba(56, 189, 248, 0.3);
  transform: translateY(-1px);
}

.btn-primary {
  background: linear-gradient(135deg, #0284c7, #0369a1);
  border: 1px solid rgba(56, 189, 248, 0.5);
  color: #fff;
}
.btn-primary:hover {
  background: linear-gradient(135deg, #0369a1, #075985);
  box-shadow: 0 0 18px rgba(56, 189, 248, 0.4);
}

.btn-danger {
  background: rgba(239, 68, 68, 0.15);
  border: 1px solid rgba(239, 68, 68, 0.5);
  color: #fca5a5;
}
.btn-danger:hover {
  background: rgba(239, 68, 68, 0.3);
  box-shadow: 0 0 14px rgba(239, 68, 68, 0.3);
}

/* Navigation Tabs */
.tabs-container {
  max-width: 1380px;
  margin: 1.5rem auto 0;
  padding: 0 1.5rem;
}

.nav-tabs {
  display: flex;
  gap: 0.5rem;
  border-bottom: 1px solid rgba(51, 65, 85, 0.8);
  background: rgba(15, 23, 42, 0.6);
  padding: 0.4rem 0.6rem 0;
  border-radius: 12px 12px 0 0;
  overflow-x: auto;
}

.tab-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.25rem;
  background: transparent;
  border: none;
  border-bottom: 2px solid transparent;
  color: var(--text-secondary);
  font-family: var(--font-sans);
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.2s ease;
}

.tab-btn:hover {
  color: var(--accent-cyan);
  background: rgba(56, 189, 248, 0.05);
  border-radius: 6px 6px 0 0;
}

.tab-btn.active {
  color: var(--accent-cyan);
  border-bottom-color: var(--accent-cyan);
  background: rgba(56, 189, 248, 0.1);
  border-radius: 6px 6px 0 0;
}

/* Main Content Area */
.main-content {
  max-width: 1380px;
  margin: 0 auto;
  padding: 1.5rem 1.5rem 4rem;
}

.tab-panel {
  display: none;
  animation: fadeIn 0.25s ease-in-out;
}
.tab-panel.active {
  display: block;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Forensic Cards */
.forensic-card {
  background: var(--bg-card);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid var(--border-subtle);
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}
.forensic-card:hover {
  border-color: var(--border-focus);
  box-shadow: 0 12px 40px rgba(56, 189, 248, 0.08);
}

/* Dossier Banner */
.dossier-banner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1.25rem;
  margin-bottom: 1.5rem;
  border-left: 4px solid var(--accent-cyan);
}

.dossier-title-row {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 0.4rem;
}

.dossier-title {
  font-size: 1.35rem;
  font-weight: 800;
  letter-spacing: 0.02em;
}

.dossier-meta {
  font-size: 0.78rem;
  color: var(--text-secondary);
}

/* KPI Grid */
.kpi-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.25rem;
  margin-bottom: 1.5rem;
}

.kpi-card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 120px;
}

.kpi-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 0.5rem;
}

.kpi-label {
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-muted);
}

.kpi-value {
  font-size: 1.55rem;
  font-weight: 800;
  color: #fff;
  letter-spacing: -0.02em;
}

.kpi-subtitle {
  font-size: 0.75rem;
  color: var(--text-secondary);
  margin-top: 0.25rem;
}

/* Two Column Layout */
.grid-2col {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 1.5rem;
  margin-bottom: 1.5rem;
}
@media (max-width: 980px) {
  .grid-2col {
    grid-template-columns: 1fr;
  }
}

/* Badges */
.badge {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.25rem 0.65rem;
  border-radius: 6px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

.badge-critical {
  background: rgba(239, 68, 68, 0.15);
  color: #f87171;
  border: 1px solid rgba(239, 68, 68, 0.4);
}
.badge-high {
  background: rgba(245, 158, 11, 0.15);
  color: #fbbf24;
  border: 1px solid rgba(245, 158, 11, 0.4);
}
.badge-verified {
  background: rgba(16, 185, 129, 0.15);
  color: #34d399;
  border: 1px solid rgba(16, 185, 129, 0.4);
}
.badge-modality {
  background: rgba(56, 189, 248, 0.15);
  color: var(--accent-cyan);
  border: 1px solid rgba(56, 189, 248, 0.35);
}
.badge-purple {
  background: rgba(168, 85, 247, 0.15);
  color: #c084fc;
  border: 1px solid rgba(168, 85, 247, 0.35);
}

.sha-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.25rem 0.65rem;
  border-radius: 6px;
  background: rgba(15, 23, 42, 0.95);
  border: 1px solid rgba(16, 185, 129, 0.3);
  font-size: 0.72rem;
  color: #6ee7b7;
}

/* Evidence Studio Subtabs */
.studio-tabs {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1.25rem;
}

.studio-tab-btn {
  padding: 0.5rem 1.25rem;
  border-radius: 8px;
  background: rgba(15, 23, 42, 0.7);
  border: 1px solid rgba(51, 65, 85, 0.6);
  color: var(--text-secondary);
  font-size: 0.82rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s ease;
}
.studio-tab-btn.active {
  background: rgba(56, 189, 248, 0.15);
  border-color: var(--accent-cyan);
  color: var(--accent-cyan);
}

/* Upload Dropzone */
.dropzone {
  border: 2px dashed rgba(56, 189, 248, 0.3);
  border-radius: 12px;
  padding: 2.5rem 1.5rem;
  text-align: center;
  background: rgba(15, 23, 42, 0.5);
  cursor: pointer;
  transition: all 0.2s ease;
}
.dropzone:hover {
  border-color: var(--accent-cyan);
  background: rgba(56, 189, 248, 0.05);
}

/* Timeline */
.timeline-filters {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
  flex-wrap: wrap;
}

.filter-btn {
  padding: 0.4rem 1rem;
  border-radius: 6px;
  background: rgba(15, 23, 42, 0.8);
  border: 1px solid rgba(51, 65, 85, 0.8);
  color: var(--text-secondary);
  font-size: 0.75rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.15s ease;
}
.filter-btn.active {
  background: rgba(56, 189, 248, 0.2);
  border-color: var(--accent-cyan);
  color: var(--accent-cyan);
}

.timeline-feed {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.timeline-item {
  border-left: 3px solid var(--accent-cyan);
  padding: 1.25rem;
  background: rgba(15, 23, 42, 0.75);
  border-radius: 0 10px 10px 0;
  border-top: 1px solid var(--border-subtle);
  border-right: 1px solid var(--border-subtle);
  border-bottom: 1px solid var(--border-subtle);
  transition: all 0.2s ease;
}
.timeline-item:hover {
  border-left-width: 5px;
  background: rgba(15, 23, 42, 0.95);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

/* Chat Copilot */
.chat-container {
  display: flex;
  flex-direction: column;
  height: 600px;
}

.chat-messages {
  flex: 1;
  overflow-y: auto;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.chat-bubble {
  max-width: 80%;
  padding: 0.85rem 1.15rem;
  border-radius: 12px;
  font-size: 0.85rem;
  line-height: 1.5;
}
.chat-bubble-user {
  align-self: flex-end;
  background: rgba(14, 165, 233, 0.2);
  border: 1px solid rgba(56, 189, 248, 0.4);
  color: #f0f9ff;
}
.chat-bubble-bot {
  align-self: flex-start;
  background: rgba(30, 41, 59, 0.85);
  border: 1px solid rgba(51, 65, 85, 0.8);
  color: #e2e8f0;
}

.chat-input-row {
  display: flex;
  gap: 0.75rem;
  padding: 1rem 0 0;
  border-top: 1px solid rgba(51, 65, 85, 0.6);
}

.chat-input {
  flex: 1;
  padding: 0.75rem 1rem;
  border-radius: 8px;
  background: rgba(15, 23, 42, 0.9);
  border: 1px solid rgba(51, 65, 85, 0.8);
  color: #fff;
  font-family: var(--font-sans);
  font-size: 0.85rem;
  outline: none;
}
.chat-input:focus {
  border-color: var(--accent-cyan);
  box-shadow: 0 0 10px rgba(56, 189, 248, 0.25);
}

.quick-prompts {
  display: flex;
  gap: 0.5rem;
  overflow-x: auto;
  padding-bottom: 0.5rem;
}

.quick-prompt-btn {
  padding: 0.35rem 0.75rem;
  border-radius: 6px;
  background: rgba(88, 28, 135, 0.2);
  border: 1px solid rgba(168, 85, 247, 0.35);
  color: #d8b4fe;
  font-size: 0.72rem;
  cursor: pointer;
  white-space: nowrap;
}
.quick-prompt-btn:hover {
  background: rgba(88, 28, 135, 0.4);
}

/* Toast Notifications */
#toast {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  padding: 0.85rem 1.5rem;
  border-radius: 8px;
  background: rgba(15, 23, 42, 0.95);
  border: 1px solid var(--accent-cyan);
  box-shadow: 0 10px 30px rgba(0,0,0,0.6);
  color: #fff;
  font-size: 0.85rem;
  font-weight: 600;
  z-index: 1000;
  opacity: 0;
  transform: translateY(20px);
  transition: all 0.3s ease;
  pointer-events: none;
}
#toast.show {
  opacity: 1;
  transform: translateY(0);
}
"""

JS_CONTENT = """// CrimeVision AI – Multimodal Forensic Analysis Platform
// Frontend Controller for Vercel Serverless & Static CDN Deployment

const CASE_ID = "CRV-2026-8841";
let activeFilter = "ALL";
let allTimelineEvents = [];

// Initialize Dashboard
document.addEventListener("DOMContentLoaded", () => {
  initTabs();
  initStudioTabs();
  initFilters();
  initChat();
  loadCaseDossier();
});

// Toast notification helper
function showToast(message, isError = false) {
  const toast = document.getElementById("toast");
  if (!toast) return;
  toast.textContent = message;
  toast.style.borderColor = isError ? "var(--accent-red)" : "var(--accent-cyan)";
  toast.classList.add("show");
  setTimeout(() => toast.classList.remove("show"), 3500);
}

// Tab Switching
function initTabs() {
  const tabBtns = document.querySelectorAll(".tab-btn");
  tabBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      const target = btn.getAttribute("data-tab");
      document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
      document.querySelectorAll(".tab-panel").forEach(p => p.classList.remove("active"));

      btn.classList.add("active");
      const panel = document.getElementById(`tab-${target}`);
      if (panel) panel.classList.add("active");
    });
  });
}

function switchTab(tabId) {
  const btn = document.querySelector(`.tab-btn[data-tab="${tabId}"]`);
  if (btn) btn.click();
}

// Studio Sub-Tabs
function initStudioTabs() {
  const studioBtns = document.querySelectorAll(".studio-tab-btn");
  studioBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      const target = btn.getAttribute("data-studio");
      studioBtns.forEach(b => b.classList.remove("active"));
      document.querySelectorAll(".studio-panel").forEach(p => p.style.display = "none");

      btn.classList.add("active");
      const activePanel = document.getElementById(`studio-${target}`);
      if (activePanel) activePanel.style.display = "block";
    });
  });
}

// Timeline Filters
function initFilters() {
  const filterBtns = document.querySelectorAll(".filter-btn");
  filterBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      filterBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      activeFilter = btn.getAttribute("data-filter");
      renderTimeline(allTimelineEvents);
    });
  });
}

// Fetch Case Dossier from Backend
async function loadCaseDossier() {
  try {
    const res = await fetch(`/api/cases/${CASE_ID}`);
    if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
    const data = await res.json();
    renderCaseData(data);
  } catch (err) {
    console.warn("Could not load case dossier, attempting demo seed...", err);
    await seedDemoCase(false);
  }
}

// Render Case Data into UI
function renderCaseData(data) {
  // Metadata & Dossier Banner
  const titleElem = document.getElementById("case-title");
  if (titleElem) titleElem.textContent = data.title || "Armed Commercial Robbery - Central Metro Express";

  const metaElem = document.getElementById("case-meta");
  if (metaElem) {
    metaElem.textContent = `INCIDENT: ${data.incident_date} | LOCATION: ${data.location} | JURISDICTION: ${data.jurisdiction}`;
  }

  const threatBadgeElem = document.getElementById("case-threat-badge");
  if (threatBadgeElem) {
    threatBadgeElem.textContent = `${data.threat_level || 'CRITICAL'} • ${data.overall_threat_score || 94}/100`;
    threatBadgeElem.className = `badge ${(data.overall_threat_score >= 85) ? 'badge-critical' : 'badge-high'}`;
  }

  // KPIs
  const kpiExhibits = document.getElementById("kpi-exhibits");
  if (kpiExhibits) kpiExhibits.textContent = `${(data.evidence_items || []).length} Logged`;

  const kpiClassification = document.getElementById("kpi-classification");
  if (kpiClassification) kpiClassification.textContent = data.classification || "Armed Robbery";

  const kpiPenal = document.getElementById("kpi-penal");
  if (kpiPenal) kpiPenal.textContent = data.penal_code || "Penal Code § 211";

  const kpiThreat = document.getElementById("kpi-threat");
  if (kpiThreat) kpiThreat.textContent = `${data.threat_level || 'CRITICAL'} (${data.overall_threat_score || 94}/100)`;

  // Narrative & Affidavit
  const narrativeElem = document.getElementById("case-narrative");
  if (narrativeElem) narrativeElem.textContent = data.summary || "Multimodal evidence analysis in progress.";

  const affidavitElem = document.getElementById("case-affidavit");
  if (affidavitElem) affidavitElem.textContent = data.probable_cause || "Sworn affidavit pending multimodal fusion.";

  // Evidence Exhibits List
  renderEvidenceGrid(data.evidence_items || []);

  // Timeline
  allTimelineEvents = data.timeline_events || [];
  renderTimeline(allTimelineEvents);
}

// Render Evidence Grid
function renderEvidenceGrid(items) {
  const container = document.getElementById("evidence-grid");
  if (!container) return;
  container.innerHTML = "";

  if (items.length === 0) {
    container.innerHTML = `<div style="grid-column: 1 / -1; text-align: center; color: var(--text-muted); padding: 2rem;">No evidence items registered yet. Use the Intake Studio or click 'Load Demo Case'.</div>`;
    return;
  }

  items.forEach(item => {
    const card = document.createElement("div");
    card.className = "forensic-card";
    card.style.padding = "1rem";

    const hashShort = item.sha256 ? `${item.sha256.substring(0, 10)}...${item.sha256.substring(item.sha256.length - 8)}` : "VERIFIED";

    card.innerHTML = `
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
        <span class="badge badge-modality">${(item.type || 'EVIDENCE').toUpperCase()}</span>
        <span class="badge ${item.threat_score >= 85 ? 'badge-critical' : 'badge-high'}">${item.threat_score}/100</span>
      </div>
      <div style="font-weight: 700; font-size: 0.88rem; margin-bottom: 0.35rem; color: #fff;" class="mono">${item.filename}</div>
      <div style="font-size: 0.75rem; color: var(--text-secondary); margin-bottom: 0.75rem; line-height: 1.4;">${item.summary || 'Evidence exhibit cataloged.'}</div>
      <div class="sha-pill mono">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        <span>SHA-256: ${hashShort}</span>
      </div>
    `;
    container.appendChild(card);
  });
}

// Render Timeline Feed
function renderTimeline(events) {
  const container = document.getElementById("timeline-feed");
  if (!container) return;
  container.innerHTML = "";

  const filtered = (activeFilter === "ALL") 
    ? events 
    : events.filter(e => (e.modality || '').toUpperCase() === activeFilter);

  if (filtered.length === 0) {
    container.innerHTML = `<div style="text-align: center; color: var(--text-muted); padding: 3rem;">No events found for modality: ${activeFilter}</div>`;
    return;
  }

  filtered.forEach(ev => {
    const item = document.createElement("div");
    item.className = "timeline-item";

    let modBadgeClass = "badge-modality";
    const mod = (ev.modality || '').toUpperCase();
    if (mod === "VIDEO") modBadgeClass = "badge-modality";
    else if (mod === "AUDIO") modBadgeClass = "badge-high";
    else if (mod === "IMAGE") modBadgeClass = "badge-verified";
    else if (mod === "FUSION") modBadgeClass = "badge-purple";

    item.innerHTML = `
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem; flex-wrap: wrap; gap: 0.5rem;">
        <div style="display: flex; align-items: center; gap: 0.5rem;">
          <span class="mono" style="font-size: 0.8rem; font-weight: 700; color: var(--accent-cyan);">${ev.timestamp}</span>
          <span class="badge ${modBadgeClass}">${mod}</span>
        </div>
        <span class="badge ${ev.threat_rating === 'CRITICAL' ? 'badge-critical' : 'badge-high'}">${ev.threat_rating}</span>
      </div>
      <div style="font-size: 0.95rem; font-weight: 700; color: #fff; margin-bottom: 0.35rem;">${ev.title}</div>
      <div style="font-size: 0.82rem; color: var(--text-secondary); line-height: 1.5; margin-bottom: 0.6rem;">${ev.description}</div>
      <div style="font-size: 0.72rem; color: #d8b4fe; background: rgba(88, 28, 135, 0.2); border: 1px solid rgba(168, 85, 247, 0.25); padding: 0.25rem 0.6rem; border-radius: 4px; display: inline-block;">
        Cross-Modal Corroboration: ${ev.correlation || 'Independent Modality Verification'}
      </div>
    `;
    container.appendChild(item);
  });
}

// Multimodal Fusion Trigger
async function triggerMultimodalFusion() {
  showToast("Running Multimodal Timeline Fusion...");
  try {
    const formData = new FormData();
    formData.append("case_id", CASE_ID);
    const res = await fetch("/api/fuse", { method: "POST", body: formData });
    if (!res.ok) throw new Error("Fusion request failed");
    const data = await res.json();
    showToast(`Timeline Fused: ${data.classification?.primary_crime || 'Armed Robbery'} (${data.composite_threat_score}/100)`);
    await loadCaseDossier();
  } catch (err) {
    showToast(`Fusion error: ${err.message}`, true);
  }
}

// Seed Full Demo Case
async function seedDemoCase(notify = true) {
  if (notify) showToast("Seeding complete multimodal case dossier...");
  try {
    const res = await fetch(`/api/demo/seed?case_id=${CASE_ID}`, { method: "POST" });
    if (!res.ok) throw new Error("Seed failed");
    const data = await res.json();
    if (notify) showToast(`Demo Case Loaded: ${data.classification} (${data.threat_score}/100)`);
    await loadCaseDossier();
  } catch (err) {
    if (notify) showToast(`Failed to load demo: ${err.message}`, true);
  }
}

// PDF Export Trigger
async function triggerPdfExport() {
  showToast("Compiling official court-admissible forensic PDF...");
  try {
    // Open direct PDF stream in new tab / download
    window.open(`/api/pdf/${CASE_ID}`, "_blank");
    showToast("PDF report generated successfully!");
  } catch (err) {
    showToast(`PDF generation error: ${err.message}`, true);
  }
}

// Copy Affidavit Draft to Clipboard
function copyAffidavit() {
  const text = document.getElementById("case-affidavit")?.textContent || "";
  navigator.clipboard.writeText(text).then(() => {
    showToast("Sworn Probable Cause Affidavit copied to clipboard!");
  }).catch(() => {
    showToast("Failed to copy affidavit", true);
  });
}

// AI Copilot Chat
function initChat() {
  const input = document.getElementById("chat-input");
  const sendBtn = document.getElementById("chat-send-btn");

  if (sendBtn && input) {
    sendBtn.addEventListener("click", () => sendChat());
    input.addEventListener("keydown", (e) => {
      if (e.key === "Enter") sendChat();
    });
  }
}

function sendQuickPrompt(promptText) {
  const input = document.getElementById("chat-input");
  if (input) {
    input.value = promptText;
    sendChat();
  }
}

async function sendChat() {
  const input = document.getElementById("chat-input");
  const msgContainer = document.getElementById("chat-messages");
  if (!input || !msgContainer) return;

  const query = input.value.trim();
  if (!query) return;

  // Add User Message
  appendChatBubble(query, "user");
  input.value = "";

  // Add Loading Bubble
  const botBubble = appendChatBubble("Analyzing multimodal forensic dossier...", "bot");

  try {
    const res = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ case_id: CASE_ID, query: query })
    });
    if (!res.ok) throw new Error("Chat request failed");
    const data = await res.json();

    let formattedText = data.response || "No intelligence analysis returned.";
    if (data.citations && data.citations.length > 0) {
      formattedText += `<br><br><span style="font-size:0.75rem; color:var(--accent-cyan); font-weight:700;">CITATIONS:</span><br>` +
        data.citations.map(c => `<span style="font-size:0.72rem; color:var(--text-muted); display:block;">• ${c}</span>`).join("");
    }
    botBubble.innerHTML = formattedText;
  } catch (err) {
    botBubble.innerHTML = `<span style="color:var(--accent-red)">Error querying forensic copilot: ${err.message}</span>`;
  }
  msgContainer.scrollTop = msgContainer.scrollHeight;
}

function appendChatBubble(text, sender) {
  const msgContainer = document.getElementById("chat-messages");
  const bubble = document.createElement("div");
  bubble.className = `chat-bubble chat-bubble-${sender}`;
  bubble.innerHTML = text;
  msgContainer.appendChild(bubble);
  msgContainer.scrollTop = msgContainer.scrollHeight;
  return bubble;
}

// Intake Studio: Analyze Image
async function analyzeImage(sampleName = null, file = null) {
  showToast("Analyzing optical evidence...");
  const formData = new FormData();
  formData.append("case_id", CASE_ID);
  if (file) formData.append("file", file);
  if (sampleName) formData.append("sample_name", sampleName);

  try {
    const res = await fetch("/api/image", { method: "POST", body: formData });
    if (!res.ok) throw new Error("Image analysis failed");
    const data = await res.json();
    renderImageResults(data);
    showToast(`Image Analyzed: Threat ${data.threat_score}/100`);
    await loadCaseDossier();
  } catch (err) {
    showToast(`Image analysis error: ${err.message}`, true);
  }
}

function renderImageResults(data) {
  const container = document.getElementById("image-results");
  if (!container) return;
  container.style.display = "block";

  const weapons = (data.weapons_detected || []).map(w => 
    `<span class="badge badge-critical" style="margin-right: 0.35rem;">${w.weapon_type} (${w.lethality_rating})</span>`
  ).join("") || "<span style='color:var(--text-muted); font-size:0.75rem;'>No lethal implements identified.</span>";

  const persons = (data.persons || []).map(p =>
    `<div style="font-size:0.75rem; color:var(--text-secondary); margin-bottom:0.25rem;">• <strong>${p.label}</strong> [${p.role_estimate}]: ${p.actions} (${p.clothing})</div>`
  ).join("") || "<span style='color:var(--text-muted); font-size:0.75rem;'>No human subjects cataloged.</span>";

  container.innerHTML = `
    <div class="forensic-card" style="margin-top: 1rem; border-color: rgba(56, 189, 248, 0.4);">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 0.75rem;">
        <span class="badge badge-modality">IMAGE ANALYSIS REPORT</span>
        <span class="badge ${data.threat_score >= 85 ? 'badge-critical' : 'badge-high'}">Threat: ${data.threat_score}/100 (${data.threat_level})</span>
      </div>
      <div style="font-size:0.85rem; color:#fff; margin-bottom:0.75rem;">${data.scene_description}</div>
      <div style="margin-bottom:0.5rem;"><strong style="font-size:0.75rem; color:var(--text-muted); text-transform:uppercase;">Weapons Detected:</strong><br>${weapons}</div>
      <div style="margin-bottom:0.5rem;"><strong style="font-size:0.75rem; color:var(--text-muted); text-transform:uppercase;">Persons Identified:</strong><br>${persons}</div>
      <div class="sha-pill mono" style="margin-top:0.5rem;">SHA-256: ${data.sha256_hash}</div>
    </div>
  `;
}

// Intake Studio: Analyze Audio
async function analyzeAudio(sampleName = null, file = null) {
  showToast("Processing acoustic evidence & diarization...");
  const formData = new FormData();
  formData.append("case_id", CASE_ID);
  if (file) formData.append("file", file);
  if (sampleName) formData.append("sample_name", sampleName);

  try {
    const res = await fetch("/api/audio", { method: "POST", body: formData });
    if (!res.ok) throw new Error("Audio analysis failed");
    const data = await res.json();
    renderAudioResults(data);
    showToast(`Audio Analyzed: ${data.speakers_identified} speakers diarized`);
    await loadCaseDossier();
  } catch (err) {
    showToast(`Audio analysis error: ${err.message}`, true);
  }
}

function renderAudioResults(data) {
  const container = document.getElementById("audio-results");
  if (!container) return;
  container.style.display = "block";

  const diarization = (data.speaker_diarization || []).map(seg => `
    <div style="padding:0.4rem 0.6rem; margin-bottom:0.35rem; background:rgba(15,23,42,0.8); border-radius:6px; font-size:0.75rem;">
      <span class="mono" style="color:var(--accent-cyan); font-weight:700;">[${seg.start_time} - ${seg.end_time}] ${seg.speaker}:</span>
      <span style="color:#fff;"> "${seg.text}"</span>
      <span class="badge ${seg.acoustic_stress === 'Panic' ? 'badge-critical' : 'badge-high'}" style="font-size:0.65rem; padding:0.15rem 0.4rem; margin-left:0.5rem;">${seg.acoustic_stress}</span>
    </div>
  `).join("");

  container.innerHTML = `
    <div class="forensic-card" style="margin-top: 1rem; border-color: rgba(245, 158, 11, 0.4);">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 0.75rem;">
        <span class="badge badge-high">ACOUSTIC DIARIZATION REPORT</span>
        <span class="badge ${data.audio_threat_score >= 85 ? 'badge-critical' : 'badge-high'}">Threat: ${data.audio_threat_score}/100</span>
      </div>
      <div style="margin-bottom:0.75rem;">${diarization}</div>
      <div class="sha-pill mono">SHA-256: ${data.sha256_hash}</div>
    </div>
  `;
}

// Intake Studio: Analyze Video
async function analyzeVideo(sampleName = null, file = null) {
  showToast("Parsing surveillance video & keyframes...");
  const formData = new FormData();
  formData.append("case_id", CASE_ID);
  if (file) formData.append("file", file);
  if (sampleName) formData.append("sample_name", sampleName);

  try {
    const res = await fetch("/api/video", { method: "POST", body: formData });
    if (!res.ok) throw new Error("Video analysis failed");
    const data = await res.json();
    renderVideoResults(data);
    showToast(`Video Analyzed: ${(data.temporal_events || []).length} keyframes extracted`);
    await loadCaseDossier();
  } catch (err) {
    showToast(`Video analysis error: ${err.message}`, true);
  }
}

function renderVideoResults(data) {
  const container = document.getElementById("video-results");
  if (!container) return;
  container.style.display = "block";

  const keyframes = (data.temporal_events || []).map(kf => `
    <div style="padding:0.4rem 0.6rem; margin-bottom:0.35rem; background:rgba(15,23,42,0.8); border-radius:6px; font-size:0.75rem;">
      <span class="mono" style="color:var(--accent-cyan); font-weight:700;">[${kf.timestamp}]</span>
      <strong style="color:#fff;"> ${kf.action_summary}</strong>
      <span style="color:var(--text-secondary); display:block; font-size:0.72rem; margin-top:0.2rem;">${kf.forensic_detail}</span>
    </div>
  `).join("");

  container.innerHTML = `
    <div class="forensic-card" style="margin-top: 1rem; border-color: rgba(56, 189, 248, 0.4);">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 0.75rem;">
        <span class="badge badge-modality">CCTV TELEMETRY REPORT</span>
        <span class="badge ${data.video_threat_score >= 85 ? 'badge-critical' : 'badge-high'}">Threat: ${data.video_threat_score}/100</span>
      </div>
      <div style="font-size:0.85rem; color:#fff; margin-bottom:0.75rem;">${data.summary}</div>
      <div style="margin-bottom:0.75rem;">${keyframes}</div>
      <div class="sha-pill mono">SHA-256: ${data.sha256_hash}</div>
    </div>
  `;
}
"""

STANDALONE_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CrimeVision AI – Multimodal Forensic Analysis Platform</title>
  <style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

:root {
  --bg-dark: #070a13;
  --bg-panel: rgba(15, 23, 42, 0.85);
  --bg-card: rgba(17, 24, 39, 0.7);
  --border-subtle: rgba(56, 189, 248, 0.15);
  --border-focus: rgba(56, 189, 248, 0.45);
  --accent-cyan: #38bdf8;
  --accent-blue: #0284c7;
  --accent-red: #ef4444;
  --accent-amber: #f59e0b;
  --accent-emerald: #10b981;
  --accent-purple: #a855f7;
  --text-primary: #f8fafc;
  --text-secondary: #94a3b8;
  --text-muted: #64748b;
  --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  background-color: var(--bg-dark);
  color: var(--text-primary);
  font-family: var(--font-sans);
  min-height: 100vh;
  overflow-x: hidden;
  background-image:
    radial-gradient(ellipse 80% 50% at 50% -20%, rgba(14, 165, 233, 0.15), transparent),
    radial-gradient(circle at 100% 100%, rgba(168, 85, 247, 0.06), transparent 30%);
}

.mono {
  font-family: var(--font-mono);
}

/* Custom Scrollbar */
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}
::-webkit-scrollbar-track {
  background: rgba(15, 23, 42, 0.6);
}
::-webkit-scrollbar-thumb {
  background: rgba(56, 189, 248, 0.25);
  border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover {
  background: rgba(56, 189, 248, 0.5);
}

/* Header Bar */
.forensic-header {
  position: sticky;
  top: 0;
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.85rem 2rem;
  background: rgba(10, 15, 30, 0.94);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--border-subtle);
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.5);
}

.brand-section {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.brand-icon {
  width: 42px;
  height: 42px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(14, 165, 233, 0.12);
  border: 1px solid rgba(56, 189, 248, 0.4);
  box-shadow: 0 0 16px rgba(56, 189, 248, 0.2);
  color: var(--accent-cyan);
}

.brand-text h1 {
  font-size: 1.15rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  display: flex;
  align-items: center;
  gap: 0.6rem;
}

.brand-text p {
  font-size: 0.72rem;
  color: var(--text-secondary);
}

.header-status-group {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.status-pill {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.35rem 0.85rem;
  border-radius: 9999px;
  background: rgba(15, 23, 42, 0.9);
  border: 1px solid rgba(51, 65, 85, 0.8);
  font-size: 0.75rem;
  font-weight: 700;
}

.pulse-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background-color: var(--accent-red);
  box-shadow: 0 0 8px var(--accent-red);
  animation: pulse-ring 1.8s infinite;
}

@keyframes pulse-ring {
  0% { transform: scale(0.95); opacity: 0.8; }
  50% { transform: scale(1.25); opacity: 1; box-shadow: 0 0 12px var(--accent-red); }
  100% { transform: scale(0.95); opacity: 0.8; }
}

.ai-engine-chip {
  display: flex;
  align-items: center;
  gap: 0.45rem;
  padding: 0.35rem 0.85rem;
  border-radius: 8px;
  background: rgba(88, 28, 135, 0.25);
  border: 1px solid rgba(168, 85, 247, 0.35);
  color: #d8b4fe;
  font-size: 0.75rem;
  font-weight: 600;
}

.btn-tactical {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.45rem 1rem;
  border-radius: 8px;
  font-size: 0.8rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s ease;
  border: 1px solid var(--accent-cyan);
  background: rgba(14, 165, 233, 0.12);
  color: var(--accent-cyan);
}
.btn-tactical:hover {
  background: rgba(14, 165, 233, 0.25);
  box-shadow: 0 0 14px rgba(56, 189, 248, 0.3);
  transform: translateY(-1px);
}

.btn-primary {
  background: linear-gradient(135deg, #0284c7, #0369a1);
  border: 1px solid rgba(56, 189, 248, 0.5);
  color: #fff;
}
.btn-primary:hover {
  background: linear-gradient(135deg, #0369a1, #075985);
  box-shadow: 0 0 18px rgba(56, 189, 248, 0.4);
}

.btn-danger {
  background: rgba(239, 68, 68, 0.15);
  border: 1px solid rgba(239, 68, 68, 0.5);
  color: #fca5a5;
}
.btn-danger:hover {
  background: rgba(239, 68, 68, 0.3);
  box-shadow: 0 0 14px rgba(239, 68, 68, 0.3);
}

/* Navigation Tabs */
.tabs-container {
  max-width: 1380px;
  margin: 1.5rem auto 0;
  padding: 0 1.5rem;
}

.nav-tabs {
  display: flex;
  gap: 0.5rem;
  border-bottom: 1px solid rgba(51, 65, 85, 0.8);
  background: rgba(15, 23, 42, 0.6);
  padding: 0.4rem 0.6rem 0;
  border-radius: 12px 12px 0 0;
  overflow-x: auto;
}

.tab-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.25rem;
  background: transparent;
  border: none;
  border-bottom: 2px solid transparent;
  color: var(--text-secondary);
  font-family: var(--font-sans);
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.2s ease;
}

.tab-btn:hover {
  color: var(--accent-cyan);
  background: rgba(56, 189, 248, 0.05);
  border-radius: 6px 6px 0 0;
}

.tab-btn.active {
  color: var(--accent-cyan);
  border-bottom-color: var(--accent-cyan);
  background: rgba(56, 189, 248, 0.1);
  border-radius: 6px 6px 0 0;
}

/* Main Content Area */
.main-content {
  max-width: 1380px;
  margin: 0 auto;
  padding: 1.5rem 1.5rem 4rem;
}

.tab-panel {
  display: none;
  animation: fadeIn 0.25s ease-in-out;
}
.tab-panel.active {
  display: block;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Forensic Cards */
.forensic-card {
  background: var(--bg-card);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid var(--border-subtle);
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}
.forensic-card:hover {
  border-color: var(--border-focus);
  box-shadow: 0 12px 40px rgba(56, 189, 248, 0.08);
}

/* Dossier Banner */
.dossier-banner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1.25rem;
  margin-bottom: 1.5rem;
  border-left: 4px solid var(--accent-cyan);
}

.dossier-title-row {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 0.4rem;
}

.dossier-title {
  font-size: 1.35rem;
  font-weight: 800;
  letter-spacing: 0.02em;
}

.dossier-meta {
  font-size: 0.78rem;
  color: var(--text-secondary);
}

/* KPI Grid */
.kpi-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.25rem;
  margin-bottom: 1.5rem;
}

.kpi-card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 120px;
}

.kpi-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 0.5rem;
}

.kpi-label {
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-muted);
}

.kpi-value {
  font-size: 1.55rem;
  font-weight: 800;
  color: #fff;
  letter-spacing: -0.02em;
}

.kpi-subtitle {
  font-size: 0.75rem;
  color: var(--text-secondary);
  margin-top: 0.25rem;
}

/* Two Column Layout */
.grid-2col {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 1.5rem;
  margin-bottom: 1.5rem;
}
@media (max-width: 980px) {
  .grid-2col {
    grid-template-columns: 1fr;
  }
}

/* Badges */
.badge {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.25rem 0.65rem;
  border-radius: 6px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

.badge-critical {
  background: rgba(239, 68, 68, 0.15);
  color: #f87171;
  border: 1px solid rgba(239, 68, 68, 0.4);
}
.badge-high {
  background: rgba(245, 158, 11, 0.15);
  color: #fbbf24;
  border: 1px solid rgba(245, 158, 11, 0.4);
}
.badge-verified {
  background: rgba(16, 185, 129, 0.15);
  color: #34d399;
  border: 1px solid rgba(16, 185, 129, 0.4);
}
.badge-modality {
  background: rgba(56, 189, 248, 0.15);
  color: var(--accent-cyan);
  border: 1px solid rgba(56, 189, 248, 0.35);
}
.badge-purple {
  background: rgba(168, 85, 247, 0.15);
  color: #c084fc;
  border: 1px solid rgba(168, 85, 247, 0.35);
}

.sha-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.25rem 0.65rem;
  border-radius: 6px;
  background: rgba(15, 23, 42, 0.95);
  border: 1px solid rgba(16, 185, 129, 0.3);
  font-size: 0.72rem;
  color: #6ee7b7;
}

/* Evidence Studio Subtabs */
.studio-tabs {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1.25rem;
}

.studio-tab-btn {
  padding: 0.5rem 1.25rem;
  border-radius: 8px;
  background: rgba(15, 23, 42, 0.7);
  border: 1px solid rgba(51, 65, 85, 0.6);
  color: var(--text-secondary);
  font-size: 0.82rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s ease;
}
.studio-tab-btn.active {
  background: rgba(56, 189, 248, 0.15);
  border-color: var(--accent-cyan);
  color: var(--accent-cyan);
}

/* Upload Dropzone */
.dropzone {
  border: 2px dashed rgba(56, 189, 248, 0.3);
  border-radius: 12px;
  padding: 2.5rem 1.5rem;
  text-align: center;
  background: rgba(15, 23, 42, 0.5);
  cursor: pointer;
  transition: all 0.2s ease;
}
.dropzone:hover {
  border-color: var(--accent-cyan);
  background: rgba(56, 189, 248, 0.05);
}

/* Timeline */
.timeline-filters {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
  flex-wrap: wrap;
}

.filter-btn {
  padding: 0.4rem 1rem;
  border-radius: 6px;
  background: rgba(15, 23, 42, 0.8);
  border: 1px solid rgba(51, 65, 85, 0.8);
  color: var(--text-secondary);
  font-size: 0.75rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.15s ease;
}
.filter-btn.active {
  background: rgba(56, 189, 248, 0.2);
  border-color: var(--accent-cyan);
  color: var(--accent-cyan);
}

.timeline-feed {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.timeline-item {
  border-left: 3px solid var(--accent-cyan);
  padding: 1.25rem;
  background: rgba(15, 23, 42, 0.75);
  border-radius: 0 10px 10px 0;
  border-top: 1px solid var(--border-subtle);
  border-right: 1px solid var(--border-subtle);
  border-bottom: 1px solid var(--border-subtle);
  transition: all 0.2s ease;
}
.timeline-item:hover {
  border-left-width: 5px;
  background: rgba(15, 23, 42, 0.95);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

/* Chat Copilot */
.chat-container {
  display: flex;
  flex-direction: column;
  height: 600px;
}

.chat-messages {
  flex: 1;
  overflow-y: auto;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.chat-bubble {
  max-width: 80%;
  padding: 0.85rem 1.15rem;
  border-radius: 12px;
  font-size: 0.85rem;
  line-height: 1.5;
}
.chat-bubble-user {
  align-self: flex-end;
  background: rgba(14, 165, 233, 0.2);
  border: 1px solid rgba(56, 189, 248, 0.4);
  color: #f0f9ff;
}
.chat-bubble-bot {
  align-self: flex-start;
  background: rgba(30, 41, 59, 0.85);
  border: 1px solid rgba(51, 65, 85, 0.8);
  color: #e2e8f0;
}

.chat-input-row {
  display: flex;
  gap: 0.75rem;
  padding: 1rem 0 0;
  border-top: 1px solid rgba(51, 65, 85, 0.6);
}

.chat-input {
  flex: 1;
  padding: 0.75rem 1rem;
  border-radius: 8px;
  background: rgba(15, 23, 42, 0.9);
  border: 1px solid rgba(51, 65, 85, 0.8);
  color: #fff;
  font-family: var(--font-sans);
  font-size: 0.85rem;
  outline: none;
}
.chat-input:focus {
  border-color: var(--accent-cyan);
  box-shadow: 0 0 10px rgba(56, 189, 248, 0.25);
}

.quick-prompts {
  display: flex;
  gap: 0.5rem;
  overflow-x: auto;
  padding-bottom: 0.5rem;
}

.quick-prompt-btn {
  padding: 0.35rem 0.75rem;
  border-radius: 6px;
  background: rgba(88, 28, 135, 0.2);
  border: 1px solid rgba(168, 85, 247, 0.35);
  color: #d8b4fe;
  font-size: 0.72rem;
  cursor: pointer;
  white-space: nowrap;
}
.quick-prompt-btn:hover {
  background: rgba(88, 28, 135, 0.4);
}

/* Toast Notifications */
#toast {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  padding: 0.85rem 1.5rem;
  border-radius: 8px;
  background: rgba(15, 23, 42, 0.95);
  border: 1px solid var(--accent-cyan);
  box-shadow: 0 10px 30px rgba(0,0,0,0.6);
  color: #fff;
  font-size: 0.85rem;
  font-weight: 600;
  z-index: 1000;
  opacity: 0;
  transform: translateY(20px);
  transition: all 0.3s ease;
  pointer-events: none;
}
#toast.show {
  opacity: 1;
  transform: translateY(0);
}

</style>
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🛡️</text></svg>">
</head>
<body>

  <!-- Top Tactical Header Bar -->
  <header class="forensic-header">
    <div class="brand-section">
      <div class="brand-icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="10"></circle>
          <path d="M12 2a10 10 0 0 1 10 10"></path>
          <path d="m4.93 4.93 4.24 4.24"></path>
          <circle cx="12" cy="12" r="2"></circle>
        </svg>
      </div>
      <div class="brand-text">
        <h1>
          CRIMEVISION AI
          <span class="badge badge-modality" style="font-size: 0.65rem;">ENTERPRISE FORENSICS</span>
        </h1>
        <p>Multimodal Forensic Intelligence, Timeline Fusion & Probable Cause Engine</p>
      </div>
    </div>

    <div class="header-status-group">
      <div class="status-pill">
        <div class="pulse-dot"></div>
        <span style="color: #fca5a5; font-size: 0.72rem; letter-spacing: 0.05em;">LIVE EVIDENCE STREAM</span>
      </div>

      <div style="text-align: right;">
        <div class="mono" style="font-size: 0.78rem; font-weight: 700; color: var(--accent-cyan);">CASE: CRV-2026-8841</div>
        <div style="font-size: 0.7rem; color: var(--text-secondary);">Det. Marcus Vance • MPD-7492</div>
      </div>

      <div class="ai-engine-chip">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>
        </svg>
        <span>Claude 3.5 Sonnet</span>
      </div>

      <button class="btn-tactical" onclick="seedDemoCase()">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M12 3v18M3 12h18"></path>
        </svg>
        Load Full Demo Case
      </button>
    </div>
  </header>

  <!-- Navigation Tabs -->
  <div class="tabs-container">
    <nav class="nav-tabs">
      <button class="tab-btn active" data-tab="overview">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="7" height="9" x="3" y="3" rx="1"/><rect width="7" height="5" x="14" y="3" rx="1"/><rect width="7" height="9" x="14" y="12" rx="1"/><rect width="7" height="5" x="3" y="16" rx="1"/></svg>
        Case Overview & Summary
      </button>
      <button class="tab-btn" data-tab="intake">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" x2="12" y1="3" y2="15"/></svg>
        Evidence Intake & Studio
      </button>
      <button class="tab-btn" data-tab="timeline">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
        Chronological Timeline
      </button>
      <button class="tab-btn" data-tab="chat">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
        AI Forensic Copilot
      </button>
      <button class="tab-btn" data-tab="export">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" x2="8" y1="13" y2="13"/><line x1="16" x2="8" y1="17" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
        PDF Court Dossier
      </button>
    </nav>
  </div>

  <!-- Main Content Viewport -->
  <main class="main-content">

    <!-- ========================================== -->
    <!-- TAB 1: CASE OVERVIEW & EXECUTIVE SUMMARY  -->
    <!-- ========================================== -->
    <section id="tab-overview" class="tab-panel active">
      <!-- Dossier Banner Card -->
      <div class="forensic-card dossier-banner">
        <div>
          <div class="dossier-title-row">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--accent-cyan)" stroke-width="2"><path d="M4 20h16a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.93a2 2 0 0 1-1.66-.9l-.82-1.2A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13c0 1.1.9 2 2 2Z"/></svg>
            <span id="case-title" class="dossier-title">Armed Commercial Robbery - Central Metro Express</span>
            <span id="case-threat-badge" class="badge badge-critical">CRITICAL • 94/100</span>
          </div>
          <div id="case-meta" class="dossier-meta mono">INCIDENT: 2026-10-24 22:45:00 | LOCATION: Sector 4B, 1422 North Meridian Ave | JURISDICTION: Metro Police Forensic Investigation Unit</div>
        </div>
        <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
          <button class="btn-tactical btn-primary" onclick="triggerMultimodalFusion()">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"/></svg>
            Run Multimodal Fusion
          </button>
          <button class="btn-tactical btn-danger" onclick="triggerPdfExport()">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" x2="12" y1="15" y2="3"/></svg>
            Generate PDF Dossier
          </button>
        </div>
      </div>

      <!-- 4 Forensic KPI Cards -->
      <div class="kpi-grid">
        <div class="forensic-card kpi-card">
          <div class="kpi-header">
            <span class="kpi-label">Evidence Exhibits</span>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--accent-cyan)" stroke-width="2"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"/></svg>
          </div>
          <div>
            <div id="kpi-exhibits" class="kpi-value mono">3 Logged</div>
            <div class="kpi-subtitle">Optical, Acoustic & Video Feeds</div>
          </div>
        </div>

        <div class="forensic-card kpi-card">
          <div class="kpi-header">
            <span class="kpi-label">Crime Classification</span>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--accent-amber)" stroke-width="2"><path d="m14 13-7.5 7.5a2.12 2.12 0 0 1-3-3L11 10"/><path d="m16 16 6-6"/><path d="m8 8 6-6"/><path d="m9 7 8 8"/></svg>
          </div>
          <div>
            <div id="kpi-classification" class="kpi-value" style="font-size: 1.25rem;">Armed Robbery</div>
            <div id="kpi-penal" class="kpi-subtitle mono" style="color: var(--accent-amber);">Penal Code § 211</div>
          </div>
        </div>

        <div class="forensic-card kpi-card">
          <div class="kpi-header">
            <span class="kpi-label">Threat Matrix Level</span>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--accent-red)" stroke-width="2"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><line x1="12" x2="12" y1="9" y2="13"/><line x1="12" x2="12.01" y1="17" y2="17"/></svg>
          </div>
          <div>
            <div id="kpi-threat" class="kpi-value mono" style="color: var(--accent-red);">CRITICAL (94/100)</div>
            <div class="kpi-subtitle">Armed Coercion & Lethal Risk</div>
          </div>
        </div>

        <div class="forensic-card kpi-card">
          <div class="kpi-header">
            <span class="kpi-label">Chain of Custody</span>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--accent-emerald)" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          </div>
          <div>
            <div class="kpi-value mono" style="color: var(--accent-emerald);">100% VALIDATED</div>
            <div class="kpi-subtitle">Cryptographic SHA-256 Ledger</div>
          </div>
        </div>
      </div>

      <!-- Narrative & Probable Cause Split -->
      <div class="grid-2col">
        <div class="forensic-card">
          <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.75rem;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--accent-cyan)" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" x2="8" y1="13" y2="13"/><line x1="16" x2="8" y1="17" y2="17"/></svg>
            <h3 style="font-size: 1rem; font-weight: 700; color: #fff;">Executive Forensic Narrative</h3>
          </div>
          <p id="case-narrative" style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6; margin-bottom: 1.25rem;">
            Multi-subject aggravated commercial armed robbery at Central Metro Express. Evidence exhibits firearm brandishing, verbal threats to staff, safe breach, and rapid getaway in a dark sedan.
          </p>

          <div style="border-top: 1px solid rgba(51, 65, 85, 0.6); padding-top: 1rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
              <span style="font-size: 0.72rem; font-weight: 800; letter-spacing: 0.08em; color: var(--accent-cyan);">SWORN PROBABLE CAUSE AFFIDAVIT DRAFT:</span>
              <button class="btn-tactical" style="padding: 0.2rem 0.6rem; font-size: 0.7rem;" onclick="copyAffidavit()">Copy Affidavit</button>
            </div>
            <p id="case-affidavit" style="font-size: 0.8rem; color: var(--text-muted); font-style: italic; line-height: 1.6;">
              Forensic multimodal surveillance analysis confirms matching facial structure, dark clothing with reflective accents, recorded verbal demands for cashier safe codes, and video telemetry corroborating weapon presentation at 22:46:12.
            </p>
          </div>
        </div>

        <div class="forensic-card" style="display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <h3 style="font-size: 1rem; font-weight: 700; color: #fff; margin-bottom: 0.4rem;">Investigator Quick Actions</h3>
            <p style="font-size: 0.75rem; color: var(--text-secondary); margin-bottom: 1.25rem;">Direct triage shortcuts to evidence intake, copilot, and court filing export.</p>

            <div style="display: flex; flex-direction: column; gap: 0.75rem;">
              <button class="btn-tactical" style="width: 100%; justify-content: flex-start;" onclick="switchTab('intake')">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" x2="12" y1="3" y2="15"/></svg>
                Intake New Forensic Evidence
              </button>
              <button class="btn-tactical" style="width: 100%; justify-content: flex-start;" onclick="switchTab('timeline')">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                Inspect Synchronized Timeline
              </button>
              <button class="btn-tactical" style="width: 100%; justify-content: flex-start; border-color: var(--accent-purple); color: #d8b4fe;" onclick="switchTab('chat')">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
                Consult Forensic AI Copilot
              </button>
              <button class="btn-tactical btn-danger" style="width: 100%; justify-content: flex-start;" onclick="triggerPdfExport()">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" x2="12" y1="15" y2="3"/></svg>
                Download Official Court Dossier
              </button>
            </div>
          </div>

          <div style="padding-top: 1rem; border-top: 1px solid rgba(51, 65, 85, 0.6); margin-top: 1rem;">
            <div style="font-size: 0.72rem; color: var(--text-muted); text-align: center;">Vercel Serverless & Python ASGI Compliant</div>
          </div>
        </div>
      </div>

      <!-- Exhibits Grid Section -->
      <div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
          <h3 style="font-size: 1.1rem; font-weight: 800; color: #fff;">Active Evidence Repository</h3>
          <span style="font-size: 0.75rem; color: var(--text-secondary);">Cryptographically registered exhibits</span>
        </div>
        <div id="evidence-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.25rem;">
          <!-- Injected via JavaScript -->
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- TAB 2: EVIDENCE INTAKE & STUDIO           -->
    <!-- ========================================== -->
    <section id="tab-intake" class="tab-panel">
      <div class="studio-tabs">
        <button class="studio-tab-btn active" data-studio="image">Optical / Image Studio</button>
        <button class="studio-tab-btn" data-studio="audio">Acoustic / Audio Studio</button>
        <button class="studio-tab-btn" data-studio="video">Surveillance CCTV / Video Studio</button>
      </div>

      <!-- Studio Panel 1: Image -->
      <div id="studio-image" class="studio-panel">
        <div class="forensic-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
            <div>
              <h3 style="font-size: 1.1rem; font-weight: 800; color: #fff;">Image Forensic Studio</h3>
              <p style="font-size: 0.78rem; color: var(--text-secondary);">Weapon detection, person cataloging, facial orientation, and SHA-256 seal.</p>
            </div>
            <button class="btn-tactical" onclick="analyzeImage('sample_surveillance_cam02.jpg')">
              Load Pre-Bundled Surveillance Sample
            </button>
          </div>

          <div class="dropzone" onclick="document.getElementById('image-upload-input').click()">
            <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="var(--accent-cyan)" stroke-width="1.5" style="margin-bottom: 0.5rem;"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"/></svg>
            <div style="font-weight: 700; font-size: 0.95rem; color: #fff;">Click to upload forensic surveillance frame</div>
            <div style="font-size: 0.75rem; color: var(--text-secondary); margin-top: 0.25rem;">Supports JPEG, PNG, WEBP (Max 25MB)</div>
            <input type="file" id="image-upload-input" accept="image/*" style="display: none;" onchange="if(this.files[0]) analyzeImage(null, this.files[0])">
          </div>

          <div style="margin-top: 1.5rem; text-align: center;">
            <img src="/samples/sample_surveillance_cam02.jpg" alt="Surveillance Preview" style="max-height: 240px; border-radius: 8px; border: 1px solid var(--border-subtle); display: inline-block;">
            <div style="font-size: 0.7rem; color: var(--text-muted); margin-top: 0.4rem;" class="mono">PREVIEW: samples/sample_surveillance_cam02.jpg (Sector 4B Cam-02)</div>
          </div>

          <div id="image-results" style="display: none;"></div>
        </div>
      </div>

      <!-- Studio Panel 2: Audio -->
      <div id="studio-audio" class="studio-panel" style="display: none;">
        <div class="forensic-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
            <div>
              <h3 style="font-size: 1.1rem; font-weight: 800; color: #fff;">Acoustic Diarization Studio</h3>
              <p style="font-size: 0.78rem; color: var(--text-secondary);">Speaker separation, vocal panic stress, verbal threat extraction, and 911 dispatch sync.</p>
            </div>
            <button class="btn-tactical" onclick="analyzeAudio('dispatch_counter_mic01.wav')">
              Load Pre-Bundled Dispatch Audio Sample
            </button>
          </div>

          <div class="dropzone" onclick="document.getElementById('audio-upload-input').click()">
            <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="var(--accent-amber)" stroke-width="1.5" style="margin-bottom: 0.5rem;"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" x2="12" y1="19" y2="22"/></svg>
            <div style="font-weight: 700; font-size: 0.95rem; color: #fff;">Click to upload forensic audio recording</div>
            <div style="font-size: 0.75rem; color: var(--text-secondary); margin-top: 0.25rem;">Supports WAV, MP3, M4A, FLAC</div>
            <input type="file" id="audio-upload-input" accept="audio/*" style="display: none;" onchange="if(this.files[0]) analyzeAudio(null, this.files[0])">
          </div>

          <div style="margin-top: 1.5rem; text-align: center;">
            <audio controls style="width: 100%; max-width: 500px;">
              <source src="/samples/dispatch_counter_mic01.wav" type="audio/wav">
              Your browser does not support audio playback.
            </audio>
            <div style="font-size: 0.7rem; color: var(--text-muted); margin-top: 0.4rem;" class="mono">PREVIEW: samples/dispatch_counter_mic01.wav (Counter Mic 01)</div>
          </div>

          <div id="audio-results" style="display: none;"></div>
        </div>
      </div>

      <!-- Studio Panel 3: Video -->
      <div id="studio-video" class="studio-panel" style="display: none;">
        <div class="forensic-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
            <div>
              <h3 style="font-size: 1.1rem; font-weight: 800; color: #fff;">Surveillance CCTV Telemetry Studio</h3>
              <p style="font-size: 0.78rem; color: var(--text-secondary);">Keyframe decomposition, getaway corridor telemetry, vehicle tracking, and egress mapping.</p>
            </div>
            <button class="btn-tactical" onclick="analyzeVideo('cctv_exterior_getaway.mp4')">
              Load Pre-Bundled CCTV Video Sample
            </button>
          </div>

          <div class="dropzone" onclick="document.getElementById('video-upload-input').click()">
            <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="var(--accent-cyan)" stroke-width="1.5" style="margin-bottom: 0.5rem;"><polygon points="23 7 16 12 23 17 23 7"/><rect width="15" height="14" x="1" y="5" rx="2" ry="2"/></svg>
            <div style="font-weight: 700; font-size: 0.95rem; color: #fff;">Click to upload CCTV surveillance video</div>
            <div style="font-size: 0.75rem; color: var(--text-secondary); margin-top: 0.25rem;">Supports MP4, MOV, MKV, AVI (Max 50MB)</div>
            <input type="file" id="video-upload-input" accept="video/*" style="display: none;" onchange="if(this.files[0]) analyzeVideo(null, this.files[0])">
          </div>

          <div style="margin-top: 1.5rem; text-align: center;">
            <video controls style="max-height: 260px; border-radius: 8px; border: 1px solid var(--border-subtle); display: inline-block;">
              <source src="/samples/cctv_exterior_getaway.mp4" type="video/mp4">
              Your browser does not support video playback.
            </video>
            <div style="font-size: 0.7rem; color: var(--text-muted); margin-top: 0.4rem;" class="mono">PREVIEW: samples/cctv_exterior_getaway.mp4 (Exterior Egress Feed)</div>
          </div>

          <div id="video-results" style="display: none;"></div>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- TAB 3: CHRONOLOGICAL FORENSIC TIMELINE    -->
    <!-- ========================================== -->
    <section id="tab-timeline" class="tab-panel">
      <div class="forensic-card" style="margin-bottom: 1.5rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
          <div>
            <h3 style="font-size: 1.1rem; font-weight: 800; color: #fff;">Chronological Forensic Timeline</h3>
            <p style="font-size: 0.78rem; color: var(--text-secondary);">Cross-modal synchronization correlating visual events with acoustic spikes and telemetry.</p>
          </div>
          <div class="timeline-filters">
            <button class="filter-btn active" data-filter="ALL">ALL MODALITIES</button>
            <button class="filter-btn" data-filter="IMAGE">IMAGE ONLY</button>
            <button class="filter-btn" data-filter="AUDIO">AUDIO ONLY</button>
            <button class="filter-btn" data-filter="VIDEO">VIDEO ONLY</button>
            <button class="filter-btn" data-filter="FUSION">FUSION SYNTHESIS</button>
          </div>
        </div>

      <div id="timeline-feed" class="timeline-feed">
        <!-- Injected via JavaScript -->
      </div>
    </section>

    <!-- ========================================== -->
    <!-- TAB 4: FORENSIC COPILOT CHAT ASSISTANT    -->
    <!-- ========================================== -->
    <section id="tab-chat" class="tab-panel">
      <div class="forensic-card chat-container">
        <div style="display: flex; justify-content: space-between; align-items: center; padding-bottom: 0.85rem; border-bottom: 1px solid rgba(51, 65, 85, 0.6);">
          <div style="display: flex; align-items: center; gap: 0.5rem;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--accent-purple)" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
            <h3 style="font-size: 1rem; font-weight: 700; color: #fff;">Forensic Intelligence Copilot</h3>
            <span class="badge badge-purple" style="font-size: 0.65rem;">CLAUDE 3.5 ACTIVE</span>
          </div>
          <span style="font-size: 0.72rem; color: var(--text-muted);">Sworn Case Investigator Dialogue</span>
        </div>

        <div style="padding: 0.75rem 0 0;">
          <div class="quick-prompts">
            <button class="quick-prompt-btn" onclick="sendQuickPrompt('What weapons were detected across all evidence exhibits?')">What weapons were detected?</button>
            <button class="quick-prompt-btn" onclick="sendQuickPrompt('Summarize suspect getaway telemetry, vehicle color, and flight path.')">Summarize getaway vehicle & flight path</button>
            <button class="quick-prompt-btn" onclick="sendQuickPrompt('Draft probable cause justification for search and arrest warrants.')">Draft probable cause justification</button>
            <button class="quick-prompt-btn" onclick="sendQuickPrompt('Cross-reference cashier statements with surveillance video timestamps.')">Cross-reference statements with video</button>
          </div>
        </div>

        <div id="chat-messages" class="chat-messages">
          <div class="chat-bubble chat-bubble-bot">
            Welcome, Detective. I am your multimodal forensic intelligence co-pilot. I have indexed Case <strong>CRV-2026-8841</strong> (Armed Commercial Robbery at Central Metro Express). You may ask questions regarding suspect attire, weapon classifications, acoustic stress markers, vehicle telemetry, or probable cause affidavit drafting.
          </div>
        </div>

        <div class="chat-input-row">
          <input type="text" id="chat-input" class="chat-input" placeholder="Query forensic case evidence, ask about suspect attire, weapons, or escape telemetry...">
          <button id="chat-send-btn" class="btn-tactical btn-primary" style="padding: 0 1.25rem;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" x2="11" y1="2" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
            Send
          </button>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- TAB 5: OFFICIAL FORENSIC PDF DOSSIER      -->
    <!-- ========================================== -->
    <section id="tab-export" class="tab-panel">
      <div class="forensic-card" style="max-width: 800px; margin: 0 auto; text-align: center; padding: 3rem 2rem;">
        <div style="width: 64px; height: 64px; margin: 0 auto 1.25rem; border-radius: 50%; background: rgba(239, 68, 68, 0.15); border: 2px solid rgba(239, 68, 68, 0.4); display: flex; align-items: center; justify-content: center; color: var(--accent-red);">
          <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" x2="8" y1="13" y2="13"/><line x1="16" x2="8" y1="17" y2="17"/></svg>
        </div>

        <h2 style="font-size: 1.4rem; font-weight: 800; color: #fff; margin-bottom: 0.5rem;">Official Court-Admissible Multimodal Forensic Report</h2>
        <p style="font-size: 0.85rem; color: var(--text-secondary); max-width: 600px; margin: 0 auto 2rem; line-height: 1.6;">
          Generates a certified digital forensic case report using ReportLab with SHA-256 cryptographic hashes, weapon lethality indices, acoustic diarization transcripts, chronological event timeline, and sworn probable cause affidavit.
        </p>

        <div class="forensic-card" style="background: rgba(15, 23, 42, 0.95); margin-bottom: 2rem; text-align: left; padding: 1.25rem;">
          <div style="font-size: 0.75rem; font-weight: 700; color: var(--accent-cyan); text-transform: uppercase; margin-bottom: 0.5rem;">Dossier Specifications:</div>
          <div style="font-size: 0.8rem; color: var(--text-secondary); line-height: 1.6;">
            • Case Identifier: <strong>CRV-2026-8841</strong> (Central Metro Express)<br>
            • Primary Statutory Charge: <strong>Penal Code § 211 - Robbery with Deadly Weapon</strong><br>
            • Lead Forensic Examiner: <strong>Det. Marcus Vance (Badge MPD-7492)</strong><br>
            • Custody Security: <strong>SHA-256 Hash Verification on all optical, acoustic, and video exhibits</strong><br>
            • Document Format: <strong>High-Resolution Vector PDF (ReportLab Engine)</strong>
          </div>
        </div>

        <button class="btn-tactical btn-danger" style="padding: 0.85rem 2.5rem; font-size: 0.95rem;" onclick="triggerPdfExport()">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" x2="12" y1="15" y2="3"/></svg>
          Download Official Forensic PDF Report
        </button>
      </div>
    </section>

  </main>

  <!-- Notification Toast -->
  <div id="toast"></div>

  <!-- Client Application Controller -->
  <script>
// CrimeVision AI – Multimodal Forensic Analysis Platform
// Frontend Controller for Vercel Serverless & Static CDN Deployment

const CASE_ID = "CRV-2026-8841";
let activeFilter = "ALL";
let allTimelineEvents = [];

// Initialize Dashboard
document.addEventListener("DOMContentLoaded", () => {
  initTabs();
  initStudioTabs();
  initFilters();
  initChat();
  loadCaseDossier();
});

// Toast notification helper
function showToast(message, isError = false) {
  const toast = document.getElementById("toast");
  if (!toast) return;
  toast.textContent = message;
  toast.style.borderColor = isError ? "var(--accent-red)" : "var(--accent-cyan)";
  toast.classList.add("show");
  setTimeout(() => toast.classList.remove("show"), 3500);
}

// Tab Switching
function initTabs() {
  const tabBtns = document.querySelectorAll(".tab-btn");
  tabBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      const target = btn.getAttribute("data-tab");
      document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
      document.querySelectorAll(".tab-panel").forEach(p => p.classList.remove("active"));

      btn.classList.add("active");
      const panel = document.getElementById(`tab-${target}`);
      if (panel) panel.classList.add("active");
    });
  });
}

function switchTab(tabId) {
  const btn = document.querySelector(`.tab-btn[data-tab="${tabId}"]`);
  if (btn) btn.click();
}

// Studio Sub-Tabs
function initStudioTabs() {
  const studioBtns = document.querySelectorAll(".studio-tab-btn");
  studioBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      const target = btn.getAttribute("data-studio");
      studioBtns.forEach(b => b.classList.remove("active"));
      document.querySelectorAll(".studio-panel").forEach(p => p.style.display = "none");

      btn.classList.add("active");
      const activePanel = document.getElementById(`studio-${target}`);
      if (activePanel) activePanel.style.display = "block";
    });
  });
}

// Timeline Filters
function initFilters() {
  const filterBtns = document.querySelectorAll(".filter-btn");
  filterBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      filterBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      activeFilter = btn.getAttribute("data-filter");
      renderTimeline(allTimelineEvents);
    });
  });
}

// Fetch Case Dossier from Backend
async function loadCaseDossier() {
  try {
    const res = await fetch(`/api/cases/${CASE_ID}`);
    if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
    const data = await res.json();
    renderCaseData(data);
  } catch (err) {
    console.warn("Could not load case dossier, attempting demo seed...", err);
    await seedDemoCase(false);
  }
}

// Render Case Data into UI
function renderCaseData(data) {
  // Metadata & Dossier Banner
  const titleElem = document.getElementById("case-title");
  if (titleElem) titleElem.textContent = data.title || "Armed Commercial Robbery - Central Metro Express";

  const metaElem = document.getElementById("case-meta");
  if (metaElem) {
    metaElem.textContent = `INCIDENT: ${data.incident_date} | LOCATION: ${data.location} | JURISDICTION: ${data.jurisdiction}`;
  }

  const threatBadgeElem = document.getElementById("case-threat-badge");
  if (threatBadgeElem) {
    threatBadgeElem.textContent = `${data.threat_level || 'CRITICAL'} • ${data.overall_threat_score || 94}/100`;
    threatBadgeElem.className = `badge ${(data.overall_threat_score >= 85) ? 'badge-critical' : 'badge-high'}`;
  }

  // KPIs
  const kpiExhibits = document.getElementById("kpi-exhibits");
  if (kpiExhibits) kpiExhibits.textContent = `${(data.evidence_items || []).length} Logged`;

  const kpiClassification = document.getElementById("kpi-classification");
  if (kpiClassification) kpiClassification.textContent = data.classification || "Armed Robbery";

  const kpiPenal = document.getElementById("kpi-penal");
  if (kpiPenal) kpiPenal.textContent = data.penal_code || "Penal Code § 211";

  const kpiThreat = document.getElementById("kpi-threat");
  if (kpiThreat) kpiThreat.textContent = `${data.threat_level || 'CRITICAL'} (${data.overall_threat_score || 94}/100)`;

  // Narrative & Affidavit
  const narrativeElem = document.getElementById("case-narrative");
  if (narrativeElem) narrativeElem.textContent = data.summary || "Multimodal evidence analysis in progress.";

  const affidavitElem = document.getElementById("case-affidavit");
  if (affidavitElem) affidavitElem.textContent = data.probable_cause || "Sworn affidavit pending multimodal fusion.";

  // Evidence Exhibits List
  renderEvidenceGrid(data.evidence_items || []);

  // Timeline
  allTimelineEvents = data.timeline_events || [];
  renderTimeline(allTimelineEvents);
}

// Render Evidence Grid
function renderEvidenceGrid(items) {
  const container = document.getElementById("evidence-grid");
  if (!container) return;
  container.innerHTML = "";

  if (items.length === 0) {
    container.innerHTML = `<div style="grid-column: 1 / -1; text-align: center; color: var(--text-muted); padding: 2rem;">No evidence items registered yet. Use the Intake Studio or click 'Load Demo Case'.</div>`;
    return;
  }

  items.forEach(item => {
    const card = document.createElement("div");
    card.className = "forensic-card";
    card.style.padding = "1rem";

    const hashShort = item.sha256 ? `${item.sha256.substring(0, 10)}...${item.sha256.substring(item.sha256.length - 8)}` : "VERIFIED";

    card.innerHTML = `
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
        <span class="badge badge-modality">${(item.type || 'EVIDENCE').toUpperCase()}</span>
        <span class="badge ${item.threat_score >= 85 ? 'badge-critical' : 'badge-high'}">${item.threat_score}/100</span>
      </div>
      <div style="font-weight: 700; font-size: 0.88rem; margin-bottom: 0.35rem; color: #fff;" class="mono">${item.filename}</div>
      <div style="font-size: 0.75rem; color: var(--text-secondary); margin-bottom: 0.75rem; line-height: 1.4;">${item.summary || 'Evidence exhibit cataloged.'}</div>
      <div class="sha-pill mono">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        <span>SHA-256: ${hashShort}</span>
      </div>
    `;
    container.appendChild(card);
  });
}

// Render Timeline Feed
function renderTimeline(events) {
  const container = document.getElementById("timeline-feed");
  if (!container) return;
  container.innerHTML = "";

  const filtered = (activeFilter === "ALL") 
    ? events 
    : events.filter(e => (e.modality || '').toUpperCase() === activeFilter);

  if (filtered.length === 0) {
    container.innerHTML = `<div style="text-align: center; color: var(--text-muted); padding: 3rem;">No events found for modality: ${activeFilter}</div>`;
    return;
  }

  filtered.forEach(ev => {
    const item = document.createElement("div");
    item.className = "timeline-item";

    let modBadgeClass = "badge-modality";
    const mod = (ev.modality || '').toUpperCase();
    if (mod === "VIDEO") modBadgeClass = "badge-modality";
    else if (mod === "AUDIO") modBadgeClass = "badge-high";
    else if (mod === "IMAGE") modBadgeClass = "badge-verified";
    else if (mod === "FUSION") modBadgeClass = "badge-purple";

    item.innerHTML = `
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem; flex-wrap: wrap; gap: 0.5rem;">
        <div style="display: flex; align-items: center; gap: 0.5rem;">
          <span class="mono" style="font-size: 0.8rem; font-weight: 700; color: var(--accent-cyan);">${ev.timestamp}</span>
          <span class="badge ${modBadgeClass}">${mod}</span>
        </div>
        <span class="badge ${ev.threat_rating === 'CRITICAL' ? 'badge-critical' : 'badge-high'}">${ev.threat_rating}</span>
      </div>
      <div style="font-size: 0.95rem; font-weight: 700; color: #fff; margin-bottom: 0.35rem;">${ev.title}</div>
      <div style="font-size: 0.82rem; color: var(--text-secondary); line-height: 1.5; margin-bottom: 0.6rem;">${ev.description}</div>
      <div style="font-size: 0.72rem; color: #d8b4fe; background: rgba(88, 28, 135, 0.2); border: 1px solid rgba(168, 85, 247, 0.25); padding: 0.25rem 0.6rem; border-radius: 4px; display: inline-block;">
        Cross-Modal Corroboration: ${ev.correlation || 'Independent Modality Verification'}
      </div>
    `;
    container.appendChild(item);
  });
}

// Multimodal Fusion Trigger
async function triggerMultimodalFusion() {
  showToast("Running Multimodal Timeline Fusion...");
  try {
    const formData = new FormData();
    formData.append("case_id", CASE_ID);
    const res = await fetch("/api/fuse", { method: "POST", body: formData });
    if (!res.ok) throw new Error("Fusion request failed");
    const data = await res.json();
    showToast(`Timeline Fused: ${data.classification?.primary_crime || 'Armed Robbery'} (${data.composite_threat_score}/100)`);
    await loadCaseDossier();
  } catch (err) {
    showToast(`Fusion error: ${err.message}`, true);
  }
}

// Seed Full Demo Case
async function seedDemoCase(notify = true) {
  if (notify) showToast("Seeding complete multimodal case dossier...");
  try {
    const res = await fetch(`/api/demo/seed?case_id=${CASE_ID}`, { method: "POST" });
    if (!res.ok) throw new Error("Seed failed");
    const data = await res.json();
    if (notify) showToast(`Demo Case Loaded: ${data.classification} (${data.threat_score}/100)`);
    await loadCaseDossier();
  } catch (err) {
    if (notify) showToast(`Failed to load demo: ${err.message}`, true);
  }
}

// PDF Export Trigger
async function triggerPdfExport() {
  showToast("Compiling official court-admissible forensic PDF...");
  try {
    // Open direct PDF stream in new tab / download
    window.open(`/api/pdf/${CASE_ID}`, "_blank");
    showToast("PDF report generated successfully!");
  } catch (err) {
    showToast(`PDF generation error: ${err.message}`, true);
  }
}

// Copy Affidavit Draft to Clipboard
function copyAffidavit() {
  const text = document.getElementById("case-affidavit")?.textContent || "";
  navigator.clipboard.writeText(text).then(() => {
    showToast("Sworn Probable Cause Affidavit copied to clipboard!");
  }).catch(() => {
    showToast("Failed to copy affidavit", true);
  });
}

// AI Copilot Chat
function initChat() {
  const input = document.getElementById("chat-input");
  const sendBtn = document.getElementById("chat-send-btn");

  if (sendBtn && input) {
    sendBtn.addEventListener("click", () => sendChat());
    input.addEventListener("keydown", (e) => {
      if (e.key === "Enter") sendChat();
    });
  }
}

function sendQuickPrompt(promptText) {
  const input = document.getElementById("chat-input");
  if (input) {
    input.value = promptText;
    sendChat();
  }
}

async function sendChat() {
  const input = document.getElementById("chat-input");
  const msgContainer = document.getElementById("chat-messages");
  if (!input || !msgContainer) return;

  const query = input.value.trim();
  if (!query) return;

  // Add User Message
  appendChatBubble(query, "user");
  input.value = "";

  // Add Loading Bubble
  const botBubble = appendChatBubble("Analyzing multimodal forensic dossier...", "bot");

  try {
    const res = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ case_id: CASE_ID, query: query })
    });
    if (!res.ok) throw new Error("Chat request failed");
    const data = await res.json();

    let formattedText = data.response || "No intelligence analysis returned.";
    if (data.citations && data.citations.length > 0) {
      formattedText += `<br><br><span style="font-size:0.75rem; color:var(--accent-cyan); font-weight:700;">CITATIONS:</span><br>` +
        data.citations.map(c => `<span style="font-size:0.72rem; color:var(--text-muted); display:block;">• ${c}</span>`).join("");
    }
    botBubble.innerHTML = formattedText;
  } catch (err) {
    botBubble.innerHTML = `<span style="color:var(--accent-red)">Error querying forensic copilot: ${err.message}</span>`;
  }
  msgContainer.scrollTop = msgContainer.scrollHeight;
}

function appendChatBubble(text, sender) {
  const msgContainer = document.getElementById("chat-messages");
  const bubble = document.createElement("div");
  bubble.className = `chat-bubble chat-bubble-${sender}`;
  bubble.innerHTML = text;
  msgContainer.appendChild(bubble);
  msgContainer.scrollTop = msgContainer.scrollHeight;
  return bubble;
}

// Intake Studio: Analyze Image
async function analyzeImage(sampleName = null, file = null) {
  showToast("Analyzing optical evidence...");
  const formData = new FormData();
  formData.append("case_id", CASE_ID);
  if (file) formData.append("file", file);
  if (sampleName) formData.append("sample_name", sampleName);

  try {
    const res = await fetch("/api/image", { method: "POST", body: formData });
    if (!res.ok) throw new Error("Image analysis failed");
    const data = await res.json();
    renderImageResults(data);
    showToast(`Image Analyzed: Threat ${data.threat_score}/100`);
    await loadCaseDossier();
  } catch (err) {
    showToast(`Image analysis error: ${err.message}`, true);
  }
}

function renderImageResults(data) {
  const container = document.getElementById("image-results");
  if (!container) return;
  container.style.display = "block";

  const weapons = (data.weapons_detected || []).map(w => 
    `<span class="badge badge-critical" style="margin-right: 0.35rem;">${w.weapon_type} (${w.lethality_rating})</span>`
  ).join("") || "<span style='color:var(--text-muted); font-size:0.75rem;'>No lethal implements identified.</span>";

  const persons = (data.persons || []).map(p =>
    `<div style="font-size:0.75rem; color:var(--text-secondary); margin-bottom:0.25rem;">• <strong>${p.label}</strong> [${p.role_estimate}]: ${p.actions} (${p.clothing})</div>`
  ).join("") || "<span style='color:var(--text-muted); font-size:0.75rem;'>No human subjects cataloged.</span>";

  container.innerHTML = `
    <div class="forensic-card" style="margin-top: 1rem; border-color: rgba(56, 189, 248, 0.4);">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 0.75rem;">
        <span class="badge badge-modality">IMAGE ANALYSIS REPORT</span>
        <span class="badge ${data.threat_score >= 85 ? 'badge-critical' : 'badge-high'}">Threat: ${data.threat_score}/100 (${data.threat_level})</span>
      </div>
      <div style="font-size:0.85rem; color:#fff; margin-bottom:0.75rem;">${data.scene_description}</div>
      <div style="margin-bottom:0.5rem;"><strong style="font-size:0.75rem; color:var(--text-muted); text-transform:uppercase;">Weapons Detected:</strong><br>${weapons}</div>
      <div style="margin-bottom:0.5rem;"><strong style="font-size:0.75rem; color:var(--text-muted); text-transform:uppercase;">Persons Identified:</strong><br>${persons}</div>
      <div class="sha-pill mono" style="margin-top:0.5rem;">SHA-256: ${data.sha256_hash}</div>
    </div>
  `;
}

// Intake Studio: Analyze Audio
async function analyzeAudio(sampleName = null, file = null) {
  showToast("Processing acoustic evidence & diarization...");
  const formData = new FormData();
  formData.append("case_id", CASE_ID);
  if (file) formData.append("file", file);
  if (sampleName) formData.append("sample_name", sampleName);

  try {
    const res = await fetch("/api/audio", { method: "POST", body: formData });
    if (!res.ok) throw new Error("Audio analysis failed");
    const data = await res.json();
    renderAudioResults(data);
    showToast(`Audio Analyzed: ${data.speakers_identified} speakers diarized`);
    await loadCaseDossier();
  } catch (err) {
    showToast(`Audio analysis error: ${err.message}`, true);
  }
}

function renderAudioResults(data) {
  const container = document.getElementById("audio-results");
  if (!container) return;
  container.style.display = "block";

  const diarization = (data.speaker_diarization || []).map(seg => `
    <div style="padding:0.4rem 0.6rem; margin-bottom:0.35rem; background:rgba(15,23,42,0.8); border-radius:6px; font-size:0.75rem;">
      <span class="mono" style="color:var(--accent-cyan); font-weight:700;">[${seg.start_time} - ${seg.end_time}] ${seg.speaker}:</span>
      <span style="color:#fff;"> "${seg.text}"</span>
      <span class="badge ${seg.acoustic_stress === 'Panic' ? 'badge-critical' : 'badge-high'}" style="font-size:0.65rem; padding:0.15rem 0.4rem; margin-left:0.5rem;">${seg.acoustic_stress}</span>
    </div>
  `).join("");

  container.innerHTML = `
    <div class="forensic-card" style="margin-top: 1rem; border-color: rgba(245, 158, 11, 0.4);">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 0.75rem;">
        <span class="badge badge-high">ACOUSTIC DIARIZATION REPORT</span>
        <span class="badge ${data.audio_threat_score >= 85 ? 'badge-critical' : 'badge-high'}">Threat: ${data.audio_threat_score}/100</span>
      </div>
      <div style="margin-bottom:0.75rem;">${diarization}</div>
      <div class="sha-pill mono">SHA-256: ${data.sha256_hash}</div>
    </div>
  `;
}

// Intake Studio: Analyze Video
async function analyzeVideo(sampleName = null, file = null) {
  showToast("Parsing surveillance video & keyframes...");
  const formData = new FormData();
  formData.append("case_id", CASE_ID);
  if (file) formData.append("file", file);
  if (sampleName) formData.append("sample_name", sampleName);

  try {
    const res = await fetch("/api/video", { method: "POST", body: formData });
    if (!res.ok) throw new Error("Video analysis failed");
    const data = await res.json();
    renderVideoResults(data);
    showToast(`Video Analyzed: ${(data.temporal_events || []).length} keyframes extracted`);
    await loadCaseDossier();
  } catch (err) {
    showToast(`Video analysis error: ${err.message}`, true);
  }
}

function renderVideoResults(data) {
  const container = document.getElementById("video-results");
  if (!container) return;
  container.style.display = "block";

  const keyframes = (data.temporal_events || []).map(kf => `
    <div style="padding:0.4rem 0.6rem; margin-bottom:0.35rem; background:rgba(15,23,42,0.8); border-radius:6px; font-size:0.75rem;">
      <span class="mono" style="color:var(--accent-cyan); font-weight:700;">[${kf.timestamp}]</span>
      <strong style="color:#fff;"> ${kf.action_summary}</strong>
      <span style="color:var(--text-secondary); display:block; font-size:0.72rem; margin-top:0.2rem;">${kf.forensic_detail}</span>
    </div>
  `).join("");

  container.innerHTML = `
    <div class="forensic-card" style="margin-top: 1rem; border-color: rgba(56, 189, 248, 0.4);">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 0.75rem;">
        <span class="badge badge-modality">CCTV TELEMETRY REPORT</span>
        <span class="badge ${data.video_threat_score >= 85 ? 'badge-critical' : 'badge-high'}">Threat: ${data.video_threat_score}/100</span>
      </div>
      <div style="font-size:0.85rem; color:#fff; margin-bottom:0.75rem;">${data.summary}</div>
      <div style="margin-bottom:0.75rem;">${keyframes}</div>
      <div class="sha-pill mono">SHA-256: ${data.sha256_hash}</div>
    </div>
  `;
}

</script>
</body>
</html>
"""

def get_dashboard_html() -> str:
    # If unbundled public/index.html exists and is fresh, use it; otherwise use STANDALONE_HTML
    index_file = PUBLIC_DIR / "index.html"
    if index_file.exists():
        try:
            raw_html = index_file.read_text(encoding="utf-8")
            css_file = PUBLIC_DIR / "styles.css"
            js_file = PUBLIC_DIR / "app.js"
            if css_file.exists() and js_file.exists():
                c = css_file.read_text(encoding="utf-8")
                j = js_file.read_text(encoding="utf-8")
                res = raw_html.replace('<link rel="stylesheet" href="/styles.css">', f"<style>\n{c}\n</style>")
                res = res.replace('<script src="/app.js"></script>', f"<script>\n{j}\n</script>")
                return res
            return raw_html
        except Exception:
            pass
    return STANDALONE_HTML
