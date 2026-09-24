"""Revierte una versión de producción sin reconstruir el modelo."""

import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT_DIR / "models" / "registry.json"
OUTPUT_DIR = ROOT_DIR / "submission" / "production"


def parse_arguments():
    """Nombrar la versión objetivo hace la reversión una decisión trazable."""

    parser = argparse.ArgumentParser()
    parser.add_argument("--to-version", required=True)
    return parser.parse_args()


def rollback(target_version):
    """La reversión conserva la versión previa y evidencia de quién quedó activa."""

    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    if target_version not in registry["versions"]:
        raise ValueError(f"Versión no registrada: {target_version}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    previous_version = registry["production_version"]
    shutil.copy2(ROOT_DIR / registry["versions"][target_version], OUTPUT_DIR / "model.pkl")
    record = {
        "previous_version": previous_version,
        "production_version": target_version,
        "rolled_back_at": datetime.now(timezone.utc).isoformat(),
    }
    (OUTPUT_DIR / "rollback_record.json").write_text(
        json.dumps(record, indent=2), encoding="utf-8"
    )
    return record


def main():
    """El resultado hace visible que volver atrás es una práctica preparada."""

    arguments = parse_arguments()
    print(json.dumps(rollback(arguments.to_version), indent=2))


if __name__ == "__main__":
    main()
