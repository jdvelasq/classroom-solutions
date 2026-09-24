"""Verifica que una liberación publique una versión y sus notas."""

import json
import subprocess
import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
MANIFEST_PATH = PRE_DIR / "submission" / "release_manifest.json"


def test_release_manifest_has_version_and_notes():
    """El consumidor debe poder reconocer qué liberación está usando."""

    try:
        subprocess.run([sys.executable, "src/main.py"], cwd=PRE_DIR, check=True)
        manifest = json.loads(MANIFEST_PATH.read_text())

        assert manifest["version"] == "1.0.0"
        assert manifest["release_notes"] == "CHANGELOG.md"
    finally:
        MANIFEST_PATH.unlink(missing_ok=True)
