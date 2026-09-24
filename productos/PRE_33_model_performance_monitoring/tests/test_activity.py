"""Verifica que una degradación de desempeño produzca una alerta."""

import json
import subprocess
import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
REPORT_PATH = PRE_DIR / "submission" / "performance_report.json"


def test_performance_alert_is_reported():
    """Una métrica por debajo del mínimo debe ser visible para la operación."""

    try:
        subprocess.run([sys.executable, "src/main.py"], cwd=PRE_DIR, check=True)
        report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))

        assert report["accuracy"] == 0.6
        assert report["alert"] is True
    finally:
        REPORT_PATH.unlink(missing_ok=True)
