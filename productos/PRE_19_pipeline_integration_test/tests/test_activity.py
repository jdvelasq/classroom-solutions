"""Verifica de extremo a extremo la salida de un flujo de datos pequeño."""

import json
import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRE_DIR))

from src.main import run_pipeline


def test_pipeline_publishes_expected_output():
    """La prueba debe cubrir entrada, transformación y artefacto de salida."""

    output = run_pipeline()
    try:
        assert json.loads(output.read_text()) == {"factory_totals": {"1": 9303, "2": 9300}}
    finally:
        output.unlink(missing_ok=True)
