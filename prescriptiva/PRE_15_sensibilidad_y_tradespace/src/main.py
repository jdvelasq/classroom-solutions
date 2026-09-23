from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
CUSTOMER_VALUE = 260


def evaluate(options):
    result = options.copy()
    result["retained_value"] = result.monthly_customers * result.retention_gain * CUSTOMER_VALUE
    result["net_value"] = result.retained_value - result.monthly_cost
    return result


def main():
    evaluate(pd.read_csv(ROOT / "data" / "service_options.csv")).to_csv(ROOT / "submission" / "tradespace.csv", index=False)


if __name__ == "__main__": main()
