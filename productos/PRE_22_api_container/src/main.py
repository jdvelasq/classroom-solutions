"""Expone una capacidad analítica mínima desde un contenedor."""

from flask import Flask, jsonify, request


app = Flask(__name__)


def validate_payload(payload):
    """La validación mantiene el contrato estable al cruzar el límite del servicio."""

    if not isinstance(payload, dict) or "daily_units_produced" not in payload:
        return "Se requiere el campo daily_units_produced."
    if not isinstance(payload["daily_units_produced"], int):
        return "daily_units_produced debe ser un entero."
    return None


@app.post("/score")
def score():
    """La regla simple deja que el despliegue sea el único tema nuevo del PRE."""

    payload = request.get_json(silent=True)
    error = validate_payload(payload)
    if error:
        return jsonify({"error": error}), 400
    risk = "high" if payload["daily_units_produced"] < 4500 else "low"
    return jsonify({"risk": risk, "threshold": 4500})
