import os

def test_01():

    assert os.path.exists("submission/metrics.csv")
    assert os.path.exists("submission/forecasts.csv")
