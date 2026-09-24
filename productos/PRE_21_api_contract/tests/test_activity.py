"""Verifica que el contrato entregue respuestas previsibles al consumidor."""

import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRE_DIR))

from src.main import app


def test_score_returns_expected_contract_for_valid_input():
    """El consumidor debe recibir el mismo esquema para una solicitud válida."""

    response = app.test_client().post("/score", json={"daily_units_produced": 4200})

    assert response.status_code == 200
    assert response.get_json() == {"risk": "high", "threshold": 4500}


def test_score_rejects_missing_required_input():
    """Un error claro es preferible a calcular sobre información incompleta."""

    response = app.test_client().post("/score", json={})

    assert response.status_code == 400
    assert response.get_json() == {"error": "Se requiere el campo daily_units_produced."}
