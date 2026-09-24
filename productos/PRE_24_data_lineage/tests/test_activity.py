"""Verifica que la transformación conserve la relación entre entrada y salida."""

import json
import subprocess
import sys
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = PRE_DIR / "submission"


def test_lineage_identifies_input_and_curated_output():
    """El reporte debe permitir rastrear el dato usado para producir el resultado."""

    try:
        subprocess.run(
            [sys.executable, "src/main.py"],
            cwd=PRE_DIR,
            check=True,
            capture_output=True,
            text=True,
        )
        lineage = json.loads((OUTPUT_DIR / "lineage.json").read_text(encoding="utf-8"))

        assert lineage["input"]["path"] == "data/raw_operations.csv"
        assert len(lineage["input"]["sha256"]) == 64
        assert lineage["output"] == {"path": "submission/factory_totals.csv", "rows": 2}
    finally:
        (OUTPUT_DIR / "factory_totals.csv").unlink(missing_ok=True)
        (OUTPUT_DIR / "lineage.json").unlink(missing_ok=True)
