"""Verifica compatibilidad declarada entre consumidor y contrato."""

import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRE_DIR))

from src.main import is_compatible


def test_contract_declares_supported_consumer_versions():
    """Un cambio debe expresar quién puede seguir consumiendo el resultado."""

    assert is_compatible("1.0") is True
    assert is_compatible("3.0") is False
