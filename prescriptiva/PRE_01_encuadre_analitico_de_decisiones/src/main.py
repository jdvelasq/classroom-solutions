"""Compara políticas de contacto; no construye ni despliega un producto."""

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def evaluate_policies(options: pd.DataFrame) -> pd.DataFrame:
    """Calcula valor esperado y factibilidad de alternativas ya definidas."""
    result = options.copy()
    result["expected_conversions"] = result.contacts * result.expected_conversion
    result["expected_net_value"] = (
        result.expected_conversions * result.net_value_per_conversion
        - result.contacts * result.contact_cost
    )
    result["capacity_ok"] = result.contacts <= result.capacity_limit
    result["exposure_ok"] = result.high_contact_share <= result.max_high_contact_share
    result["feasible"] = result.capacity_ok & result.exposure_ok
    return result


def make_decision_brief(options: pd.DataFrame) -> pd.DataFrame:
    """Escoge la mejor alternativa factible y hace visibles sus supuestos."""
    evaluated = evaluate_policies(options)
    recommendation = evaluated.loc[evaluated.feasible].nlargest(1, "expected_net_value")
    brief = recommendation.loc[
        :, [
            "policy_id",
            "policy",
            "contacts",
            "expected_conversions",
            "expected_net_value",
            "capacity_ok",
            "exposure_ok",
        ]
    ].copy().reset_index(drop=True)
    brief["decision_owner"] = "Responsable comercial"
    brief["review_trigger"] = "Revisar si la conversión observada cae por debajo de 10%."
    return brief


def main() -> None:
    options = pd.read_csv(ROOT / "data" / "policy_options.csv")
    brief = make_decision_brief(options)
    brief.to_csv(ROOT / "submission" / "decision_brief.csv", index=False)


if __name__ == "__main__":
    main()
