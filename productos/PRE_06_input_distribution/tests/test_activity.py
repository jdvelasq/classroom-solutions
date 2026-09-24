import importlib.util
import subprocess
import sys
from pathlib import Path

import pandas as pd
import pytest


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SPECIFICATION = importlib.util.spec_from_file_location(
    "input_distribution_main", ACTIVITY_DIR / "src" / "main.py"
)
main = importlib.util.module_from_spec(SPECIFICATION)
SPECIFICATION.loader.exec_module(main)


def load_inputs(name: str) -> pd.DataFrame:
    return pd.read_csv(ACTIVITY_DIR / "data" / name)


def test_model_defines_the_input_columns():
    assert main.load_model_features(ACTIVITY_DIR / "estimator.pkl") == [
        "texture_mean",
        "compactness_mean",
    ]


def test_new_inputs_are_compatible_with_training_inputs():
    training_inputs = load_inputs("training_inputs.csv")
    new_inputs = load_inputs("new_inputs.csv")

    anomaly_rate, is_compatible = main.assess_new_inputs(training_inputs, new_inputs)

    assert anomaly_rate <= main.MAX_ANOMALY_RATE
    assert is_compatible


def test_shifted_inputs_are_not_compatible_with_training_inputs():
    training_inputs = load_inputs("training_inputs.csv")
    shifted_inputs = load_inputs("new_inputs.csv").assign(
        texture_mean=lambda dataframe: dataframe["texture_mean"] + 100
    )

    anomaly_rate, is_compatible = main.assess_new_inputs(training_inputs, shifted_inputs)

    assert anomaly_rate > main.MAX_ANOMALY_RATE
    assert not is_compatible


def test_input_selection_rejects_an_unknown_column():
    dataframe = load_inputs("new_inputs.csv").assign(unexpected=1)

    with pytest.raises(ValueError, match="no coinciden"):
        main.select_model_inputs(dataframe, ["texture_mean", "compactness_mean"])


def test_main_reports_the_compatibility_assessment():
    result = subprocess.run(
        [sys.executable, "src/main.py"],
        cwd=ACTIVITY_DIR,
        check=True,
        capture_output=True,
        text=True,
    )

    assert "Tasa de entradas inusuales: " in result.stdout
    assert "Entradas compatibles: sí" in result.stdout
