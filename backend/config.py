import os
import shutil
from pathlib import Path

# Base Paths
BASE_DIR = Path(__file__).resolve().parent.parent

# Detect Vercel / serverless / read-only filesystem environment
IS_VERCEL = bool(os.getenv("VERCEL") or os.getenv("AWS_LAMBDA_FUNCTION_NAME"))

def _resolve_dir(preferred: Path, fallback_name: str) -> Path:
    """Returns a guaranteed writable directory, falling back to /tmp in serverless/read-only environments."""
    if not IS_VERCEL:
        try:
            preferred.mkdir(parents=True, exist_ok=True)
            test_file = preferred / ".perm_check"
            test_file.touch()
            test_file.unlink(missing_ok=True)
            return preferred
        except (OSError, PermissionError):
            pass

    # Serverless fallback to /tmp
    tmp_path = Path("/tmp") / "crimevision" / fallback_name
    try:
        tmp_path.mkdir(parents=True, exist_ok=True)
    except OSError:
        pass
    return tmp_path

DATA_DIR = _resolve_dir(BASE_DIR / "data", "data")
UPLOADS_DIR = _resolve_dir(DATA_DIR / "uploads", "uploads")
REPORTS_DIR = _resolve_dir(DATA_DIR / "reports", "reports")
SAMPLES_DIR = BASE_DIR / "samples"
PUBLIC_DIR = BASE_DIR / "public"

try:
    SAMPLES_DIR.mkdir(parents=True, exist_ok=True)
except OSError:
    pass

# Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL", "").strip()
DB_PATH = DATA_DIR / "crimevision.db"

# Seed initial SQLite DB in serverless /tmp if repo template exists
REPO_DB = BASE_DIR / "data" / "crimevision.db"
if DB_PATH != REPO_DB and REPO_DB.exists() and not DB_PATH.exists():
    try:
        shutil.copy2(REPO_DB, DB_PATH)
    except Exception:
        pass
# AI Configuration
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "").strip()
CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-3-5-sonnet-20241022")

# App Metadata
APP_NAME = "CrimeVision AI"
APP_VERSION = "2.4.0-Enterprise"
APP_DESCRIPTION = "Intelligent Multimodal Forensic Analysis & Timeline Fusion Platform"

DEFAULT_CASE = {
    "case_id": "CRV-2026-8841",
    "title": "Armed Commercial Robbery - Central Metro Express",
    "incident_date": "2026-10-24 22:45:00",
    "location": "Sector 4B, 1422 North Meridian Ave",
    "lead_investigator": "Det. Marcus Vance",
    "badge_number": "MPD-7492",
    "jurisdiction": "Metro Police Forensic Investigation Unit",
    "status": "ACTIVE_INVESTIGATION"
}
