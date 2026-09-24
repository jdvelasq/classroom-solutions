import importlib.util
import subprocess
import sys
from pathlib import Path

import pandas as pd
import pytest


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPECIFICATION = importlib.util.spec_from_file_location(
    "data_testing_main", ACTIVITY_DIR / "src" / "main.py"
)
main = importlib.util.module_from_spec(SPECIFICATION)
SPECIFICATION.loader.exec_module(main)


def load_data(filename: str) -> pd.DataFrame:
    return pd.read_csv(ACTIVITY_DIR / "data" / filename)


def test_source_data_satisfies_the_contract():
    main.validate_data(load_data("machine_throughput_export.csv"))


@pytest.mark.parametrize(
    ("filename", "message"),
    [
        ("invalid_negative_production.csv", "no puede ser negativo"),
        ("invalid_duplicate_key.csv", "está duplicada"),
        ("invalid_date.csv", "fechas válidas"),
        ("invalid_schema.csv", "esquema"),
    ],
)
def test_problematic_datasets_do_not_satisfy_the_contract(filename, message):
    with pytest.raises(ValueError, match=message):
        main.validate_data(load_data(filename))


def test_main_reports_the_validated_row_count():
    result = subprocess.run(
        [sys.executable, "src/main.py"],
        cwd=ACTIVITY_DIR,
        check=True,
        capture_output=True,
        text=True,
    )

    assert "Contrato de datos válido." in result.stdout
    assert "Filas validadas: 18350" in result.stdout
