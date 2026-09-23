"""Las pruebas se implementarán junto con la solución del taller."""
from pathlib import Path
import importlib.util
import pandas as pd

FOLDER = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("pre09_main", FOLDER / "src" / "main.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
simulate_project = module.simulate_project
summarize_risk = module.summarize_risk


def test_simulation_is_deterministic_and_has_expected_size():
    parameters = pd.read_csv(FOLDER / "data" / "project_parameters.csv").iloc[0]
    assert simulate_project(parameters, 20).equals(simulate_project(parameters, 20))
    assert len(simulate_project(parameters, 20)) == 20


def test_summary_reports_risk_and_action():
    parameters = pd.read_csv(FOLDER / "data" / "project_parameters.csv").iloc[0]
    summary = summarize_risk(simulate_project(parameters, 1_000))
    assert 0 <= summary.loc[0, "loss_probability"] <= 1
    assert summary.loc[0, "recommendation"] in {"financiar", "no_financiar"}
