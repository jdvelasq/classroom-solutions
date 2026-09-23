import os

ESTIMATOR = "submission/estimator.pkl"


def test_01():

    assert os.path.exists(ESTIMATOR)
