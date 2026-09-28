from pathlib import Path

import pandas as pd

TEXT_COLUMNS = [
    "sexo",
    "tipo_de_emprendimiento",
    "idea_negocio",
    "barrio",
    "línea_credito",
]


def pregunta_01():
    """
    Escribe la respuesta conocida: el archivo limpio del que se generaron los
    datos de los estudiantes, con el texto normalizado y sin duplicados.
    """

    root = Path(__file__).resolve().parents[1]
    clean = pd.read_csv(root / "scripts" / "SOLICITUDES_DE_CREDITO.csv", sep=";")
    for column in TEXT_COLUMNS:
        clean[column] = (
            clean[column]
            .str.lower()
            .str.replace("-", " ", regex=False)
            .str.replace("_", " ", regex=False)
            .str.strip()
        )
    clean = clean.drop_duplicates()

    submission_dir = root / "submission"
    submission_dir.mkdir(exist_ok=True)
    clean.to_csv(submission_dir / "solicitudes_de_credito.csv", sep=";", index=False)

    return clean
