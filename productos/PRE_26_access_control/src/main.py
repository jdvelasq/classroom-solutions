"""Aplica una política mínima antes de entregar un resultado analítico."""

import json
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]


def can_access(resource, role):
    """La política separa quién puede consumir un resultado de cómo se calcula."""

    policy = json.loads((ROOT_DIR / "data" / "access_policy.json").read_text(encoding="utf-8"))
    return role in policy.get(resource, [])


def get_factory_risk_report(role):
    """Un rechazo explícito protege el producto frente a accesos no autorizados."""

    if not can_access("factory_risk_report", role):
        raise PermissionError("Rol no autorizado para factory_risk_report.")
    return {"factory_id": 2, "risk": "high"}
