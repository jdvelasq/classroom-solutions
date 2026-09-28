"""Registra y verifica la identidad de un archivo de datos con un manifiesto."""

import csv
import hashlib
import json
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT_DIR / "data" / "raw" / "daily_operations.csv"
MANIFEST_PATH = ROOT_DIR / "submission" / "data_manifest.json"


def describe_data(path):
    """La identidad completa permite distinguir archivos iguales en nombre pero no en contenido."""

    with path.open() as input_file:
        columns = next(csv.reader(input_file))
    return {
        "version": "daily-operations-v1",
        "path": "data/raw/daily_operations.csv",
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "bytes": path.stat().st_size,
        "columns": columns,
    }


def main():
    """El manifiesto es el artefacto que se versionaría junto con el código en Git."""

    manifest = describe_data(DATA_PATH)
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
