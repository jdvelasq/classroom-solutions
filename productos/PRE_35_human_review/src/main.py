"""Registra una revisión humana antes de ejecutar una recomendación sensible."""

import json
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]


def review_recommendation(decision):
    """La decisión humana conserva responsabilidad sobre la acción operacional."""

    recommendation = json.loads((ROOT_DIR / "data" / "recommendation.json").read_text())
    return {"recommendation": recommendation, "human_decision": decision, "action_authorized": decision == "approve"}


if __name__ == "__main__":
    (ROOT_DIR / "submission" / "review.json").write_text(json.dumps(review_recommendation("approve")))
