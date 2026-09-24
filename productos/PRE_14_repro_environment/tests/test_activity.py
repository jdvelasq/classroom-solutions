"""Verifica la evidencia mínima de una ejecución reproducible."""

import json
import subprocess
import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
REPORT_PATH = PRE_DIR / "submission" / "environment_report.json"


def test_declared_environment_generates_versioned_report():
    """La evidencia debe ligar el indicador con las versiones que lo produjeron."""

    try:
        subprocess.run(
            [sys.executable, "src/main.py"],
            cwd=PRE_DIR,
            check=True,
            capture_output=True,
            text=True,
        )
        report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
        requirements = (PRE_DIR / "requirements.txt").read_text(encoding="utf-8")

        assert "pandas==2.2.3" in requirements
        assert report["pandas_version"] == "2.2.3"
        assert report["factory_totals"] == [
            {"factory_id": 1, "total_units_produced": 9303},
            {"factory_id": 2, "total_units_produced": 9300},
        ]
    finally:
        REPORT_PATH.unlink(missing_ok=True)
