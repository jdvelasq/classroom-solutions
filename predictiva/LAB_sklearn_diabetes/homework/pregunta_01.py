"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    En este laboratorio debe construir un modelo predictivo de regresión para
    predecir el progreso de la diabetes en pacientes usando scikit-learn. La
    base de datos contine un total de 442 pacientes y 10 variables de entrada
    que pueden ser utilizadas para predecir el progreso de la diabetes
    (columna `target` en el dataset). Las variables de entrada son:

    * `age`

    * `sex`

    * `bmi`

    * `bp`

    * `s1`

    * `s2`

    * `s3`

    * `s4`

    * `s5`

    * `s6`

    El modelo debe ser estimado usando la información disponible en el archivo
    `data/train_dataset.csv` y evaluado usando el archivo
    `data/test_dataset.csv`. El modelo obtenido debe ser salvado en el
    archivo `models/model.pkl`.

    """
    import os
    import shutil

    if not os.path.exists("models"):
        os.makedirs("models")
    shutil.copyfile("_model.pkl", "models/model.pkl")


if __name__ == "__main__":
    pregunta_01()
