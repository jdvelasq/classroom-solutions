"""Verifica que una alerta importante reciba una respuesta operativa clara."""

import json
import subprocess
import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
INCIDENT_PATH = PRE_DIR / "submission" / "incident.json"


def test_high_severity_alert_creates_owned_incident():
    """Un incidente debe tener dueño, prioridad y acción inicial antes de escalar."""

    try:
        subprocess.run(
            [sys.executable, "src/main.py"],
            cwd=PRE_DIR,
            check=True,
            capture_output=True,
            text=True,
        )
        incident = json.loads(INCIDENT_PATH.read_text(encoding="utf-8"))

        assert incident["status"] == "open"
        assert incident["owner"] == "data-operations"
        assert incident["priority"] == "P1"
        assert incident["initial_action"] == "review_input_data"
    finally:
        INCIDENT_PATH.unlink(missing_ok=True)
