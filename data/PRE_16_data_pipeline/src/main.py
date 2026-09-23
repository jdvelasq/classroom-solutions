"""Pipeline docente: fuentes operativas de fábrica hasta una tabla analítica curada."""

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).parents[1]
DATA = ROOT / "data"
TEMP = ROOT / "temp" / "pipeline"
SUBMISSION = ROOT / "submission"


def extract():
    """Lee las fuentes sin modificar y conserva una copia reproducible en raw."""
    raw = TEMP / "raw"
    raw.mkdir(parents=True, exist_ok=True)
    sources = {
        "throughput": "machine_throughput_export.csv",
        "uptime": "machine_uptime_export.csv",
        "ambient": "factory_ambient_export.csv",
    }
    frames = {name: pd.read_csv(DATA / filename) for name, filename in sources.items()}
    for name, frame in frames.items():
        frame.to_csv(raw / f"{name}.csv", index=False)
    return frames


def transform(frames):
    """Integra las fuentes a grano fábrica-día y verifica las llaves de unión."""
    machine_day = frames["throughput"].merge(
        frames["uptime"],
        on=["factory_id", "machine_id", "factory_date"],
        validate="one_to_one",
    )
    factory_day = (
        machine_day.groupby(["factory_id", "factory_date"], as_index=False)
        .agg(
            units_produced=("daily_units_produced", "sum"),
            average_hours_operational=("hours_operational", "mean"),
            machines_reported=("machine_id", "nunique"),
        )
        .merge(
            frames["ambient"],
            left_on=["factory_id", "factory_date"],
            right_on=["factory_id", "date_measured"],
            validate="one_to_one",
        )
        .drop(columns="date_measured")
    )
    factory_day["factory_date"] = pd.to_datetime(factory_day["factory_date"])
    factory_day["average_hours_operational"] = factory_day[
        "average_hours_operational"
    ].round(2)
    assert factory_day[["factory_id", "factory_date"]].duplicated().sum() == 0
    assert factory_day.notna().all().all()
    return factory_day.sort_values(["factory_id", "factory_date"])


def publish(curated, frames):
    """Publica una tabla apta para Analytics y evidencia mínima de cada etapa."""
    staging = TEMP / "staging"
    curated_path = TEMP / "curated"
    staging.mkdir(parents=True, exist_ok=True)
    curated_path.mkdir(parents=True, exist_ok=True)
    curated.to_csv(staging / "factory_daily.csv", index=False)
    curated.to_csv(curated_path / "factory_daily.csv", index=False)
    curated.to_csv(SUBMISSION / "factory_daily.csv", index=False)
    report = pd.DataFrame(
        [
            ("raw", sum(len(frame) for frame in frames.values()), "SUCCESS"),
            ("staging", len(curated), "SUCCESS"),
            ("curated", len(curated), "SUCCESS"),
        ],
        columns=["stage", "rows", "status"],
    )
    report.to_csv(SUBMISSION / "pipeline_report.csv", index=False)


def build_submission():
    """Ejecuta las tres capas del pipeline de principio a fin."""
    SUBMISSION.mkdir(exist_ok=True)
    frames = extract()
    curated = transform(frames)
    publish(curated, frames)


if __name__ == "__main__":
    build_submission()
