"""Recupera la ficha operacional de un dataset desde un catálogo mínimo."""

import json
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]


def load_catalog_entry():
    """La ficha compartida aclara responsabilidad y uso antes de operar el dato."""

    return json.loads((ROOT_DIR / "data" / "catalog.json").read_text())


def main():
    """La ficha del dataset queda registrada."""

    output_path = ROOT_DIR / "submission" / "catalog_entry.json"
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(json.dumps(load_catalog_entry(), indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
