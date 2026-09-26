"""Verificaciones del taller de gobierno de KPI."""

import nbformat
import pandas as pd


def test_kpi_governance_artifacts_are_publishable():
    catalog = pd.read_csv("submission/kpi_catalog.csv")
    checks = pd.read_csv("submission/kpi_quality_report.csv")
    decision = pd.read_csv("submission/kpi_publication_decision.csv")

    assert catalog.shape[0] == 3
    assert {"grano", "propietario", "fuente"}.issubset(catalog.columns)
    assert checks["estado"].eq("PASS").all()
    assert decision.loc[0, "estado"] == "APROBADO"


def test_notebook_keeps_definition_quality_and_lineage_together():
    notebook = nbformat.read("notebooks/notebook.ipynb", as_version=4)
    source = "\n".join(cell.source for cell in notebook.cells)

    for concept in ["kpi_catalog", "quality_checks", "metric_lineage"]:
        assert concept in source
