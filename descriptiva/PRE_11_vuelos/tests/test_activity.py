"""Verificaciones del agregado simplificado usado en el taller de vuelos."""

import pandas as pd
import pytest


DAY_HOUR_FILE = "data/flights_by_carrier_day_hour.csv.gz"
MONTHLY_FILE = "data/flights_by_carrier_month.csv.gz"
MEASURES = [
    "scheduled_flights",
    "cancelled_flights",
    "operated_flights",
    "delayed_departure_15_flights",
    "positive_departure_delay_minutes",
]


def test_01_day_hour_aggregate_reconciles_to_the_monthly_dataset():
    """El análisis por segmento debe reconciliarse con el total mensual."""
    day_hour = pd.read_csv(DAY_HOUR_FILE)
    monthly = pd.read_csv(MONTHLY_FILE)

    rebuilt_monthly = (
        day_hour.groupby(["year", "month", "reporting_airline"], as_index=False)[
            MEASURES
        ]
        .sum()
        .sort_values(["year", "month", "reporting_airline"])
        .reset_index(drop=True)
    )
    expected_monthly = monthly.sort_values(
        ["year", "month", "reporting_airline"]
    ).reset_index(drop=True)

    pd.testing.assert_frame_equal(rebuilt_monthly, expected_monthly)


def test_02_operational_kpis_use_the_correct_denominators():
    """Las tasas de cancelación y demora se calculan sobre vuelos comparables."""
    monthly = pd.read_csv(MONTHLY_FILE)
    totals = monthly[MEASURES].sum()

    cancellation_rate = totals["cancelled_flights"] / totals["scheduled_flights"]
    delay_rate = totals["delayed_departure_15_flights"] / totals["operated_flights"]
    mean_positive_delay = (
        totals["positive_departure_delay_minutes"] / totals["operated_flights"]
    )

    assert cancellation_rate == pytest.approx(0.0194461489)
    assert delay_rate == pytest.approx(0.2041330573)
    assert mean_positive_delay == pytest.approx(12.7886029364)
