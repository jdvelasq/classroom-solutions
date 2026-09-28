from pathlib import Path

import pandas as pd


def generate_dirty_data():
    """Genera `data/solicitudes_de_credito.csv.gz` a partir del archivo limpio."""

    root = Path(__file__).resolve().parents[1]
    clean_file = root / "scripts" / "SOLICITUDES_DE_CREDITO.csv"
    dirty_file = root / "data" / "solicitudes_de_credito.csv.gz"
    clean = pd.read_csv(clean_file, sep=";")

    missing_type = clean.sample(n=110, random_state=11).copy()
    missing_type["tipo_de_emprendimiento"] = pd.NA
    missing_neighborhood = clean.sample(n=110, random_state=12).copy()
    missing_neighborhood["barrio"] = pd.NA
    duplicated = clean.sample(n=520, random_state=13).copy()
    dirty = pd.concat(
        [clean, duplicated, missing_type, missing_neighborhood],
        ignore_index=True,
    )

    for column, random_state in {
        "sexo": 21,
        "tipo_de_emprendimiento": 22,
        "idea_negocio": 23,
        "barrio": 24,
        "línea_credito": 25,
    }.items():
        indexes = dirty.sample(n=240, random_state=random_state).index
        dirty.loc[indexes, column] = dirty.loc[indexes, column].str.upper()
        indexes = dirty.sample(n=240, random_state=random_state + 100).index
        dirty.loc[indexes, column] = dirty.loc[indexes, column].str.replace(
            " ", "-", regex=False
        )

    dirty["estrato"] = dirty["estrato"].astype("string")
    indexes = dirty.sample(n=420, random_state=31).index
    dirty.loc[indexes, "estrato"] = dirty.loc[indexes, "estrato"].map(
        lambda value: f"0{value}"
    )
    indexes = dirty.sample(n=700, random_state=32).index
    dirty.loc[indexes, "fecha_de_beneficio"] = dirty.loc[
        indexes, "fecha_de_beneficio"
    ].map(lambda value: pd.to_datetime(value, dayfirst=True).strftime("%Y/%m/%d"))
    dirty["monto_del_credito"] = dirty["monto_del_credito"].astype("string")
    indexes = dirty.sample(n=480, random_state=33).index
    dirty.loc[indexes, "monto_del_credito"] = dirty.loc[
        indexes, "monto_del_credito"
    ].map(lambda value: f"$ {float(value):,.2f}")

    dirty = dirty.sample(frac=1, random_state=99).reset_index(drop=True)
    dirty.to_csv(
        dirty_file,
        sep=";",
        index=True,
        compression={"method": "gzip", "mtime": 0},
    )

    return dirty


if __name__ == "__main__":
    generate_dirty_data()
