"""Verifica que la carga incremental conserve solo eventos nuevos."""

import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRE_DIR))

from src.main import process_new_events


def test_watermark_selects_only_new_events():
    """La carga incremental debe avanzar la marca al último evento procesado."""

    assert process_new_events() == {"processed_ids": [2], "new_watermark": "2026-09-24T10:00:00Z"}
