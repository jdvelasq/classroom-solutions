"""Verifica que una diferencia entre origen y destino bloquee la reconciliación."""

import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRE_DIR))

from src.main import reconcile


def test_total_difference_is_detected():
    """Una publicación debe detenerse aunque el número de filas coincida."""

    result = reconcile()

    assert result["checks"] == {"rows": True, "total_amount": False}
    assert result["reconciled"] is False
