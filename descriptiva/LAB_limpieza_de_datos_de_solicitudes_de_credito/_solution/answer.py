"""
Escriba el codigo que ejecute la accion solicitada en la pregunta. Los
archivos requeridos se encuentran en la carpeta data/.
"""

import os

import pandas as pd  # type: ignore


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    """
    if not os.path.exists("files/output/"):
        os.makedirs("files/output/", exist_ok=True)

    df = pd.read_csv("_solicitudes_de_credito.csv", sep=";")
    df = df.drop_duplicates()
    df = df.dropna()
    df.to_csv("files/output/solicitudes_de_credito.csv", sep=";", index=False)
