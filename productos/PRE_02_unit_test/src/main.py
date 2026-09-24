import csv
from pathlib import Path


ACTIVITY_DIR = Path(__file__).resolve().parents[1]


def summarize_by_factory(operations: list[dict]) -> list[dict]:
    totals = {}
    for operation in operations:
        factory_id = operation["factory_id"]
        totals[factory_id] = totals.get(factory_id, 0) + operation[
            "daily_units_produced"
        ]

    return [
        {"factory_id": factory_id, "total_units": totals[factory_id]}
        for factory_id in sorted(totals)
    ]


def load_operations(data_path: Path) -> list[dict]:
    with data_path.open(newline="", encoding="utf-8") as file:
        return [
            {
                "factory_id": int(row["factory_id"]),
                "machine_id": int(row["machine_id"]),
                "daily_units_produced": int(row["daily_units_produced"]),
            }
            for row in csv.DictReader(file)
        ]


def write_summary(summary: list[dict], output_path: Path) -> None:
    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["factory_id", "total_units"])
        writer.writeheader()
        writer.writerows(summary)


def main() -> None:
    operations = load_operations(ACTIVITY_DIR / "data" / "daily_operations.csv")
    summary = summarize_by_factory(operations)
    output_path = ACTIVITY_DIR / "submission" / "factory_totals.csv"

    write_summary(summary, output_path)
    print(f"Resumen generado: {output_path.name}")


if __name__ == "__main__":
    main()
