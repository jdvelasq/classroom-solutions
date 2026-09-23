"""Las pruebas se implementarán junto con la solución del taller."""
from pathlib import Path
import sys

import pandas as pd

FOLDER = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FOLDER / "src"))

from solution import evaluate_policies, make_decision_brief


def test_recommendation_is_feasible_and_traceable():
    options = pd.read_csv(FOLDER / "data" / "policy_options.csv")
    brief = make_decision_brief(options)

    assert brief.loc[0, "policy_id"] == "P2"
    assert bool(brief.loc[0, "capacity_ok"])
    assert bool(brief.loc[0, "exposure_ok"])
    assert brief.loc[0, "decision_owner"] == "Responsable comercial"


def test_infeasible_policy_is_not_recommended():
    options = pd.read_csv(FOLDER / "data" / "policy_options.csv")
    evaluated = evaluate_policies(options)

    assert not bool(evaluated.loc[evaluated.policy_id == "P3", "feasible"].iloc[0])
    assert make_decision_brief(options).loc[0, "policy_id"] != "P3"
