"""Verifica que el monitoreo haga visible un cambio relevante en producción."""

import json
import subprocess
import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
REPORT_PATH = PRE_DIR / "submission" / "monitoring_report.json"


def test_monitoring_report_flags_shifted_feature():
    """Una alerta demostrable centra el taller en la operación posterior al despliegue."""

    try:
        subprocess.run(
            [sys.executable, "src/main.py"],
            cwd=PRE_DIR,
            check=True,
            capture_output=True,
            text=True,
        )
        report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))

        assert report["threshold"] == 1.0
        assert "alcohol" in report["alerts"]
    finally:
        REPORT_PATH.unlink(missing_ok=True)
