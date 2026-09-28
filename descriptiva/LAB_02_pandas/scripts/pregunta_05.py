import pandas as pd
from pathlib import Path


def pregunta_05():
    """
    Usando `data/tbl0.tsv`, encuentre el valor máximo de la columna `c2` para
    cada categoría de la columna `c1`. Retorne una Serie de Pandas cuyo índice
    son las categorías, en orden alfabético, y cuyos valores son los máximos.

    Ejemplo del formato de la respuesta:

        c1
        A    9
        B    9
        C    9
        ...
    """

    path = Path(__file__).resolve().parents[1] / "data" / "tbl0.tsv"
    table = pd.read_csv(path, sep="\t")
    result = table.groupby("c1")["c2"].max()
    result.name = None
    return result
