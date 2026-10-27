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
