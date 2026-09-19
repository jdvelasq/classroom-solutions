# PRE Specification

## Identification

**Activity:** `PRE_10_data_pipeline`

**Week:** 7

**Status:** `READY`

---

## Activity title

**Construir un pipeline reproducible**

---

## Central engineering insight

A sequence of notebook operations is not yet a reliable data pipeline.

A pipeline makes explicit:

* inputs;
* stages;
* intermediate outputs;
* final output;
* execution order;
* validation;
* reproducible execution.

The workshop should answer:

> How do we turn a sequence of working data transformations into a process that can be executed completely from a clean state?

The central progression is:

```text
manual steps
↓
explicit stages
↓
raw
↓
staging
↓
curated
↓
validation
↓
single reproducible execution
```

---

## Course capability

Integrate previously introduced concepts into one end-to-end workflow:

* extraction;
* transformation;
* loading;
* raw layer;
* staging layer;
* curated layer;
* ETL;
* ELT concept;
* configuration;
* logging;
* validation;
* reproducibility.

This is an integration workshop.

It should not introduce several new technologies.

---

## Engineering problem

The retailer receives transaction data and product reference data.

An analyst currently performs:

```text
read transactions
read products
clean transaction fields
join products
calculate sales
save result
```

manually in a notebook.

The steps work.

However, the result depends on:

* execution order;
* notebook state;
* manually selected paths;
* intermediate data that are not persisted;
* manual verification.

Students must convert those steps into a reproducible pipeline.

---

## Minimal input sources

Use exactly two inputs.

### `data/transactions.csv`

Recommended:

```text
10–20 rows
```

Required fields:

```text
transaction_id
transaction_date
product_id
quantity
unit_price
```

Include one or two deliberately simple staging issues, such as:

```text
transaction_date stored as text
quantity stored as text
```

Do not include extensive dirty-data cases.

---

### `data/products.csv`

Recommended:

```text
4–6 products
```

Required fields:

```text
product_id
product_name
product_category
```

Both complete datasets should fit comfortably on screen.

---

## Final analytical output

Required grain:

> One row per transaction.

Required fields:

```text
transaction_id
transaction_date
product_id
product_name
product_category
quantity
unit_price
sales_amount
```

where:

```text
sales_amount = quantity * unit_price
```

---

## Pipeline layers

The practical pipeline uses exactly three data layers.

### Raw

```text
temp/pipeline/raw/
```

Purpose:

Preserve extracted source data with minimal modification.

---

### Staging

```text
temp/pipeline/staging/
```

Purpose:

Prepare data for integration.

---

### Curated

```text
temp/pipeline/curated/
```

Purpose:

Contain the integrated analytics-ready dataset.

---

## Target physical structure

```text
temp/pipeline/
├── raw/
│   ├── transactions.parquet
│   └── products.parquet
├── staging/
│   └── transactions.parquet
└── curated/
    └── sales.parquet
```

Final consumer artifact:

```text
submission/sales_curated.parquet
```

Execution summary:

```text
submission/pipeline_report.csv
```

---

## Notebook execution budget

Available teaching allocation:

**approximately 150–165 minutes**

Hard constraints:

```text
maximum notebook cells: 14
recommended cells: 11–12

maximum effective code lines per code cell: 12
```

The full pipeline logic must remain visible before being consolidated into `src/pipeline.py`.

---

## Notebook progression

### Cell 1 — Inspect the source data

Load and display:

```text
transactions
products
```

Central discussion:

> What are the inputs to the process?

The complete source data should remain understandable.

---

### Cell 2 — Reproduce the manual workflow

Perform the familiar sequence directly:

```text
read
convert types
join
calculate sales_amount
```

Produce a correct DataFrame.

Central observation:

```text
correct result
≠
reproducible pipeline
```

---

### Cell 3 — Identify the pipeline stages

Define explicitly:

```text
extract
stage
curate
validate
```

Use a small configuration structure containing only paths.

Example intent:

```python
paths = {
    "transactions": "data/transactions.csv",
    "products": "data/products.csv",
    "pipeline": "temp/pipeline",
}
```

Central discussion:

> Why should paths and execution structure be explicit rather than scattered through the code?

---

### Cell 4 — Extract to raw

Read both source datasets and persist:

```text
temp/pipeline/raw/transactions.parquet
temp/pipeline/raw/products.parquet
```

Minimal transformation only.

Students should directly see:

```text
source
→ raw
```

---

### Cell 5 — Build staging

Read raw transactions.

Apply only the transformations required before integration:

```text
transaction_date → datetime
quantity → numeric
unit_price → numeric
```

Persist:

```text
temp/pipeline/staging/transactions.parquet
```

Central discussion:

> Why separate source preservation from preparation?

---

### Cell 6 — Build curated data

Read staged transactions and raw products.

Join using:

```text
product_id
```

Calculate:

```text
sales_amount
```

Produce the final transaction-level analytical representation.

---

### Cell 7 — Persist curated output

Write:

```text
temp/pipeline/curated/sales.parquet
```

and:

```text
submission/sales_curated.parquet
```

Students should see the explicit load/persistence boundary.

---

### Cell 8 — Validate the pipeline result

Use only the validations central to the activity:

```text
transaction_id is unique
curated row count equals source row count
all product_id values resolved
total sales reconcile
```

Do not build a full data-quality framework.

Central discussion:

> Why is validation part of the pipeline rather than a manual step after it?

---

### Cell 9 — Add minimal execution logging

Record concise execution evidence such as:

```text
EXTRACT: 15 transactions
STAGING: 15 transactions
CURATED: 15 transactions
VALIDATION: PASS
```

Use Python's standard logging or an equally transparent mechanism.

Do not build an observability framework.

---

### Cell 10 — Consolidate the pipeline

Move the already demonstrated logic into:

```text
src/pipeline.py
```

Suggested functions:

```text
extract()
stage()
curate()
validate()
run_pipeline()
```

The notebook must not introduce new hidden behavior at this point.

`src/` consolidates code that students have already seen.

---

### Cell 11 — Execute from a clean state

Delete generated:

```text
temp/pipeline/
submission/sales_curated.parquet
```

when appropriate.

Then execute:

```python
run_pipeline()
```

Students should observe:

```text
clean generated state
↓
one execution
↓
complete pipeline rebuilt
```

This is the central reproducibility demonstration.

---

### Cell 12 — Generate the pipeline report

Create:

```text
submission/pipeline_report.csv
```

Required columns:

```text
stage
input_rows
output_rows
status
```

Required logical rows:

```text
extract
staging
curated
validation
```

No additional report is necessary.

---

## Optional cells 13–14

Use only if class time comfortably permits.

### Optional — Silent logical failure

Create one temporary duplicated product key.

Show that a join may execute without exception while multiplying transaction rows.

Then demonstrate that the row-count validation detects the error.

This reinforces:

```text
pipeline ran
≠
pipeline is correct
```

This is valuable but optional because grain errors were already introduced in `PRE_02`.

---

### Optional — ETL versus ELT mapping

Map the implemented pipeline to:

```text
Extract
→ Transform
→ Load
```

Then discuss conceptually how an ELT design would differ:

```text
Extract
→ Load
→ Transform in target system
```

No second implementation is required.

This discussion may occur orally rather than as a dedicated cell.

---

## Required code philosophy

Students must directly see:

```text
how source data are extracted
how raw outputs are created
how staging transformations occur
how integration occurs
how curated data are persisted
how validation works
how the complete pipeline is executed
```

Do not begin with:

```python
run_pipeline()
```

and then explain hidden implementation.

The order must be:

```text
see logic
↓
understand logic
↓
consolidate logic
↓
run pipeline
```

---

## Configuration

Keep configuration minimal.

Only values such as:

```text
input paths
generated paths
output paths
```

need to be separated from processing logic.

Do not introduce:

* YAML;
* TOML;
* configuration libraries;
* environment-management frameworks.

The lesson is simply:

```text
configuration
≠
processing logic
```

---

## Logging

Logging should answer:

```text
What stage ran?
How many rows did it process?
Did it succeed?
```

Nothing more is required.

Do not include detailed timestamps in graded artifacts if they reduce determinism.

---

## ETL versus ELT

The implemented workflow may be described primarily as ETL-style:

```text
extract
→ transform
→ persist analytical result
```

ELT should be introduced conceptually as an alternative where raw data are loaded into the target platform before transformation.

Do not implement two pipelines.

---

## Expected artifacts

### `submission/sales_curated.parquet`

Required properties:

* one row per transaction;
* `transaction_id` unique;
* all product references resolved;
* `sales_amount` correct;
* deterministic logical content.

---

### `submission/pipeline_report.csv`

Required columns:

```text
stage
input_rows
output_rows
status
```

No additional submission artifacts are required.

---

## Visible validation

The notebook should visibly validate only the claims central to the pipeline:

### Grain

```text
source transactions
=
curated rows
```

### Reference resolution

```text
all product_id values match products
```

### Business calculation

```text
sales_amount = quantity * unit_price
```

### Reproducibility

A clean rerun recreates equivalent logical outputs.

---

## Required tests

Repository tests should verify:

1. Required source files exist.
2. `src/pipeline.py` can be imported.
3. Raw outputs can be generated.
4. Staging output can be generated.
5. Curated output can be generated.
6. `submission/sales_curated.parquet` exists.
7. Required curated columns exist.
8. `transaction_id` is unique.
9. Curated row count equals source transaction count.
10. All product identifiers resolve.
11. `sales_amount` is correct.
12. Total sales reconcile with source values.
13. `submission/pipeline_report.csv` exists.
14. Required stages are represented.
15. A clean second execution produces equivalent logical output.
16. No machine-specific absolute paths appear in submission artifacts.

Tests should validate observable pipeline behavior rather than internal function organization.

---

## What students should observe

The complete workshop should reduce to:

```text
working notebook operations
↓
explicit stages
↓
raw
↓
staging
↓
curated
↓
validation
↓
consolidated pipeline
↓
delete outputs
↓
rebuild everything
```

The essential engineering insight is:

> A pipeline is valuable because its complete result can be recreated predictably from explicit inputs.

---

## Boundaries

Do not introduce:

* API ingestion;
* orchestration frameworks;
* DAG schedulers;
* retries between pipeline tasks;
* incremental processing;
* CDC;
* data contracts;
* comprehensive data-quality frameworks;
* distributed processing;
* streaming;
* cloud infrastructure.

Those topics belong to later PREs.

---

## Relationship with PRE_08 and PRE_09

`PRE_08` and `PRE_09` establish:

```text
source
→ ingestion
```

`PRE_10` extends the idea to:

```text
source
→ raw
→ staging
→ curated
→ validated analytical output
```

---

## Relationship with PRE_11–PRE_14

This PRE establishes the simple pipeline that subsequent activities will strengthen.

```text
PRE_10  reproducible pipeline
PRE_11  quality
PRE_12  contracts
PRE_13  incremental execution
PRE_14  operations
```

Each later PRE should add one engineering capability rather than rebuild this entire workshop.

---

## Acceptance criteria

The PRE is pedagogically acceptable only when:

1. Exactly two source datasets are sufficient.
2. Both sources remain visually understandable.
3. The notebook uses no more than 14 cells.
4. Recommended implementation uses approximately 11–12 cells.
5. No code cell exceeds 12 effective lines.
6. Manual workflow appears before pipeline consolidation.
7. Raw, staging, and curated roles are explicit.
8. All core transformation logic is visible.
9. `src/pipeline.py` only consolidates previously visible logic.
10. One explicit pipeline entry point exists.
11. Clean-state execution recreates all required outputs.
12. Validation is part of the pipeline.
13. Configuration remains minimal.
14. Logging remains minimal.
15. ETL versus ELT is explained without implementing a second workflow.
16. No later-course capability is pulled into this PRE unnecessarily.
17. The instructor can spend the class explaining **why explicit stages and reproducibility matter** rather than debugging hidden abstractions.
18. The activity complies with `AGENTS.md`.

---

## Agent implementation instructions

Do not implement while:

```text
Status: DRAFT
```

When implementation is later authorized:

* use exactly two small sources;
* show the complete manual logic before consolidation;
* keep raw/staging/curated visibly distinct;
* use only minimal configuration;
* use only minimal logging;
* do not add orchestration;
* do not add incremental processing;
* do not add generalized quality frameworks;
* do not hide essential logic in `src/`;
* preserve the 14-cell and 12-line hard limits.
