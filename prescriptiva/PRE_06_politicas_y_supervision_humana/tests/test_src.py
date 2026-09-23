"""Las pruebas se implementarán junto con la solución del taller."""
from pathlib import Path
import sys
import pandas as pd

FOLDER = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FOLDER / "src"))
from solution import apply_review_policy


def test_policy_preserves_human_review_for_ambiguous_cases():
    output = apply_review_policy(pd.read_csv(FOLDER / "data" / "applications.csv"))
    assert output.loc[output.application_id == "A02", "action"].iloc[0] == "revisión_humana"
    assert output.loc[output.application_id == "A05", "action"].iloc[0] == "revisión_humana"
    assert output.human_owner.eq("Analista de crédito").all()


def test_clear_recommendations_have_explicit_reasons():
    output = apply_review_policy(pd.read_csv(FOLDER / "data" / "applications.csv"))
    assert output.loc[output.application_id == "A01", "action"].iloc[0] == "aprobar_recomendación"
    assert output.loc[output.application_id == "A04", "action"].iloc[0] == "revisión_humana"
