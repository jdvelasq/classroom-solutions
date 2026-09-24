"""Verifica que el dato inválido no llegue a la salida válida y conserve su causa."""

import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRE_DIR))

from src.main import quarantine_invalid_records


def test_invalid_record_is_quarantined_with_reason():
    """Un rechazo útil debe conservar el registro y explicar por qué no pasó."""

    result = quarantine_invalid_records()

    assert result["valid"] == [{"id": 1, "amount": 20}]
    assert result["quarantined"][0]["rejection_reason"] == "amount_must_be_non_negative"
