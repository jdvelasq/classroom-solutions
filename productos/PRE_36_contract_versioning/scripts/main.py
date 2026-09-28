"""Verifica que un consumidor pueda aceptar una versión declarada de contrato."""

import json
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]


def is_compatible(consumer_version):
    """La compatibilidad explícita evita romper integraciones con un cambio de esquema."""

    contract = json.loads((ROOT_DIR / "data" / "contract.json").read_text())
    return consumer_version in contract["compatible_with"]


def main():
    """La compatibilidad de cada versión consumidora queda registrada."""

    output_path = ROOT_DIR / "submission" / "compatibility.json"
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(json.dumps({version: is_compatible(version) for version in ["1.0", "3.0"]}, indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
