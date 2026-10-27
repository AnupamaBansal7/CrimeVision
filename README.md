# CrimeVision AI – Intelligent Multimodal Forensic Analysis Platform

An enterprise-grade digital forensic investigation platform combining **FastAPI**, **NiceGUI** (Python-native Web Framework), and **Anthropic Claude 3.5 Sonnet** for multimodal evidence intelligence, timeline fusion, and official report generation.

Strictly built without MERN / Node.js / JavaScript frameworks — 100% Python-native stack.

---

## 🏛️ System Architecture

```
CrimeVision/
├── backend/
│   ├── main.py              # Standalone FastAPI microservice
│   ├── config.py            # System configuration & Claude model settings
│   ├── models.py            # Peewee ORM SQLite models & Pydantic schemas
│   ├── routes.py            # RESTful JSON microservice endpoints (/api/...)
│   ├── services/
│   │   ├── claude_service.py # Anthropic Claude 3.5 Sonnet + Forensic Mock Fallback
│   │   ├── fusion_service.py # Chronological multimodal timeline fusion engine
│   │   └── pdf_service.py    # ReportLab official forensic PDF builder
│   └── requirements.txt
├── ui/
│   ├── main_ui.py           # NiceGUI 5-Tab Dashboard & Evidence Studio
│   ├── components.py        # Custom UI cards, threat dials & waveform players
│   └── theme.py             # Dark tactical cyber-forensic styling
├── samples/                 # Pre-bundled forensic samples (Surveillance, Dispatch, CCTV)
├── data/                    # SQLite database, uploaded evidence, and generated reports
├── run.py                   # Master entrypoint booting unified full-stack application
└── requirements.txt
```

---

## 🚀 Key Modules & Capabilities

### 1. Image Analysis Module (`/api/image`)
- **Weapon Detection & Threat Scoring**: Detects firearms, edged weapons, blunt force tools with lethality classification.
- **Subject Extraction**: Estimates suspect vs victim roles, attire, action verbs, and facial orientation.
- **Object Cataloging**: Categorizes physical evidence (cash drawers, duffel bags, tools, license plates).
- **Cryptographic Chain of Custody**: Automatic SHA-256 calculation for evidentiary integrity.

### 2. Audio Analysis Module (`/api/audio`)
- **Speech-to-Text Transcription**: Forensic speech recognition with time offsets.
- **Speaker Diarization**: Isolates distinct acoustic sources (Suspect Alpha, Store Clerk, Accomplice).
- **Acoustic Stress Analysis**: Identifies vocal agitation, panic pitches, shouting, and background reverberation.
- **Verbal Threat Extraction**: Isolates key statements, admissions, and demands.

### 3. Video Analysis Module (`/api/video`)
- **Keyframe Breakdown**: Chronological action timeline from surveillance video feeds.
- **Subject Trajectory Mapping**: Analyzes breach points, interior path, and egress corridor.
- **Escape Telemetry**: Logs getaway vehicle make, color, direction of flight, and anomaly ratings.

### 4. Multimodal Fusion Engine & Crime Classifier (`/api/fuse`)
- **Timeline Fusion**: Temporally synchronizes optical frames, acoustic spikes, and video keyframes.
- **Cross-Modal Corroboration**: Pairs visual firearm drawing with vocal coercion acoustics.
- **Automated Crime Classification**: Classifies crime into Armed Robbery, Burglary, Homicide, Accident, or Assault with statutory penal code mapping (e.g., Penal Code § 211).
- **Sworn Probable Cause Affidavit**: Automated legal drafting for search/arrest warrants.

### 5. NiceGUI Enterprise Dashboard
- **Tab 1: Executive Summary & Case Overview**: Case metadata, 4 KPI cards, threat dials, probable cause draft.
- **Tab 2: Evidence Intake & Processing Studio**: Dedicated Image, Audio, and Video studios with live uploads, preview players, and pre-loaded forensic test samples.
- **Tab 3: Interactive Forensic Timeline**: Chronological view with modality filter chips ([ALL], [IMAGE], [AUDIO], [VIDEO], [FUSION]).
- **Tab 4: Forensic Copilot (Chat)**: Conversational assistant grounded in case evidence with quick prompt chips.
- **Tab 5: PDF Export & Chain of Custody**: Verification ledger with SHA-256 hashes and 1-click ReportLab PDF export.

---

## ⚡ Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. (Optional) Configure Anthropic API Key
```bash
# Windows PowerShell
$env:ANTHROPIC_API_KEY = "your-api-key-here"

# Linux / Mac
export ANTHROPIC_API_KEY="your-api-key-here"
```
> *Note:* If no API key is provided, CrimeVision automatically operates in high-fidelity mock fallback mode so all features work out of the box!

### 3. Launch Platform Locally
```bash
# Standard Web Dashboard + FastAPI Server (Matches Vercel Architecture)
python run.py

# Optional: Legacy NiceGUI Dashboard
python run.py --nicegui
```
- **Web Dashboard**: [http://localhost:8000/](http://localhost:8000/)
- **FastAPI Swagger API Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **REST Endpoints**: [http://localhost:8000/api/...](http://localhost:8000/api/...)

---

## ☁️ Deploying to Vercel

CrimeVision is fully architected for 1-click deployment on **Vercel**:

1. **Push to GitHub**:
   Push your repository to GitHub / GitLab / Bitbucket.

2. **Import into Vercel**:
   - Click **Add New Project** in your Vercel Dashboard.
   - Select your CrimeVision repository.
   - Framework Preset: **Other** (Vercel automatically detects `vercel.json`, `api/index.py`, and `public/`).

3. **Environment Variables**:
   Add the following in Vercel Project Settings > Environment Variables:
   - `ANTHROPIC_API_KEY`: *(Optional)* Your Claude 3.5 Sonnet API key. If omitted, CrimeVision operates in resilient forensic mock fallback mode.
   - `DATABASE_URL`: *(Optional)* Connection string for external PostgreSQL (e.g. Neon, Supabase, Railway). If omitted, CrimeVision uses an auto-seeded SQLite database in `/tmp`.

4. **Deploy**:
   - Click **Deploy**.
   - Your CrimeVision Web Dashboard will be live at `https://<your-project>.vercel.app/` with Edge CDN delivery and serverless API endpoints at `/api/...`.
