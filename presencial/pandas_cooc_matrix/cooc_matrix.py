"""Taller Presencial Evaluable"""

import pandas as pd

#
# Lea el archivo 
dataframe = pd.read_csv(
    "input.txt",
    header=None,
    delimiter="\t",
    names=["line"],
    index_col=None,
)
