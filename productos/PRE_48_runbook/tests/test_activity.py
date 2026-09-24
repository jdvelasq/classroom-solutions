"""Verifica que el incidente tenga una guía operativa recuperable."""

import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRE_DIR))

from src.main import get_runbook


def test_freshness_alert_has_actionable_runbook():
    """La guía debe indicar una verificación y evitar publicar datos vencidos."""

    runbook = get_runbook("freshness_alert")

    assert "Verifique" in runbook
    assert "No publique" in runbook
