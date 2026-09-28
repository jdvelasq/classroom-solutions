"""Registra una señal de uso para mejorar un producto analítico."""

import json
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]


def capture_feedback(useful, comment):
    """La señal del consumidor conecta la salida analítica con su adopción real."""

    response = json.loads((ROOT_DIR / "data" / "product_response.json").read_text())
    return {"response": response, "useful": useful, "comment": comment}


def main():
    """La señal del consumidor queda registrada."""

    output_path = ROOT_DIR / "submission" / "feedback.json"
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(json.dumps(capture_feedback(True, "Permitió priorizar la inspección."), indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
