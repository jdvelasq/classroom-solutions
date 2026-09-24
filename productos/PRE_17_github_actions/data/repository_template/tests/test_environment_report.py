"""Prueba que valida el producto dentro del ambiente reproducible."""

import json
import subprocess
import sys
import unittest
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
REPORT_PATH = PRE_DIR / "submission" / "environment_report.json"


class EnvironmentReportTest(unittest.TestCase):
    """El reporte debe conservar el resultado conocido del producto simple."""

    def test_factory_totals(self):
        """La prueba permite detectar un cambio inesperado antes de publicar."""

        try:
            subprocess.run(
                [sys.executable, "src/main.py"],
                cwd=PRE_DIR,
                check=True,
                capture_output=True,
                text=True,
            )
            report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
            self.assertEqual(
                report["factory_totals"],
                [
                    {"factory_id": 1, "total_units_produced": 9303},
                    {"factory_id": 2, "total_units_produced": 9300},
                ],
            )
        finally:
            REPORT_PATH.unlink(missing_ok=True)
