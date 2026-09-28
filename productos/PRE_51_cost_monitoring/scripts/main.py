"""Compara el costo acumulado de operación con un presupuesto declarado."""

import json
from decimal import Decimal
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]


def monitor_cost():
    """El costo visible permite operar una capacidad analítica con un límite explícito."""

    data = json.loads((ROOT_DIR / "data" / "costs.json").read_text())
    total = sum(Decimal(str(cost)) for cost in data["runs"])
    budget = Decimal(str(data["budget"]))
    return {"cost": float(total), "budget": float(budget), "alert": total > budget}


def main():
    """La comparación entre costo y presupuesto queda registrada."""

    output_path = ROOT_DIR / "submission" / "cost_report.json"
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(json.dumps(monitor_cost(), indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
