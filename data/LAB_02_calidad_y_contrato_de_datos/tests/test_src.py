"""Validación del laboratorio de calidad y contrato."""

from ..src.main import main


def test_quarantines_invalid_and_duplicate_records():
    report = main()
    assert report["input_rows"] == 42
    assert report["accepted_rows"] == 39
    assert report["quarantined_rows"] == 3
    assert report["reasons"] == {"invalid_state": 0, "invalid_income_group": 1, "duplicate_postal_income_key": 2, "negative_return_count": 1}
