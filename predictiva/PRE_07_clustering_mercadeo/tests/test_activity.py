import os

import pandas as pd

def test_homework():
    """Test the homework."""

    assert os.path.exists("submission/segmented.csv")

    df = pd.read_csv("submission/segmented.csv", index_col=0)

    assert df.shape[0] > 0
    assert df.shape[1] > 0
