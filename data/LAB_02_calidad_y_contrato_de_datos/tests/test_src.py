"""Validación del laboratorio de calidad y contrato."""

from ..src.main import main


def test_quarantines_invalid_and_duplicate_records():
    report = main()
    assert report["input_rows"] == 6
    assert report["accepted_rows"] == 1
    assert report["quarantined_rows"] == 5
    assert report["reasons"] == {"duplicate_customer_id": 2, "missing_age": 1, "invalid_age": 1, "invalid_segment": 1}
