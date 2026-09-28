"""Expone una capacidad analítica mínima mediante un contrato estable."""

import json
from pathlib import Path

from flask import Flask, jsonify, request


ROOT_DIR = Path(__file__).resolve().parents[1]


app = Flask(__name__)


def validate_payload(payload):
    """Un contrato explícito evita que el producto falle silenciosamente en producción."""

    if not isinstance(payload, dict) or "daily_units_produced" not in payload:
        return "Se requiere el campo daily_units_produced."
    if not isinstance(payload["daily_units_produced"], int):
        return "daily_units_produced debe ser un entero."
    return None


def classify_risk(daily_units_produced):
    """La regla conocida permite concentrar la actividad en el contrato de entrega."""

    return "high" if daily_units_produced < 4500 else "low"


@app.post("/score")
def score():
    """La respuesta conserva nombres estables que un consumidor puede integrar."""

    payload = request.get_json(silent=True)
    error = validate_payload(payload)
    if error:
        return jsonify({"error": error}), 400

    return jsonify(
        {
            "risk": classify_risk(payload["daily_units_produced"]),
            "threshold": 4500,
        }
    )


def main():
    """Las respuestas de ejemplo documentan el contrato antes de publicar el servicio."""

    client = app.test_client()
    examples = {
        "valid": client.post("/score", json={"daily_units_produced": 4200}).get_json(),
        "missing_field": client.post("/score", json={}).get_json(),
    }
    output_path = ROOT_DIR / "submission" / "score_examples.json"
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(json.dumps(examples, indent=2, ensure_ascii=False), encoding="utf-8")
    app.run(port=8000)


if __name__ == "__main__":
    main()
