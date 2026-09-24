import importlib.util
from pathlib import Path

import pandas as pd
import pytest


# Se importa el módulo real para que pytest revise el mismo código que se ejecutará en el taller.

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPECIFICATION = importlib.util.spec_from_file_location(
    "pytest_pandas_main", ACTIVITY_DIR / "src" / "main.py"
)
main = importlib.util.module_from_spec(SPECIFICATION)
SPECIFICATION.loader.exec_module(main)

build_certified_driver_totals = main.build_certified_driver_totals


def test_builds_totals_for_certified_drivers_only():
    # Un conjunto pequeño permite verificar qué conductores entran al indicador y por qué.

    drivers = pd.DataFrame(
        {
            "driverId": [10, 11, 12],
            "name": ["Ana", "Bruno", "Carla"],
            "certified": ["Y", "N", "Y"],
        }
    )
    timesheet = pd.DataFrame(
        {
            "driverId": [10, 10, 11, 12],
            "hours-logged": [8, 7, 9, 6],
            "miles-logged": [120, 100, 140, 90],
        }
    )

    summary = build_certified_driver_totals(drivers, timesheet)

    expected = pd.DataFrame(
        {
            "driverId": [10, 12],
            "name": ["Ana", "Carla"],
            "total_hours": [15, 6],
            "total_miles": [220, 90],
        }
    )
    pd.testing.assert_frame_equal(summary, expected)


def test_rejects_a_timesheet_without_required_columns():
    # Una entrada incompleta debe fallar antes de producir un resumen engañoso.

    drivers = pd.DataFrame(
        {"driverId": [10], "name": ["Ana"], "certified": ["Y"]}
    )
    timesheet = pd.DataFrame({"driverId": [10], "hours-logged": [8]})

    with pytest.raises(ValueError, match="turnos"):
        build_certified_driver_totals(drivers, timesheet)
