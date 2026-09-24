"""Verifica que una recomendación requiera una decisión humana explícita."""

import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRE_DIR))

from src.main import review_recommendation


def test_approval_is_explicit():
    """La autorización no debe inferirse automáticamente de una predicción."""

    assert review_recommendation("reject")["action_authorized"] is False
    assert review_recommendation("approve")["action_authorized"] is True
