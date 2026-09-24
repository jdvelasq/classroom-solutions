"""Verifica que el reporte integrado exponga cada señal y el estado global."""

import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRE_DIR))

from src.main import build_observability_report


def test_report_combines_operational_signals():
    """Una vista común debe indicar qué falló y si el dato es apto para operar."""

    report = build_observability_report()

    assert report["checks"] == {"freshness": False, "volume": False, "schema": True}
    assert report["healthy"] is False
