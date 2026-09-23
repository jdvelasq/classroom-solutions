"""Pruebas del laboratorio de cohortes de clientes."""

from pathlib import Path

import matplotlib.image as mpimg
import pandas as pd
import pytest

from ..src.pregunta_01 import build_cohort_analysis


ACTIVITY_DIR = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ACTIVITY_DIR / "submission"


def test_generates_the_table_and_heatmap():
    """Genera la evidencia tabular y visual requerida."""
    build_cohort_analysis()

    table = SUBMISSION_DIR / "cohort_retention.csv"
    heatmap = SUBMISSION_DIR / "cohort_retention_heatmap.png"
    assert table.exists()
    assert heatmap.exists()
    assert mpimg.imread(heatmap).size > 0


def test_retention_table_has_the_correct_grain_and_columns():
    """Entrega una fila por cohorte y meses desde adquisición observados."""
    retention = pd.read_csv(SUBMISSION_DIR / "cohort_retention.csv")

    assert retention.columns.tolist() == [
        "cohort_month",
        "period_index",
        "active_customers",
        "cohort_size",
        "retention_rate",
    ]
    assert retention.shape == (36, 5)
    assert retention["cohort_month"].nunique() == 8
    assert retention["period_index"].min() == 0
    assert retention["period_index"].max() == 7


def test_cohort_sizes_and_first_month_retention_are_correct():
    """Establece el tamaño inicial de cada cohorte y su retención del 100 %."""
    retention = pd.read_csv(SUBMISSION_DIR / "cohort_retention.csv")
    initial = retention[retention["period_index"].eq(0)]

    assert initial["cohort_month"].tolist() == [
        "2022-01",
        "2022-02",
        "2022-03",
        "2022-04",
        "2022-05",
        "2022-06",
        "2022-07",
        "2022-08",
    ]
    assert initial["cohort_size"].tolist() == [100, 76, 70, 57, 46, 29, 23, 27]
    assert initial["retention_rate"].tolist() == pytest.approx([1.0] * 8)


def test_retention_rates_measure_active_customers_over_cohort_size():
    """Calcula la tasa de retención con el denominador de la cohorte original."""
    retention = pd.read_csv(SUBMISSION_DIR / "cohort_retention.csv")

    january_month_1 = retention.loc[
        retention["cohort_month"].eq("2022-01") & retention["period_index"].eq(1)
    ].iloc[0]
    june_month_1 = retention.loc[
        retention["cohort_month"].eq("2022-06") & retention["period_index"].eq(1)
    ].iloc[0]

    assert january_month_1["active_customers"] == 26
    assert january_month_1["retention_rate"] == pytest.approx(0.26)
    assert june_month_1["active_customers"] == 2
    assert june_month_1["retention_rate"] == pytest.approx(2 / 29)
    assert retention["retention_rate"].between(0, 1).all()
