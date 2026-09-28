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


def main():
    """El reporte entregado a un rol autorizado queda registrado."""

    output_path = ROOT_DIR / "submission" / "factory_risk_report.json"
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(json.dumps(get_factory_risk_report("operations_manager"), indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
