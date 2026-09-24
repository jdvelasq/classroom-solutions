"""Verifica que repetir una tarea conserve un único resultado."""

import json
import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRE_DIR))

from src.main import OUTPUT_PATH, generate_daily_report


def test_repeated_execution_preserves_one_report():
    """La segunda ejecución debe recuperar, no duplicar, el resultado existente."""

    try:
        first = generate_daily_report()
        second = generate_daily_report()

        assert first == second
        assert json.loads(OUTPUT_PATH.read_text(encoding="utf-8")) == first
    finally:
        OUTPUT_PATH.unlink(missing_ok=True)
