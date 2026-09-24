"""Verifica que una reversión deje el modelo y su evidencia de auditoría."""

import json
import shutil
import subprocess
import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = PRE_DIR / "submission" / "production"


def test_rollback_restores_a_registered_version():
    """La operación debe declarar desde cuál versión y hacia cuál se revirtió."""

    try:
        subprocess.run(
            [sys.executable, "src/main.py", "--to-version", "v1"],
            cwd=PRE_DIR,
            check=True,
            capture_output=True,
            text=True,
        )
        record = json.loads(
            (OUTPUT_DIR / "rollback_record.json").read_text(encoding="utf-8")
        )

        assert record["previous_version"] == "v2"
        assert record["production_version"] == "v1"
        assert (OUTPUT_DIR / "model.pkl").exists()
    finally:
        shutil.rmtree(OUTPUT_DIR, ignore_errors=True)
