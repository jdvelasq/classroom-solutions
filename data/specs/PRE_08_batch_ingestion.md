# PRE Specification

## Identification

**Activity:** `PRE_08_batch_ingestion`

**Week:** 6

**Status:** `READY`

---

## Activity title

**Ingerir datos en batch**

---

## Central engineering insight

Reading a source manually is not the same as ingesting it into a controlled data platform.

A batch ingestion step should make explicit:

* where data come from;
* whether the source is valid;
* where the extracted data are persisted;
* what happened during the ingestion.

The workshop should answer:

> How do we move source data into a controlled raw layer without depending on manual notebook state?

The central progression is:

```text
source
↓
validate
↓
extract
↓
persist raw
↓
report
```

---

## Course capability

Introduce the minimum batch-ingestion concepts required later:

* batch source;
* file source;
* database source;
* extraction;
* source validation;
* raw persistence;
* ingestion status;
* ingestion metadata;
* reproducible re-execution.

This activity should not yet become a complete pipeline.

---

## Engineering problem

The retailer receives sales transactions as a daily file.

Product master data are stored in an operational SQLite database.

The analytical platform needs to ingest both sources into a controlled raw area.

Students must build a small ingestion process that:

* validates the source;
* extracts the data;
* persists raw copies;
* records what happened.

---

## Minimal input sources

Provide exactly two sources.

### File source

```text
data/transactions.csv
```

Recommended size:

```text
10–20 rows
```

Suggested fields:

```text
transaction_id
transaction_date
customer_id
product_id
quantity
unit_price
```

---

### Database source

```text
data/products.db
```

Required table:

```text
products
```

Suggested fields:

```text
product_id
product_name
product_category
```

Recommended size:

```text
5–8 products
```

Both complete sources should remain easy to inspect.

---

## Target raw layer

Generate:

```text
temp/raw/
├── transactions.parquet
└── products.parquet
```

The raw outputs should preserve the source information with minimal transformation.

No business transformation is required.

---

## Notebook execution budget

Available teaching allocation:

**approximately 75–80 minutes**

Hard constraints:

```text
maximum notebook cells: 8
recommended cells: 7

maximum effective code lines per code cell: 12
```

Core ingestion logic must remain visible.

Unlike earlier PREs, this activity requires a small reusable source file because ingestion is the first point where code begins to become pipeline-like.

---

## Notebook progression

### Cell 1 — Inspect the two sources

Load:

```text
transactions.csv
products.db
```

Display both small datasets.

Central discussion:

> These sources exist. What would make their entry into the analytical platform controlled and reproducible?

---

### Cell 2 — Validate the file source

Check explicitly:

```text
file exists
required columns exist
transaction_id is present
```

Do not perform full data-quality analysis.

The purpose is only to determine whether extraction can proceed.

Central distinction:

```text
source validation
≠
data quality framework
```

---

### Cell 3 — Ingest the file source

Read:

```text
data/transactions.csv
```

and persist:

```text
temp/raw/transactions.parquet
```

The code should show:

```text
source path
→ read
→ raw output path
```

No hidden helper logic at this point.

---

### Cell 4 — Validate and ingest the database source

Connect to:

```text
data/products.db
```

Verify that:

```text
products
```

exists.

Read it and persist:

```text
temp/raw/products.parquet
```

This cell should visibly demonstrate that ingestion can abstract over different source types.

---

### Cell 5 — Demonstrate one controlled ingestion failure

Use one intentionally invalid source condition.

Recommended:

```text
missing required column in a temporary copy
```

or:

```text
requested database table does not exist
```

Expected result:

```text
FAIL clearly
```

Do not silently continue.

Central lesson:

> A failed ingestion should fail visibly and early.

Only one failure scenario is required.

---

### Cell 6 — Consolidate the ingestion logic

Move the already visible logic into:

```text
src/ingest.py
```

Suggested simple functions:

```text
ingest_csv(...)
ingest_sqlite_table(...)
```

The notebook should then call these functions once.

Important:

The logic must first have been shown explicitly.

`src/` consolidates the lesson; it does not hide it.

---

### Cell 7 — Generate the ingestion report

Create:

```text
submission/ingestion_report.csv
```

Required columns:

```text
source_name
source_type
row_count
status
output_path
```

Required rows:

```text
transactions
products
```

Expected status:

```text
SUCCESS
```

for the canonical final execution.

---

## Optional eighth cell

Only if class time comfortably permits:

delete:

```text
temp/raw/
```

and rerun the consolidated ingestion functions.

Verify that the same logical raw outputs are produced.

This makes reproducibility visible.

If time is tight, this behavior may remain enforced by tests rather than shown in a separate cell.

---

## Required code philosophy

The student must directly see:

```text
how a source is validated
how it is read
where it is written
how success is recorded
```

Do not hide these steps behind an ingestion framework.

Prefer:

```python
transactions = pd.read_csv(source_path)

transactions.to_parquet(
    output_path,
    index=False,
)
```

over a generic abstraction such as:

```python
run_ingestion(config)
```

before the mechanics have been demonstrated.

Classroom explanation should focus on:

* why source validation occurs before ingestion;
* why raw data are persisted;
* why raw data should remain minimally transformed;
* why ingestion metadata matter;
* why failures should not be silently swallowed.

---

## Raw-layer principle

The raw layer should preserve source information.

Permitted transformations are limited to those required for reliable persistence.

Do not:

* calculate sales metrics;
* standardize categories;
* deduplicate business entities;
* join sources;
* aggregate data.

Those operations belong to transformation and pipeline PREs.

---

## Duplicate behavior

If the canonical source contains a duplicate identifier, the ingestion step may detect and report it but should not silently decide how to resolve it.

The principle is:

```text
detect
≠
repair
```

Complex duplicate treatment belongs to later quality/transformation activities.

For the minimal canonical dataset, duplicates are not required.

---

## Ingestion metadata

The final report should answer:

```text
What source was ingested?
What type of source was it?
How many rows were extracted?
Did ingestion succeed?
Where was the raw output written?
```

No timestamps are required because deterministic output is preferable for the classroom artifact.

---

## Expected artifacts

### `temp/raw/transactions.parquet`

Raw copy of the file source.

### `temp/raw/products.parquet`

Raw copy of the database table.

### `submission/ingestion_report.csv`

Required columns:

```text
source_name
source_type
row_count
status
output_path
```

No additional submission artifact is necessary.

---

## Visible validation

Two validations are sufficient.

### Validation 1 — Row preservation

Verify:

```text
source row count
=
raw row count
```

for both sources.

### Validation 2 — Re-ingestion

When rerun from clean generated state, the ingestion produces equivalent raw outputs.

No full idempotency framework is required yet.

---

## Required tests

Repository tests should verify:

1. `data/transactions.csv` exists.
2. `data/products.db` exists.
3. Required source columns exist.
4. Required `products` table exists.
5. `temp/raw/transactions.parquet` can be generated.
6. `temp/raw/products.parquet` can be generated.
7. Raw row counts match source row counts.
8. Raw logical values match source values.
9. Invalid source condition fails clearly.
10. `submission/ingestion_report.csv` exists.
11. Required report columns exist.
12. Report row counts match actual raw outputs.
13. Output paths are relative.
14. Re-execution produces equivalent logical raw outputs.

Tests should validate ingestion behavior rather than internal function names.

---

## What students should observe

The complete workshop should reduce to:

```text
two sources
↓
validate
↓
extract
↓
persist raw
↓
controlled failure
↓
consolidate
↓
report
```

The essential engineering insight is:

> Ingestion creates a controlled boundary between external sources and the internal data platform.

---

## Boundaries

Do not introduce:

* API ingestion;
* streaming ingestion;
* orchestration;
* retries;
* data contracts;
* full data-quality rules;
* incremental processing;
* CDC;
* joins;
* transformations;
* cloud ingestion services.

Those topics belong later.

---

## Relationship with PRE_07

`PRE_07` asks:

> How may source data be represented?

`PRE_08` asks:

> How do source data enter the analytical platform in a controlled way?

---

## Relationship with PRE_09

`PRE_08` uses stable batch sources:

```text
file
database
```

`PRE_09_api_ingestion` introduces a less stable source:

```text
HTTP API
```

and therefore adds:

```text
pagination
transient failure
retry
```

Do not introduce those concerns here.

---

## Relationship with PRE_10

`PRE_08` establishes:

```text
source
→ raw
```

`PRE_10_data_pipeline` will extend that into:

```text
source
→ raw
→ staging
→ curated
```

---

## Acceptance criteria

The PRE is pedagogically acceptable only when:

1. Exactly two source types are sufficient.
2. Both sources are small enough to inspect completely.
3. The notebook uses no more than 8 cells.
4. No code cell exceeds 12 effective lines.
5. Source validation is explicit.
6. File ingestion is explicit.
7. Database ingestion is explicit.
8. Raw persistence is explicit.
9. One controlled failure is demonstrated.
10. Core ingestion logic appears visibly before consolidation into `src/`.
11. Reusable code remains simple and transparent.
12. `submission/ingestion_report.csv` summarizes the ingestion.
13. No transformation or orchestration logic is introduced.
14. The instructor can focus on **why ingestion is a controlled platform boundary**.
15. The activity complies with `AGENTS.md`.

---

## Agent implementation instructions

Do not implement while:

```text
Status: DRAFT
```

When implementation is later authorized:

* use exactly one file source and one SQLite table source;
* keep both datasets small;
* show all core ingestion steps explicitly before moving them to `src/`;
* use only one controlled failure;
* do not add retries;
* do not add joins or transformations;
* do not add configuration frameworks;
* keep `src/ingest.py` simple and functional;
* preserve the 8-cell and 12-line hard limits.
