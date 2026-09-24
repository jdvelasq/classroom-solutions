"""Verifica que un consumidor pueda aceptar una versión declarada de contrato."""

import json
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]


def is_compatible(consumer_version):
    """La compatibilidad explícita evita romper integraciones con un cambio de esquema."""

    contract = json.loads((ROOT_DIR / "data" / "contract.json").read_text())
    return consumer_version in contract["compatible_with"]
