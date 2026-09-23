from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def simulate_project(parameters: pd.Series, n_simulations: int = 10_000) -> pd.DataFrame:
    rng = np.random.default_rng(20260923)
    years = np.arange(1, int(parameters.years) + 1)
    revenue_factor = rng.lognormal(-0.5 * parameters.revenue_sigma**2, parameters.revenue_sigma, (n_simulations, len(years)))
    margin_factor = np.clip(rng.normal(1, parameters.margin_sigma, (n_simulations, len(years))), 0.7, 1.3)
    revenues = parameters.base_revenue * revenue_factor
    cashflows = revenues * (1 - parameters.variable_cost_rate * margin_factor) - parameters.fixed_cost
    npv = -parameters.initial_investment + (cashflows / (1 + parameters.discount_rate) ** years).sum(axis=1)
    return pd.DataFrame({"simulation_id": np.arange(1, n_simulations + 1), "npv": npv})


def summarize_risk(simulations: pd.DataFrame) -> pd.DataFrame:
    loss_probability = (simulations.npv < 0).mean()
    mean_npv = simulations.npv.mean()
    recommendation = "financiar" if mean_npv > 0 and loss_probability <= 0.35 else "no_financiar"
    return pd.DataFrame([{
        "policy": "financiar_proyecto",
        "mean_npv": mean_npv,
        "p10_npv": simulations.npv.quantile(0.10),
        "loss_probability": loss_probability,
        "recommendation": recommendation,
        "review_trigger": "Escalar si la probabilidad de pérdida supera 35%.",
    }])


def main() -> None:
    parameters = pd.read_csv(ROOT / "data" / "project_parameters.csv").iloc[0]
    summarize_risk(simulate_project(parameters)).to_csv(ROOT / "submission" / "project_risk_summary.csv", index=False)


if __name__ == "__main__":
    main()
