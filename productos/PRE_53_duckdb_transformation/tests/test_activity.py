"""Verifica que la transformación SQL produzca el mart analítico esperado."""

import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRE_DIR))

from src.main import build_factory_totals


def test_sql_transformation_builds_factory_totals():
    """El resultado de la capa analítica debe ser reproducible y verificable."""

    assert build_factory_totals() == [(1, 9303), (2, 9300)]
