from pathlib import Path

import pandas as pd


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
EXPECTED_COLUMNS = (
    "factory_id",
    "machine_id",
    "daily_units_produced",
    "factory_date",
)
BUSINESS_KEY = ("factory_id", "machine_id", "factory_date")


def validate_data(dataframe: pd.DataFrame) -> None:
    violations = []

    if tuple(dataframe.columns) != EXPECTED_COLUMNS:
        violations.append("El esquema no coincide con el contrato esperado.")
        raise ValueError("\n".join(violations))

    if not dataframe["factory_id"].gt(0).all():
        violations.append("factory_id debe contener valores positivos.")
    if not dataframe["machine_id"].gt(0).all():
        violations.append("machine_id debe contener valores positivos.")
    if not dataframe["daily_units_produced"].ge(0).all():
        violations.append("daily_units_produced no puede ser negativo.")
    if pd.to_datetime(dataframe["factory_date"], errors="coerce").isna().any():
        violations.append("factory_date debe contener fechas válidas.")
    if dataframe.duplicated(BUSINESS_KEY).any():
        violations.append("La llave factory_id-machine_id-factory_date está duplicada.")

    if violations:
        raise ValueError("\n".join(violations))


def main() -> None:
    data_path = ACTIVITY_DIR / "data" / "machine_throughput_export.csv"
    dataframe = pd.read_csv(data_path)

    validate_data(dataframe)

    print("Contrato de datos válido.")
    print(f"Filas validadas: {len(dataframe)}")


if __name__ == "__main__":
    main()
