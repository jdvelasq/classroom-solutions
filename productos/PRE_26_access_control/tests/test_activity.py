"""Verifica que la política permita y rechace accesos de manera inequívoca."""

import sys
from pathlib import Path

import pytest


PRE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRE_DIR))

from src.main import get_factory_risk_report


def test_authorized_role_receives_report():
    """El consumidor autorizado debe obtener el resultado acordado."""

    assert get_factory_risk_report("operations_manager") == {"factory_id": 2, "risk": "high"}


def test_unauthorized_role_is_rejected():
    """La ausencia de autorización debe detener la entrega del resultado."""

    with pytest.raises(PermissionError, match="Rol no autorizado"):
        get_factory_risk_report("intern")
