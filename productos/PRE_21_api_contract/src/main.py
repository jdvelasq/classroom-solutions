"""Expone una capacidad analítica mínima mediante un contrato estable."""

from flask import Flask, jsonify, request


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


if __name__ == "__main__":
    app.run()
