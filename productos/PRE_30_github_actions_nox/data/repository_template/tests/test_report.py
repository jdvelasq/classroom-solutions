"""Prueba del producto que será ejecutada por la sesión de Nox."""

import json
import subprocess
import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
REPORT_PATH = PRE_DIR / "submission" / "report.json"


def test_factory_totals():
    """La sesión debe comprobar un resultado analítico reproducible."""

    try:
        subprocess.run([sys.executable, "src/main.py"], cwd=PRE_DIR, check=True)
        report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))

        assert report["factory_totals"] == {"1": 9303, "2": 9300}
    finally:
        REPORT_PATH.unlink(missing_ok=True)
