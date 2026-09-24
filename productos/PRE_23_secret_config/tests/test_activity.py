"""Verifica que la aplicación use una variable de ambiente sin revelar su valor."""

import json
import os
import subprocess
import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
REPORT_PATH = PRE_DIR / "submission" / "secret_config_report.json"


def test_secret_configuration_is_confirmed_without_exposure():
    """El reporte debe evidenciar configuración, nunca conservar la credencial."""

    environment = os.environ.copy()
    environment["ANALYTICS_API_KEY"] = "only-for-test"
    try:
        subprocess.run(
            [sys.executable, "src/main.py"],
            cwd=PRE_DIR,
            check=True,
            capture_output=True,
            text=True,
            env=environment,
        )
        report_text = REPORT_PATH.read_text(encoding="utf-8")
        report = json.loads(report_text)

        assert report == {"secret_name": "ANALYTICS_API_KEY", "configured": True}
        assert "only-for-test" not in report_text
    finally:
        REPORT_PATH.unlink(missing_ok=True)
