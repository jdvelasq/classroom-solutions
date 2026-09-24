"""Verifica que la promoción produzca un registro y artefacto recuperables."""

import json
import shutil
import subprocess
import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
REGISTRY_DIR = PRE_DIR / "submission" / "model_registry"


def test_candidate_can_be_promoted_to_production():
    """Producción debe señalar una versión concreta y conservar su artefacto."""

    try:
        subprocess.run(
            [sys.executable, "src/main.py", "--stage", "production"],
            cwd=PRE_DIR,
            check=True,
            capture_output=True,
            text=True,
        )
        record = json.loads(
            (REGISTRY_DIR / "production" / "registry.json").read_text(encoding="utf-8")
        )

        assert record["model_id"] == "candidate_v1"
        assert record["stage"] == "production"
        assert (REGISTRY_DIR / "production" / "model.pkl").exists()
    finally:
        shutil.rmtree(REGISTRY_DIR, ignore_errors=True)
