"""Verifica el contrato y la configuración de despliegue del servicio."""

import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRE_DIR))

from src.main import app


def test_containerized_service_has_a_stable_score_endpoint():
    """El consumidor debe obtener una respuesta previsible después del despliegue."""

    response = app.test_client().post("/score", json={"daily_units_produced": 4700})
    dockerfile = (PRE_DIR / "Dockerfile").read_text(encoding="utf-8")

    assert response.get_json() == {"risk": "low", "threshold": 4500}
    assert "--host" in dockerfile
    assert "0.0.0.0" in dockerfile
    assert "--port" in dockerfile
    assert "8000" in dockerfile
