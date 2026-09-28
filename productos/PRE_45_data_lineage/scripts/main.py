"""Genera un conjunto curado y registra de qué dato provino."""

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[1]
INPUT_PATH = ROOT_DIR / "data" / "raw_operations.csv"
OUTPUT_DIR = ROOT_DIR / "submission"


def file_checksum(path):
    """La huella permite identificar la versión exacta de un insumo de datos."""

    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    """El linaje explica un resultado sin obligar a reconstruir la transformación."""

    raw_data = pd.read_csv(INPUT_PATH)
    curated_data = raw_data.groupby("factory_id", as_index=False)["daily_units_produced"].sum()
    curated_path = OUTPUT_DIR / "factory_totals.csv"
    curated_data.to_csv(curated_path, index=False)

    lineage = {
        "input": {"path": "data/raw_operations.csv", "sha256": file_checksum(INPUT_PATH)},
        "output": {"path": "submission/factory_totals.csv", "rows": len(curated_data)},
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    (OUTPUT_DIR / "lineage.json").write_text(
        json.dumps(lineage, indent=2), encoding="utf-8"
    )
    print(json.dumps(lineage, indent=2))


if __name__ == "__main__":
    main()
