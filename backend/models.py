import datetime
import json
import hashlib
from typing import List, Optional, Dict, Any
from peewee import (
    SqliteDatabase, Model, CharField, TextField, IntegerField,
    FloatField, DateTimeField, ForeignKeyField, AutoField
)
from pydantic import BaseModel, Field
from playhouse.db_url import connect
from backend.config import DB_PATH, DATABASE_URL

# Initialize Peewee Database (PostgreSQL if DATABASE_URL is set, else SQLite)
# Note: Use journal_mode='delete' (NEVER 'wal') on serverless /tmp to avoid POSIX SHM lock failures
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

if DATABASE_URL:
    try:
        db = connect(DATABASE_URL)
    except Exception as e:
        print(f"[CrimeVision DB] DATABASE_URL connect error ({e}), falling back to SQLite: {DB_PATH}")
        db = SqliteDatabase(
            str(DB_PATH),
            timeout=30.0,
            pragmas={
                'foreign_keys': 1,
                'ignore_check_constraints': 0,
                'synchronous': 1
            }
        )
else:
    db = SqliteDatabase(
        str(DB_PATH),
        timeout=30.0,
        pragmas={
            'foreign_keys': 1,
            'ignore_check_constraints': 0,
            'synchronous': 1
        }
    )
class BaseModelDB(Model):
    class Meta:
        database = db

class Case(BaseModelDB):
    case_id = CharField(unique=True, index=True, max_length=64)
    title = CharField(max_length=255)
    incident_date = CharField(max_length=64, default="2026-10-24 22:45:00")
    location = CharField(max_length=255, default="Sector 4B, 1422 North Meridian Ave")
    lead_investigator = CharField(max_length=128, default="Det. Marcus Vance")
    badge_number = CharField(max_length=64, default="MPD-7492")
    jurisdiction = CharField(max_length=128, default="Metro Police Forensic Investigation Unit")
    classification = CharField(max_length=128, default="Pending Analysis")
    classification_confidence = FloatField(default=0.0)
    penal_code = CharField(max_length=128, default="TBD")
    threat_level = CharField(max_length=32, default="EVALUATING")
    overall_threat_score = IntegerField(default=0)
    summary = TextField(default="")
    probable_cause = TextField(default="")
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)

class EvidenceItem(BaseModelDB):
    id = AutoField()
    case = ForeignKeyField(Case, backref='evidence_items', on_delete='CASCADE')
    evidence_type = CharField(max_length=32)  # image, audio, video
    filename = CharField(max_length=255)
    file_path = CharField(max_length=512)
    file_size = IntegerField(default=0)
    sha256_hash = CharField(max_length=64)
    timestamp_logged = DateTimeField(default=datetime.datetime.now)
    threat_score = IntegerField(default=0)
    analysis_status = CharField(max_length=32, default="pending")  # pending, analyzed, failed
    raw_analysis_json = TextField(default="{}")
    summary = TextField(default="")

    def get_analysis_data(self) -> Dict[str, Any]:
        try:
            return json.loads(self.raw_analysis_json) if self.raw_analysis_json else {}
        except Exception:
            return {}

class TimelineEvent(BaseModelDB):
    id = AutoField()
    case = ForeignKeyField(Case, backref='timeline_events', on_delete='CASCADE')
    evidence_id = IntegerField(null=True)
    timestamp_str = CharField(max_length=64)
    modality = CharField(max_length=32)  # IMAGE, AUDIO, VIDEO, FUSION
    title = CharField(max_length=255)
    description = TextField()
    actor = CharField(max_length=128, default="Unknown Subject")
    threat_rating = CharField(max_length=32, default="LOW")  # CRITICAL, HIGH, ELEVATED, LOW
    confidence = FloatField(default=0.90)
    cross_modal_correlation = CharField(max_length=255, default="Independent Modality")

class ChatMessage(BaseModelDB):
    id = AutoField()
    case_id = CharField(max_length=64, index=True)
    role = CharField(max_length=16)  # user, assistant
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)


_db_initialized = False

def init_db(force: bool = False):
    """Initializes tables and seeds default case if not present."""
    global _db_initialized
    if _db_initialized and not force:
        return
    try:
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        db.create_tables([Case, EvidenceItem, TimelineEvent, ChatMessage], safe=True)
        from backend.config import DEFAULT_CASE
        case = Case.get_or_none(Case.case_id == DEFAULT_CASE["case_id"])
        if not case:
            case = Case.create(
                case_id=DEFAULT_CASE["case_id"],
                title=DEFAULT_CASE["title"],
                incident_date=DEFAULT_CASE["incident_date"],
                location=DEFAULT_CASE["location"],
                lead_investigator=DEFAULT_CASE["lead_investigator"],
                badge_number=DEFAULT_CASE["badge_number"],
                jurisdiction=DEFAULT_CASE["jurisdiction"],
                classification="Commercial Armed Robbery",
                classification_confidence=0.94,
                penal_code="Penal Code § 211 - Robbery with Deadly Weapon",
                threat_level="CRITICAL",
                overall_threat_score=88,
                summary="Multi-subject aggravated commercial armed robbery at Central Metro Express. Evidence exhibits firearm brandishing, verbal threats to staff, safe breach, and rapid getaway in a dark sedan.",
                probable_cause="Forensic multimodal analysis confirms matching facial structure, dark clothing with reflective accents, recorded verbal demands for cashier safe codes, and video telemetry corroborating weapon presentation at 22:46:12."
            )
        # Auto-seed initial timeline & evidence if empty
        if EvidenceItem.select().where(EvidenceItem.case == case).count() == 0:
            try:
                from backend.services.fusion_service import MultimodalFusionEngine
                MultimodalFusionEngine.fuse_case_evidence(DEFAULT_CASE["case_id"])
            except Exception as fe:
                print(f"[CrimeVision DB] Initial evidence seed notice: {fe}")
        _db_initialized = True
    except Exception as e:
        print(f"[CrimeVision DB] Schema init warning: {e}")

def get_or_create_case(case_id: str = None) -> Case:
    """Guarantees a valid case is returned without throwing 404 or table errors."""
    init_db()
    from backend.config import DEFAULT_CASE
    cid = case_id or DEFAULT_CASE["case_id"]
    try:
        case = Case.get_or_none(Case.case_id == cid)
        if not case:
            case = Case.create(
                case_id=cid,
                title=DEFAULT_CASE["title"],
                incident_date=DEFAULT_CASE["incident_date"],
                location=DEFAULT_CASE["location"],
                lead_investigator=DEFAULT_CASE["lead_investigator"],
                badge_number=DEFAULT_CASE["badge_number"],
                jurisdiction=DEFAULT_CASE["jurisdiction"],
                classification="Commercial Armed Robbery",
                classification_confidence=0.94,
                penal_code="Penal Code § 211 - Robbery with Deadly Weapon",
                threat_level="CRITICAL",
                overall_threat_score=88,
                summary="Multi-subject aggravated commercial armed robbery at Central Metro Express.",
                probable_cause="Forensic multimodal surveillance analysis confirms weapon brandishing and rapid egress."
            )
        return case
    except Exception as e:
        print(f"[CrimeVision DB] get_or_create_case error: {e}")
        init_db(force=True)
        return Case.get_or_none(Case.case_id == cid) or Case(
            case_id=cid,
            title=DEFAULT_CASE["title"],
            incident_date=DEFAULT_CASE["incident_date"],
            location=DEFAULT_CASE["location"]
        )

# Auto-initialize database on module load so serverless execution never hits missing tables
init_db()

# ==========================================
# Pydantic Schemas for API Serialization
# ==========================================

class WeaponItem(BaseModel):
    weapon_type: str = "Unknown Implement"
    confidence: float = 0.85
    description: str = ""
    lethality_rating: str = "ELEVATED"

class PersonEntity(BaseModel):
    label: str = "Subject"
    role_estimate: str = "Suspect"  # Suspect, Victim, Witness, Bystander
    clothing: str = "Unspecified attire"
    actions: str = "Observed in scene"
    facial_features: str = "Indeterminate"

class DetectedObject(BaseModel):
    label: str = "Object"
    confidence: float = 0.85
    location_in_frame: str = "Scene"
    forensic_relevance: str = "Evidentiary context"

class ImageAnalysisResponse(BaseModel):
    status: str = "success"
    filename: str = "evidence_image.jpg"
    sha256_hash: str = ""
    people_count: int = 1
    persons: List[PersonEntity] = []
    weapons_detected: List[WeaponItem] = []
    cataloged_objects: List[DetectedObject] = []
    threat_score: int = 50
    threat_level: str = "EVALUATING"  # CRITICAL, HIGH, ELEVATED, LOW
    scene_description: str = "Forensic optical frame parsed."
    lighting_and_environment: str = "Ambient"
    forensic_tags: List[str] = []

class AudioTranscriptSegment(BaseModel):
    speaker: str
    start_time: str
    end_time: str
    text: str
    acoustic_stress: str  # Panic, Agitation, Calm, Shouting

class AudioAnalysisResponse(BaseModel):
    status: str = "success"
    filename: str
    sha256_hash: str
    full_transcript: str
    speakers_identified: int
    speaker_diarization: List[AudioTranscriptSegment] = []
    key_statements: List[str] = []
    acoustic_environment: str
    audio_threat_score: int
    threat_level: str
    extracted_admissions_or_threats: List[str] = []

class VideoEventItem(BaseModel):
    timestamp_offset: str
    scene_keyframe: str
    action_detected: str
    subjects_involved: str
    anomaly_threat_score: int
    cross_audio_sync_hint: Optional[str] = None

class VideoAnalysisResponse(BaseModel):
    status: str = "success"
    filename: str
    sha256_hash: str
    duration_str: str
    keyframe_count: int
    timeline_events: List[VideoEventItem] = []
    suspect_trajectory: str
    escape_route_observed: str
    video_threat_score: int
    threat_level: str
    summary: str

class CrimeClassificationResult(BaseModel):
    primary_crime: str
    confidence: float
    statutory_code: str
    intent_level: str
    secondary_offenses: List[str] = []
    justification: str

class TimelineFusionEvent(BaseModel):
    timestamp: str
    modality: str
    source_ref: str
    event_headline: str
    detailed_narrative: str
    threat_score: int
    corroboration: str

class FusionAnalysisResponse(BaseModel):
    case_id: str
    classification: CrimeClassificationResult
    composite_threat_score: int
    composite_threat_level: str
    fused_timeline: List[TimelineFusionEvent]
    multimodal_correlations: List[str]
    investigative_leads: List[str]
    probable_cause_draft: str

class ChatQueryRequest(BaseModel):
    case_id: str = "CRV-2026-8841"
    query: str

class ChatQueryResponse(BaseModel):
    response: str
    citations: List[str] = []
    suggested_followups: List[str] = []
