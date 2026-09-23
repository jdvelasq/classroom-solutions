"""Validación de tiempo de evento y tardanza."""

from ..src.main import main


def test_uses_event_time_and_identifies_late_events():
    metrics, late, report = main()
    assert metrics.events.tolist() == [2, 2]
    assert late.event_id.tolist() == ["E04"]
    assert report == {"allowed_lateness_minutes": 15, "late_event_count": 1, "accepted_event_count": 4, "event_count": 5}
