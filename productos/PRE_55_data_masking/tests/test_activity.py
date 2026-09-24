"""Verifica que el reporte no exponga el identificador completo."""

import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRE_DIR))

from src.main import create_masked_report


def test_email_is_masked_in_shared_report():
    """La operación debe minimizar datos personales en la salida compartida."""

    report = create_masked_report()

    assert report["email"] == "a***@example.com"
