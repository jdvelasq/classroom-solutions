"""Las pruebas se implementarán junto con la solución del taller."""
from pathlib import Path
import sys
import pandas as pd

FOLDER = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FOLDER / "src"))
from solution import evaluate_policies, recommend


def test_policy_is_feasible_and_traced_to_a_decisor():
    policies = pd.read_csv(FOLDER / "data" / "policy_options.csv")
    chosen = recommend(policies)
    assert chosen.loc[0, "policy_id"] == "P1"
    assert bool(chosen.loc[0, "feasible"])
    assert chosen.loc[0, "decision_owner"] == "Dirección académica"


def test_capacity_and_minimum_are_checked():
    policies = pd.read_csv(FOLDER / "data" / "policy_options.csv")
    evaluated = evaluate_policies(policies)
    assert evaluated.capacity_ok.all()
    assert evaluated.minimum_ok.all()
