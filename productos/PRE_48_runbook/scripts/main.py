"""Recupera el runbook asociado a un síntoma operacional."""

import json
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]


def get_runbook(symptom):
    """Un procedimiento escrito permite responder sin depender de memoria individual."""

    if symptom != "freshness_alert":
        raise ValueError("No hay runbook para este síntoma.")
    return (ROOT_DIR / "RUNBOOK.md").read_text()


def main():
    """El procedimiento consultado queda disponible para quien atienda la alerta."""

    output_path = ROOT_DIR / "submission" / "freshness_alert_runbook.md"
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(get_runbook("freshness_alert"), encoding="utf-8")


if __name__ == "__main__":
    main()
