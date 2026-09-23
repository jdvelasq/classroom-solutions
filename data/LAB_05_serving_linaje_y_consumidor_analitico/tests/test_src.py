"""Validación del activo de serving y su linaje."""

from ..src.main import main


def test_serves_the_requested_grain_with_lineage():
    view, manifest, lineage = main()
    assert len(view) == 4
    assert view.amount.sum() == 500
    assert manifest["grain"] == "sale_date,region"
    assert lineage.target.tolist()[-1] == "sales_serving_view"
