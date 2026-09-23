"""Pruebas automáticas de la solución del dashboard analítico."""

import pandas as pd
import pytest

from ..src.pregunta_01 import (
    DATA_FILE,
    SUMMARY_FILE,
    calculate_kpis,
    create_source_summary,
    filter_campaign_data,
    load_campaign_data,
    summarize_by_campaign,
    summarize_by_day,
    summarize_by_source,
)


def test_01_loads_the_campaign_data_and_calculates_profit():
    data = load_campaign_data(DATA_FILE)

    assert data.shape[0] == 1096
    assert pd.api.types.is_datetime64_any_dtype(data["utc_date"])
    assert (data["gross_profit"] == data["revenue"] - data["ad_spend"]).all()


def test_02_filters_the_active_population_without_changing_the_input():
    data = load_campaign_data(DATA_FILE)
    filtered = filter_campaign_data(
        data, "2020-01-01", "2020-01-31", ["TikTok Ads"], ["United Kingdom"]
    )

    assert not filtered.empty
    assert filtered["utc_date"].between("2020-01-01", "2020-01-31").all()
    assert filtered["traffic_source"].eq("TikTok Ads").all()
    assert filtered["country"].eq("United Kingdom").all()
    assert data.shape[0] == 1096


def test_03_recalculates_ratios_from_the_filtered_totals():
    kpis = calculate_kpis(
        pd.DataFrame({
            "impressions": [100, 200], "paid_clicks": [10, 30],
            "revenue": [100.0, 300.0], "ad_spend": [20.0, 60.0],
        })
    )

    assert kpis == {
        "impressions": 300, "paid_clicks": 40, "revenue": 400.0,
        "ad_spend": 80.0, "gross_profit": 320.0, "roas": 5.0, "cpc": 2.0,
    }


def test_04_all_summaries_reconcile_with_the_active_population():
    data = load_campaign_data(DATA_FILE)
    filtered = filter_campaign_data(
        data, "2021-01-01", "2021-12-31", ["Facebook Ads", "LinkedIn Ads"],
        ["Canada", "United States"],
    )
    profit = calculate_kpis(filtered)["gross_profit"]

    assert summarize_by_day(filtered)["gross_profit"].sum() == pytest.approx(profit)
    assert summarize_by_source(filtered)["gross_profit"].sum() == pytest.approx(profit)
    assert summarize_by_campaign(filtered)["gross_profit"].sum() == pytest.approx(profit)


def test_05_creates_the_required_source_summary_in_submission():
    summary = create_source_summary()
    saved_summary = pd.read_csv(SUMMARY_FILE)

    assert SUMMARY_FILE.exists()
    assert set(saved_summary.columns) == {
        "traffic_source", "impressions", "paid_clicks", "revenue", "ad_spend",
        "gross_profit", "roas", "cpc",
    }
    assert saved_summary["gross_profit"].sum() == pytest.approx(summary["gross_profit"].sum())
