"""Verifica que la retroalimentación preserve respuesta y percepción del usuario."""

import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRE_DIR))

from src.main import capture_feedback


def test_feedback_keeps_consumer_signal():
    """La mejora debe poder asociarse con el resultado que recibió el consumidor."""

    feedback = capture_feedback(True, "Permitió priorizar la inspección.")

    assert feedback["response"]["risk"] == "high"
    assert feedback["useful"] is True
