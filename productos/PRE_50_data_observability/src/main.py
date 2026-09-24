"""Integra señales operativas básicas en un reporte de observabilidad."""

import json
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]


def build_observability_report():
    """Una vista integrada permite priorizar la operación sin revisar indicadores aislados."""

    signals = json.loads((ROOT_DIR / "data" / "signals.json").read_text())
    checks = {
        "freshness": signals["age_days"] <= signals["maximum_age_days"],
        "volume": signals["rows"] >= signals["minimum_rows"],
        "schema": signals["schema_valid"],
    }
    return {"checks": checks, "healthy": all(checks.values())}
