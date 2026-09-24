"""Verifica que el backfill limite el reproceso al periodo solicitado."""

import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRE_DIR))

from src.main import select_backfill


def test_backfill_selects_explicit_historical_range():
    """Reprocesar debe ser una acción acotada y auditable."""

    assert select_backfill("2026-09-20", "2026-09-21") == [1, 2]
