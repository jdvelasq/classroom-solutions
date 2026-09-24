"""Verifica que un dato vencido produzca una alerta de frescura."""

import json
import subprocess
import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
REPORT_PATH = PRE_DIR / "submission" / "freshness_report.json"


def test_stale_data_is_flagged():
    """La operación debe distinguir un resultado actual de uno vencido."""

    try:
        subprocess.run([sys.executable, "src/main.py"], cwd=PRE_DIR, check=True)
        assert json.loads(REPORT_PATH.read_text()) == {"age_days": 4, "maximum_age_days": 1, "alert": True}
    finally:
        REPORT_PATH.unlink(missing_ok=True)
