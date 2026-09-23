"""Las pruebas se implementarán junto con la solución del taller."""
from pathlib import Path
import importlib.util
import pandas as pd

FOLDER = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("pre12_main", FOLDER / "src" / "main.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_policy_evaluation_respects_scenario_probabilities():
    policies = pd.read_csv(FOLDER / "data" / "capacity_policies.csv")
    scenarios = pd.read_csv(FOLDER / "data" / "demand_scenarios.csv")
    comparison = module.evaluate(policies, scenarios)
    assert round(comparison.expected_service_rate.iloc[0], 3) == 0.815
    assert module.recommend(policies, scenarios).loc[0, "policy_id"] == "P1"
