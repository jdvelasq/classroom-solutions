"""Verifica que el incumplimiento del nivel de servicio sea visible."""

import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRE_DIR))

from src.main import evaluate_service_level


def test_service_level_is_compared_to_target():
    """La operación debe evidenciar cuándo el acuerdo no se cumplió."""

    result = evaluate_service_level()

    assert result["availability"] == 0.9
    assert result["met"] is False
