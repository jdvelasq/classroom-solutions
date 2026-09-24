"""Verifica que un costo que excede el presupuesto active una alerta."""

import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRE_DIR))

from src.main import monitor_cost


def test_cost_exceeding_budget_is_visible():
    """La operación debe detectar un costo antes de que se normalice como sorpresa."""

    result = monitor_cost()

    assert result["cost"] == 3.7
    assert result["alert"] is True
