"""Recupera el runbook asociado a un síntoma operacional."""

import json
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]


def get_runbook(symptom):
    """Un procedimiento escrito permite responder sin depender de memoria individual."""

    if symptom != "freshness_alert":
        raise ValueError("No hay runbook para este síntoma.")
    return (ROOT_DIR / "RUNBOOK.md").read_text()
