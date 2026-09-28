"""Evalúa un nivel de servicio a partir de ejecuciones observadas."""

import json
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]


def evaluate_service_level():
    """Una meta explícita permite decidir si la operación cumple lo acordado."""

    executions = json.loads((ROOT_DIR / "data" / "executions.json").read_text())
    availability = executions["successful"] / executions["total"]
    return {"availability": availability, "target": executions["target"], "met": availability >= executions["target"]}


def main():
    """La evaluación del nivel de servicio queda registrada."""

    output_path = ROOT_DIR / "submission" / "service_level.json"
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(json.dumps(evaluate_service_level(), indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
