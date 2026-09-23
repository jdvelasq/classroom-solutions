"""Validación del activo de serving y su linaje."""

from ..src.main import main


def test_serves_the_requested_grain_with_lineage():
    view, manifest, lineage = main()
    assert len(view) > 1000
    assert view.daily_units_produced.sum() > 0
    assert manifest["grain"] == "factory_date,factory_id"
    assert lineage.target.tolist()[-1] == "factory_daily_serving_view"
    assert lineage.loc[lineage.target == "factory_daily_serving_view", "source"].iloc[0] == manifest["source_asset"]
