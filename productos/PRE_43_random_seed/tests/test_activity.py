"""Verifica que una semilla produzca siempre la misma selección."""

import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRE_DIR))

from src.main import select_sample


def test_same_seed_repeats_same_sample():
    """La reproducibilidad exige que dos ejecuciones equivalentes coincidan."""

    assert select_sample(123) == select_sample(123)
