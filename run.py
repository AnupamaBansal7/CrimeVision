import os
import sys
from pathlib import Path

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

if __name__ in {"__main__", "__mp_main__"}:
    port = int(os.getenv("PORT", 8000))
    use_nicegui = "--nicegui" in sys.argv

    if use_nicegui:
        try:
            from nicegui import app as nicegui_app, ui
            from backend.routes import api_router
            from backend.models import init_db
            from ui.main_ui import build_ui
            from backend.config import UPLOADS_DIR, REPORTS_DIR, SAMPLES_DIR

            init_db()
            nicegui_app.include_router(api_router)
            nicegui_app.add_static_files('/uploads', str(UPLOADS_DIR))
            nicegui_app.add_static_files('/reports', str(REPORTS_DIR))
            nicegui_app.add_static_files('/samples', str(SAMPLES_DIR))

            @ui.page('/')
            def index_page():
                build_ui()

            print(f"==================================================================")
            print(f"  CRIMEVISION AI – NICEGUI LEGACY DASHBOARD")
            print(f"  - NiceGUI Dashboard: http://localhost:{port}/")
            print(f"==================================================================")
            ui.run(
                title="CrimeVision AI – Intelligent Multimodal Forensic Analysis Platform",
                port=port,
                reload=False,
                dark=True,
                favicon="🛡️"
            )
        except Exception as e:
            print(f"NiceGUI launch notice: {e}. Switching to standard FastAPI runtime.")
            use_nicegui = False

    if not use_nicegui:
        import uvicorn
        print(f"==================================================================")
        print(f"  CRIMEVISION AI – MULTIMODAL FORENSIC ANALYSIS PLATFORM")
        print(f"  - Web Dashboard: http://localhost:{port}/")
        print(f"  - Swagger API Docs: http://localhost:{port}/docs")
        print(f"  - REST API Endpoints: http://localhost:{port}/api/...")
        print(f"==================================================================")
        uvicorn.run("backend.main:app", host="0.0.0.0", port=port, reload=False)
