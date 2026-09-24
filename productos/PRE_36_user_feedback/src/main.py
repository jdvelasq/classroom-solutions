"""Registra una señal de uso para mejorar un producto analítico."""

import json
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]


def capture_feedback(useful, comment):
    """La señal del consumidor conecta la salida analítica con su adopción real."""

    response = json.loads((ROOT_DIR / "data" / "product_response.json").read_text())
    return {"response": response, "useful": useful, "comment": comment}
