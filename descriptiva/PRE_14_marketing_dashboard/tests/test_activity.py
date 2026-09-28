import pandas as pd
import pytest

from ..src.main import (
    DATA_FILE,
    calculate_kpis,
    filter_campaign_data,
    load_campaign_data,
    summarize_by_campaign,
    summarize_by_day,
    summarize_by_source,
)


def test_01_loads_the_campaign_data_and_recomputes_profit():
    data = load_campaign_data(DATA_FILE)

    assert data.shape[0] == 1096
    assert pd.api.types.is_datetime64_any_dtype(data["utc_date"])
    assert (data["gross_profit"] == data["revenue"] - data["ad_spend"]).all()


def test_02_filters_by_date_source_and_country_without_changing_the_input():
    data = load_campaign_data(DATA_FILE)
    filtered_data = filter_campaign_data(
        data,
        start_date="2020-01-01",
        end_date="2020-01-31",
        traffic_sources=["TikTok Ads"],
        countries=["United Kingdom"],
    )

    assert not filtered_data.empty
    assert filtered_data["utc_date"].between("2020-01-01", "2020-01-31").all()
    assert filtered_data["traffic_source"].eq("TikTok Ads").all()
    assert filtered_data["country"].eq("United Kingdom").all()
    assert data.shape[0] == 1096


def test_03_recalculates_ratios_from_filtered_totals():
    data = pd.DataFrame(
        {
            "impressions": [100, 200],
            "paid_clicks": [10, 30],
            "revenue": [100.0, 300.0],
            "ad_spend": [20.0, 60.0],
        }
    )

    kpis = calculate_kpis(data)

    assert kpis == {
        "impressions": 300,
        "paid_clicks": 40,
        "revenue": 400.0,
        "ad_spend": 80.0,
        "gross_profit": 320.0,
        "roas": 5.0,
        "cpc": 2.0,
    }


def test_04_handles_zero_denominators_without_infinite_ratios():
    data = pd.DataFrame(
        {
            "impressions": [0],
            "paid_clicks": [0],
            "revenue": [0.0],
            "ad_spend": [0.0],
        }
    )

    kpis = calculate_kpis(data)

    assert kpis["roas"] is None
    assert kpis["cpc"] is None


def test_05_summaries_reconcile_with_the_active_population():
    data = load_campaign_data(DATA_FILE)
    filtered_data = filter_campaign_data(
        data,
        start_date="2021-01-01",
        end_date="2021-12-31",
        traffic_sources=["Facebook Ads", "LinkedIn Ads"],
        countries=["Canada", "United States"],
    )
    kpis = calculate_kpis(filtered_data)

    assert summarize_by_day(filtered_data)["gross_profit"].sum() == pytest.approx(kpis["gross_profit"])
    assert summarize_by_source(filtered_data)["gross_profit"].sum() == pytest.approx(kpis["gross_profit"])
    assert summarize_by_campaign(filtered_data)["gross_profit"].sum() == pytest.approx(kpis["gross_profit"])
