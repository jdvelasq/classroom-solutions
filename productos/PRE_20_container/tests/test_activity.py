"""Verifica que el PRE tenga un empaquetamiento mínimo y un resultado comprobable."""

import json
import subprocess
import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
REPORT_PATH = PRE_DIR / "submission" / "factory_report.json"


def test_container_definition_and_indicator_are_ready():
    """La actividad debe declarar una imagen y conservar el resultado esperado."""

    try:
        subprocess.run(
            [sys.executable, "src/main.py"],
            cwd=PRE_DIR,
            check=True,
            capture_output=True,
            text=True,
        )
        dockerfile = (PRE_DIR / "Dockerfile").read_text(encoding="utf-8")
        report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))

        assert "FROM python:3.11-slim" in dockerfile
        assert "--no-cache-dir --requirement requirements.txt" in dockerfile
        assert 'CMD ["python", "src/main.py"]' in dockerfile
        assert report["factory_totals"] == [
            {"factory_id": 1, "total_units_produced": 9303},
            {"factory_id": 2, "total_units_produced": 9300},
        ]
    finally:
        REPORT_PATH.unlink(missing_ok=True)
