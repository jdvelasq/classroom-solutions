"""Compara métricas de origen y destino antes de publicar una salida de datos."""

import json
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]


def reconcile():
    """Coincidir en filas no basta: también debe conservarse un total de control."""

    source = json.loads((ROOT_DIR / "data" / "source.json").read_text())
    target = json.loads((ROOT_DIR / "data" / "target.json").read_text())
    checks = {"rows": source["rows"] == target["rows"], "total_amount": source["total_amount"] == target["total_amount"]}
    return {"checks": checks, "reconciled": all(checks.values())}


def main():
    """El resultado de la conciliación queda registrado antes de publicar."""

    output_path = ROOT_DIR / "submission" / "reconciliation.json"
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(json.dumps(reconcile(), indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
