from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def apply_review_policy(applications: pd.DataFrame) -> pd.DataFrame:
    result = applications.copy()
    result["action"] = "revisión_humana"
    result.loc[
        (result.default_probability < 0.08) & result.documentation_complete,
        "action",
    ] = "aprobar_recomendación"
    result.loc[
        (result.default_probability > 0.30) & result.documentation_complete,
        "action",
    ] = "rechazar_recomendación"
    result["reason"] = "incertidumbre, monto alto o documentación incompleta"
    result.loc[result.action == "aprobar_recomendación", "reason"] = "riesgo bajo y documentación completa"
    result.loc[result.action == "rechazar_recomendación", "reason"] = "riesgo alto y documentación completa"
    result["human_owner"] = "Analista de crédito" 
    return result


def main() -> None:
    applications = pd.read_csv(ROOT / "data" / "applications.csv")
    apply_review_policy(applications).to_csv(ROOT / "submission" / "review_policy.csv", index=False)


if __name__ == "__main__":
    main()
