import os

FOLDER = "PRE_10_wildfire_resource_positioning"
OUTPUT_FOLDER = f"{FOLDER}/submission"


def test_01():

    assert os.path.exists(f"{OUTPUT_FOLDER}/deployment_decisions.csv")
    assert os.path.exists(f"{OUTPUT_FOLDER}/zone_assignments.csv")
    assert os.path.exists(f"{OUTPUT_FOLDER}/resource_sensitivity.csv")
    assert os.path.exists(f"{OUTPUT_FOLDER}/wildfire_resource_deployment_map.png")
