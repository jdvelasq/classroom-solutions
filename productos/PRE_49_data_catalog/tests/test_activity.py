"""Verifica que la ficha incluya información mínima para operar el dataset."""

import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRE_DIR))

from src.main import load_catalog_entry


def test_catalog_identifies_owner_contract_and_consumer():
    """Un dato operativo debe declarar quién responde y quién lo utiliza."""

    entry = load_catalog_entry()

    assert entry["owner"] == "data-operations"
    assert entry["contract_version"] == "2.0"
    assert entry["consumer"] == "operations_manager"
