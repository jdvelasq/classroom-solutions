import logging
from pathlib import Path

import pandas as pd


ACTIVITY_DIR = Path(__file__).resolve().parents[1]


def main() -> None:
    # Un archivo de log conserva los eventos de una ejecución para investigarlos después.

    submission_dir = ACTIVITY_DIR / "submission"
    log_path = submission_dir / "pipeline.log"

    logging.basicConfig(
        filename=log_path,
        filemode="w",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        force=True,
    )

    logger = logging.getLogger(__name__)
    logger.info("pipeline_started")

    # La carga registra fuente y volumen porque ambos ayudan a explicar un resultado inesperado.

    data_path = ACTIVITY_DIR / "data" / "machine_throughput_export.csv"
    dataframe = pd.read_csv(data_path)
    logger.info("input_loaded source=%s rows=%s", data_path.name, len(dataframe))

    total_units = dataframe["daily_units_produced"].sum()
    # El evento final permite distinguir una ejecución completa de una interrumpida.

    logger.info("production_calculated total_units=%s", total_units)
    logger.info("pipeline_completed")

    print(f"Log generado: {log_path.name}")


if __name__ == "__main__":
    main()
