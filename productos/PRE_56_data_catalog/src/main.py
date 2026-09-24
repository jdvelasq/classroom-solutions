"""Recupera la ficha operacional de un dataset desde un catálogo mínimo."""

import json
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]


def load_catalog_entry():
    """La ficha compartida aclara responsabilidad y uso antes de operar el dato."""

    return json.loads((ROOT_DIR / "data" / "catalog.json").read_text())
