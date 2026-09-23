import pandas as pd

from ..src.s05_countries_frequency_report import (
    FREQUENCY_REPORT_FILE,
    s05_countries_frequency_report,
)
from ..src.s08_countries_cooc_matrix import MATRIX_FILE, s08_countries_cooc_matrix
from ..src.s10_countries_clusters import CLUSTERS_FILE, s10_countries_clusters


def test_01_country_frequency_report_has_the_expected_reference_counts():
    """El reporte preserva la frecuencia de los países ya normalizados."""
    s05_countries_frequency_report()
    frequency = pd.read_csv(FREQUENCY_REPORT_FILE).set_index("item")

    assert frequency.loc["United States of America", "count"] == 75
    assert frequency.loc["United Kingdom", "count"] == 39
    assert frequency.loc["China", "count"] == 36
    assert frequency.loc["Australia", "count"] == 31
    assert frequency.loc["India", "count"] == 27


def test_02_collaboration_products_are_built_from_the_frequency_data():
    """Matriz y comunidades se generan como entregables del análisis."""
    s08_countries_cooc_matrix()
    s10_countries_clusters()

    matrix = pd.read_csv(MATRIX_FILE, index_col=0)
    assert matrix.equals(matrix.T)
    assert matrix.loc["United States of America", "China"] > 0
    assert CLUSTERS_FILE.read_text(encoding="utf-8").strip()


def test_03_network_source_uses_the_matrix_and_country_frequencies():
    """La visualización de red preserva las dos fuentes del análisis."""
    source = open("src/s11_countries_network.py", encoding="utf-8").read()

    assert "MATRIX_FILE" in source
    assert "FREQUENCY_REPORT_FILE" in source
    assert "NETWORK_FILE" in source
    assert "go.Scatter" in source
