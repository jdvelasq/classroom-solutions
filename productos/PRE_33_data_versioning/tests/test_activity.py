"""Verifica que el manifiesto identifique el archivo de datos usado."""

import json
import subprocess
import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
MANIFEST_PATH = PRE_DIR / "submission" / "data_manifest.json"


def test_manifest_registers_data_identity():
    """La versión debe incluir nombre, huella y esquema del insumo real."""

    try:
        subprocess.run([sys.executable, "src/main.py"], cwd=PRE_DIR, check=True)
        manifest = json.loads(MANIFEST_PATH.read_text())

        assert manifest["version"] == "daily-operations-v1"
        assert len(manifest["sha256"]) == 64
        assert manifest["columns"] == ["factory_id", "machine_id", "daily_units_produced"]
    finally:
        MANIFEST_PATH.unlink(missing_ok=True)
