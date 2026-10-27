import sys
import types
from pathlib import Path

# When deployed as an isolated Vercel service with root 'backend', ensure 'backend' package resolves
_cur = Path(__file__).resolve().parent
if "backend" not in sys.modules:
    try:
        import backend
    except ImportError:
        _pkg = types.ModuleType("backend")
        _pkg.__path__ = [str(_cur)]
        _pkg.__file__ = str(_cur / "__init__.py")
        sys.modules["backend"] = _pkg

if str(_cur) not in sys.path:
    sys.path.insert(0, str(_cur))
