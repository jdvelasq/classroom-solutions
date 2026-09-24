"""Evalúa un nivel de servicio a partir de ejecuciones observadas."""

import json
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]


def evaluate_service_level():
    """Una meta explícita permite decidir si la operación cumple lo acordado."""

    executions = json.loads((ROOT_DIR / "data" / "executions.json").read_text())
    availability = executions["successful"] / executions["total"]
    return {"availability": availability, "target": executions["target"], "met": availability >= executions["target"]}
