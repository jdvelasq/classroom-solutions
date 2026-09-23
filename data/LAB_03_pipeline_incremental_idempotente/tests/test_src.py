"""Validación de idempotencia y estado vigente."""

from ..src.main import main


def test_keeps_one_latest_version_per_transaction():
    current, report = main()
    assert current.transaction_id.tolist() == ["T01", "T02", "T03", "T04"]
    assert current.loc[current.transaction_id == "T02", "amount"].iloc[0] == 85
    assert report == {"row_count": 4, "total_amount": 345.0, "unique_transactions": 4}


def test_reexecution_is_idempotent():
    first, _ = main()
    second, _ = main()
    assert first.to_csv(index=False) == second.to_csv(index=False)
