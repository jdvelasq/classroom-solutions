"""Validación de integración y grano del laboratorio."""

from ..src.main import main


def test_preserves_customer_month_grain_and_amounts():
    result, report = main()
    assert len(result) == 3
    assert result.amount.sum() == 450
    assert report["source_amount"] == report["output_amount"] == 450
    assert report["grain"] == "customer_id,month"
    assert not result.duplicated(["customer_id", "month"]).any()
