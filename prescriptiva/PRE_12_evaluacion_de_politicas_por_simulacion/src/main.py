from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def evaluate(policies: pd.DataFrame, scenarios: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for policy in policies.itertuples(index=False):
        served = scenarios.demand.clip(upper=policy.capacity)
        service_rate = served / scenarios.demand
        expected_service = (service_rate * scenarios.probability).sum()
        breach_probability = scenarios.loc[service_rate < policy.service_target, "probability"].sum()
        rows.append({"policy_id": policy.policy_id, "policy": policy.policy,
                     "expected_service_rate": expected_service,
                     "breach_probability": breach_probability,
                     "daily_cost": policy.daily_cost,
                     "feasible": expected_service >= policy.service_target})
    return pd.DataFrame(rows)


def recommend(policies, scenarios):
    comparison = evaluate(policies, scenarios)
    return comparison.loc[comparison.feasible].nsmallest(1, "daily_cost").reset_index(drop=True)


def main():
    policies = pd.read_csv(ROOT / "data" / "capacity_policies.csv")
    scenarios = pd.read_csv(ROOT / "data" / "demand_scenarios.csv")
    evaluate(policies, scenarios).to_csv(ROOT / "submission" / "capacity_policy_comparison.csv", index=False)


if __name__ == "__main__":
    main()
