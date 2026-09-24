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


def load_data() -> pd.DataFrame:
    return pd.read_csv(ACTIVITY_DIR / "data" / "machine_throughput_export.csv")


def test_source_data_satisfies_the_contract():
    main.validate_data(load_data())


def test_contract_rejects_a_negative_production_value():
    dataframe = load_data()
    dataframe.loc[0, "daily_units_produced"] = -1

    with pytest.raises(ValueError, match="no puede ser negativo"):
        main.validate_data(dataframe)


def test_contract_rejects_an_unexpected_schema():
    dataframe = load_data().drop(columns="factory_date")

    with pytest.raises(ValueError, match="esquema"):
        main.validate_data(dataframe)


def test_contract_rejects_a_duplicate_business_key():
    dataframe = pd.concat([load_data(), load_data().iloc[[0]]], ignore_index=True)

    with pytest.raises(ValueError, match="está duplicada"):
        main.validate_data(dataframe)


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
