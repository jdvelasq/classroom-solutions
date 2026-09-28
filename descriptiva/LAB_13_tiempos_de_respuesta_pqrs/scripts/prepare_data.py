from pathlib import Path

import pandas as pd

SOURCE_URL = (
    "https://raw.githubusercontent.com/jdvelasq/datalabs/master/"
    "datasets/pqrs/historical_requests_{channel}.csv"
)
CHANNELS = ["web", "letter"]


def prepare_data():
    """
    Genera `data/historical_requests_web.csv.gz` y
    `data/historical_requests_letter.csv.gz` a partir de los archivos de
    datalabs. Reemplaza `record_id` por un código corto para reducir el tamaño
    del archivo, conservando las filas repetidas y los identificadores
    faltantes.
    """

    root = Path(__file__).resolve().parents[1]
    requests = {
        channel: pd.read_csv(SOURCE_URL.format(channel=channel)) for channel in CHANNELS
    }
    record_ids = pd.concat([requests[channel]["record_id"] for channel in CHANNELS])
    codes = {
        record_id: f"R{number:06d}"
        for number, record_id in enumerate(record_ids.dropna().unique(), start=1)
    }
    for channel, data in requests.items():
        data["record_id"] = data["record_id"].map(codes)
        data.to_csv(
            root / "data" / f"historical_requests_{channel}.csv.gz",
            index=False,
            compression={"method": "gzip", "mtime": 0},
        )


if __name__ == "__main__":
    prepare_data()
