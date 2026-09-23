"""Validación de tiempo de evento y tardanza."""

from ..src.main import main


def test_uses_event_time_and_identifies_late_events():
    metrics, late, report = main()
    assert metrics.events.sum() == 56
    assert len(late) == 4
    assert report == {"allowed_lateness_minutes": 15, "late_event_count": 4, "accepted_event_count": 56, "event_count": 60}
