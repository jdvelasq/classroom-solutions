"""Taller Presencial Evaluable"""

import pandas as pd

dataframe = pd.read_csv(
    "input.txt",
    header=None,
    delimiter="\t",
    names=["line"],
    index_col=None,
)
