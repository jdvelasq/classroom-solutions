"""Migra un registro de contrato v1 a contrato v2."""

import json
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]


def migrate_v1_to_v2(record):
    """La migración explícita preserva consumidores mientras evoluciona el esquema."""

    return {"schema_version": "2.0", "factory_id": record["factory"], "risk": record["risk"]}


if __name__ == "__main__":
    source = json.loads((ROOT_DIR / "data" / "record_v1.json").read_text())
    (ROOT_DIR / "submission" / "record_v2.json").write_text(json.dumps(migrate_v1_to_v2(source)))
