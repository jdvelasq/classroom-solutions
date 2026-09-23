"""Verificaciones de indicadores de cumplimiento de entregas."""

import json

import pandas as pd
import pytest


DATA_FILE = "data/supply_chain.csv"
NOTEBOOK_FILE = "notebooks/notebook.ipynb"


def prepare_shipments():
    """Reconstruye las métricas operativas usadas en el taller."""
    shipments = pd.read_csv(DATA_FILE)
    for column in ["Scheduled Delivery Date", "Delivered to Client Date"]:
        shipments[column] = pd.to_datetime(shipments[column], format="%d-%b-%y")
    shipments["DeliveryDaysVsSchedule"] = (
        shipments["Delivered to Client Date"] - shipments["Scheduled Delivery Date"]
    ).dt.days
    shipments["IsLate"] = shipments["DeliveryDaysVsSchedule"] > 0
    return shipments


def test_01_compliance_kpis_reconcile_with_the_delivered_shipments():
    """El riesgo económico se calcula solamente con los envíos tardíos."""
    shipments = prepare_shipments()

    assert shipments["ID"].size == 10_324
    assert (1 - shipments["IsLate"].mean()) == pytest.approx(0.8851220457)
    assert shipments["DeliveryDaysVsSchedule"].median() == 0
    assert shipments.loc[shipments["IsLate"], "Line Item Value"].sum() == pytest.approx(
        259_034_270.94
    )


def test_02_priority_segments_keep_a_minimum_operational_volume():
    """Los segmentos se comparan solo si contienen al menos 30 envíos."""
    shipments = prepare_shipments()
    segments = (
        shipments.groupby(["Country", "Shipment Mode"], dropna=False)
        .agg(
            shipments=("ID", "size"),
            on_time=("IsLate", lambda value: 1 - value.mean()),
            late_value=(
                "Line Item Value",
                lambda value: value[shipments.loc[value.index, "IsLate"]].sum(),
            ),
        )
        .reset_index()
        .query("shipments >= 30")
    )

    assert not segments.empty
    assert segments["shipments"].ge(30).all()
    assert segments["late_value"].max() > 0


def test_03_notebook_distinguishes_compliance_from_cost_coverage():
    """El caso trata cumplimiento, riesgo económico y calidad de costos."""
    notebook = json.loads(open(NOTEBOOK_FILE, encoding="utf-8").read())
    source = "\n".join(
        "".join(cell["source"])
        for cell in notebook["cells"]
        if cell["cell_type"] == "code"
    )

    for concept in [
        "cumplimiento_a_tiempo",
        "valor_enviado_tarde_usd",
        "minimum_shipments = 50",
        "cobertura_valor_con_flete",
    ]:
        assert concept in source
