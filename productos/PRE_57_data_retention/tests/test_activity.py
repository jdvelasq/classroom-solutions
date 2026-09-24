"""Verifica que la política de retención conserve y expire los registros correctos."""

import sys
from datetime import date
from pathlib import Path


PRE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PRE_DIR))

from src.main import apply_retention_policy


def test_retention_policy_preserves_recent_events_and_evidence():
    """La purga lógica debe preservar el dato vigente y evidenciar qué quedó vencido."""

    result = apply_retention_policy(date(2026, 9, 1))

    assert result["cutoff"] == "2026-06-03"
    assert [event["event_id"] for event in result["retained"]] == ["evt-001"]
    assert result["expired"] == [
        {"event_id": "evt-002", "reason": "retention_period_expired"},
        {"event_id": "evt-003", "reason": "retention_period_expired"},
    ]
