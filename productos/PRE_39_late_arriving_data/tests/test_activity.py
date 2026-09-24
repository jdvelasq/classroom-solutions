"""Verifica que un registro tardío se dirija al proceso correcto."""

import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRE_DIR))

from src.main import classify_arrival


def test_late_event_requests_backfill():
    """Un evento histórico no debe confundirse con la carga corriente."""

    assert classify_arrival() == {"late": True, "action": "backfill"}
