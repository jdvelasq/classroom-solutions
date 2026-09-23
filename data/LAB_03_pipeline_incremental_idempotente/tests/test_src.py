"""Validación de idempotencia y estado vigente."""

from ..src.main import main


def test_keeps_one_latest_version_per_transaction():
    current, report = main()
    assert len(current) == 21
    assert current.operation_id.is_unique
    assert report["row_count"] == report["unique_operations"] == 21


def test_reexecution_is_idempotent():
    first, _ = main()
    second, _ = main()
    assert first.to_csv(index=False) == second.to_csv(index=False)
