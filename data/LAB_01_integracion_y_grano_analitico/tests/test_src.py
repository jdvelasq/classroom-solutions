"""Validación de integración y grano del laboratorio."""

from ..src.main import main


def test_preserves_customer_month_grain_and_amounts():
    result, report = main()
    assert len(result) > 1000
    assert report["source_units"] == report["output_units"]
    assert report["grain"] == "factory_id,factory_date"
    assert not result.duplicated(["factory_id", "factory_date"]).any()
