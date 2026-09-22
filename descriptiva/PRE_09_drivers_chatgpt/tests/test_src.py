import os

FOLDER = "PRE_09_drivers_chatgpt"


def test_01():

    assert os.path.exists(f"{FOLDER}/submission/summary.csv")
    assert os.path.exists(f"{FOLDER}/submission/top10_drivers.png")
