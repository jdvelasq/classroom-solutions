import os

FOLDER = "PRE_16_credit_campaign_targeting"
OUTPUT_FOLDER = f"{FOLDER}/submission"


def test_01():

    assert os.path.exists(f"{OUTPUT_FOLDER}/targeting_decisions.csv")
    assert os.path.exists(f"{OUTPUT_FOLDER}/policy_comparison.csv")
    assert os.path.exists(f"{OUTPUT_FOLDER}/capacity_sensitivity.csv")
    assert os.path.exists(f"{OUTPUT_FOLDER}/credit_campaign_targeting_planner.png")
