"""Convierte una alerta técnica en un incidente operativo rastreable."""

import json
from datetime import datetime, timezone
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]


def main():
    """Una respuesta explícita evita que una alerta se pierda entre los registros."""

    alert = json.loads(
        (ROOT_DIR / "data" / "monitoring_alert.json").read_text(encoding="utf-8")
    )
    incident = {
        "incident_id": "incident-001",
        "alert_id": alert["alert_id"],
        "status": "open",
        "owner": "data-operations",
        "priority": "P1" if alert["severity"] == "high" else "P2",
        "initial_action": "review_input_data",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    output_path = ROOT_DIR / "submission" / "incident.json"
    output_path.write_text(json.dumps(incident, indent=2), encoding="utf-8")
    print(json.dumps(incident, indent=2))


if __name__ == "__main__":
    main()
