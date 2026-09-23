# PRE Specification

## Identification

**Activity:** `PRE_22_data_lakehouse`

**Week:** 5

**Status:** `READY`

---

## Activity title

**Organizar un dataset analítico en un data lake**

---

## Central engineering insight

As analytical data grow, one logical dataset does not need to be stored as one physical file.

It can be organized as multiple files using meaningful partitions.

The workshop should answer:

> How can a large logical dataset be physically organized so that processing can target only the relevant portion?

The central progression is:

```text
one dataset
↓
many files
↓
partitioned organization
↓
selective access
```

A second conceptual distinction is:

```text
data lake
≠
lakehouse
```

A lakehouse adds table-management capabilities on top of lake-style storage.

---

## Course capability

Introduce only the minimum concepts required for subsequent activities:

* data lake;
* object-storage intuition;
* analytical files;
* partitioned dataset;
* partition column;
* partition pruning intuition;
* raw versus curated organization;
* lakehouse concept.

The practical exercise should focus on partitioning.

Lakehouse technology itself is not implemented.

---

## Engineering problem

The retailer has accumulated sales for several months.

Keeping the complete history in one analytical file works, but every consumer must conceptually address the complete dataset even when only one month is needed.

The engineering team wants to organize the sales history by:

```text
year
month
```

so that a process interested in one month can address that portion directly.

---

## Minimal input dataset

Provide:

```text
data/sales_history.parquet
```

Suggested fields:

```text
transaction_id
transaction_date
customer_id
product_id
quantity
sales_amount
```

Recommended size:

```text
30–60 rows
```

covering:

```text
2 years
3–4 months
```

The dataset should remain completely understandable.

Large volume is not required because the workshop teaches **organization**, not performance.

---

## Target physical organization

Generate a local structure such as:

```text
temp/lake/
└── curated/
    └── sales/
        ├── year=2025/
        │   ├── month=11/
        │   └── month=12/
        └── year=2026/
            ├── month=01/
            └── month=02/
```

The local filesystem represents the same hierarchical organization that could exist in object storage.

It must be stated explicitly that:

```text
local directories
simulate organization
```

but are not themselves cloud object storage.

---

## Notebook execution budget

Available teaching allocation:

**approximately 45–55 minutes**

Hard constraints:

```text
maximum notebook cells: 6
recommended cells: 6

maximum effective code lines per code cell: 12
```

No essential partitioning logic may be hidden in helper modules.

`src/` is not required.

---

## Notebook progression

### Cell 1 — Load the historical dataset

Read:

```text
data/sales_history.parquet
```

Display the complete or nearly complete dataset.

Derive:

```text
year
month
```

from `transaction_date`.

Central discussion:

> If I need only January 2026, why should the physical organization make me think about all historical records?

---

### Cell 2 — Show the single-file representation

Inspect:

```text
data/sales_history.parquet
```

as one logical and physical file.

Students should recognize:

```text
one dataset
=
one file
```

in the initial representation.

No benchmark is required.

---

### Cell 3 — Write the partitioned dataset

Write the same logical records under:

```text
temp/lake/curated/sales/
```

partitioned by:

```text
year
month
```

The code must make the partitioning decision explicit.

Example logical intent:

```python
sales.to_parquet(
    lake_path,
    partition_cols=["year", "month"],
    index=False,
)
```

The precise implementation may vary according to the approved Parquet engine.

---

### Cell 4 — Inspect the physical layout

List the generated directories/files.

Students should directly observe:

```text
year=...
month=...
```

and connect values in the data to physical locations.

Central question:

> What does the partition column now control besides being an ordinary column value?

This is the key visual moment of the activity.

---

### Cell 5 — Read only one partition

Read only one target such as:

```text
year=2026/month=01
```

and verify that all returned records belong to that period.

The activity should make visible:

```text
logical query need
↓
specific physical partition
```

No timing benchmark is required.

No claim about exact bytes read is required.

---

### Cell 6 — Summarize the architecture

Generate:

```text
submission/lake_summary.csv
```

Required fields:

```text
dataset
partition_columns
partition_count
file_count
row_count
```

Then conclude conceptually:

```text
partitioned Parquet files
+
lake-style storage organization
=
data lake pattern
```

and:

```text
data lake
+
table-management capabilities
=
lakehouse concept
```

No lakehouse table format is implemented.

---

## Required code philosophy

The partitioning operation must be visible directly in the notebook.

Students should be able to understand:

```text
where the data started
where the files were written
which columns define partitions
how one partition is selected
```

without the instructor explaining hidden utility functions.

Classroom explanation should focus on:

* why one logical dataset may contain many physical files;
* why partitioning should reflect common access patterns;
* why year/month is reasonable for temporal data;
* why a high-cardinality identifier is usually a poor partition choice;
* why lake and lakehouse are related but different concepts.

---

## Partition-choice discussion

Only one good and one bad choice are necessary.

### Reasonable

```text
year / month
```

because analytical processing often uses time ranges.

### Poor example

```text
transaction_id
```

because it could create extremely many tiny partitions.

Do not implement the bad partitioning scheme.

Discuss it only.

---

## Raw and curated layers

Mention the common pattern:

```text
raw
curated
```

but do not build two complete pipelines.

For this PRE:

```text
data/sales_history.parquet
```

acts as the provided source, and:

```text
temp/lake/curated/sales/
```

is the generated analytical organization.

Layered pipeline construction belongs to `PRE_10`.

---

## Data lake concept

For this course, a data lake should be introduced as storage that can hold analytical data in files/objects while preserving flexible physical organization.

The practical activity demonstrates:

```text
files
+
directories / object-style prefixes
+
partitions
```

Do not imply that a data lake requires one specific vendor.

---

## Object-storage intuition

Briefly explain that cloud object stores commonly address objects by keys/prefixes rather than by traditional database tables.

The local path:

```text
curated/sales/year=2026/month=01/
```

is used only as a transparent classroom analogue.

Do not introduce:

* S3 credentials;
* buckets;
* IAM;
* cloud APIs;
* cloud SDKs.

---

## Lakehouse concept

A crucial conceptual statement must be explicit:

> Partitioned Parquet files alone do not constitute a complete lakehouse.

Introduce lakehouse as adding table-management semantics over lake-style storage, potentially including capabilities such as:

```text
schema management
transactional updates
table metadata
reliable table versions
```

These are conceptual examples only.

Do not implement:

* Delta Lake;
* Apache Iceberg;
* Apache Hudi.

---

## Expected artifact

### `submission/lake_summary.csv`

Required columns:

```text
dataset
partition_columns
partition_count
file_count
row_count
```

The artifact should describe:

```text
sales
```

and its generated partitioned organization.

No additional submission artifact is necessary.

---

## Visible validation

Only two visible validations are required.

### Validation 1 — Logical equivalence

Verify that:

```text
rows in original dataset
=
rows across partitioned dataset
```

### Validation 2 — Partition correctness

Verify that the selected:

```text
year=2026/month=01
```

partition contains only January 2026 records.

---

## Required tests

Repository tests should verify:

1. `data/sales_history.parquet` exists.
2. Partitioned output can be generated.
3. Required year/month directories exist.
4. All original rows are represented exactly once.
5. Selected partition contains only the expected period.
6. Total row count is preserved.
7. `submission/lake_summary.csv` exists.
8. Required summary columns exist.
9. Partition and file counts match generated structure.
10. Output is deterministic.

No performance timing should be tested.

---

## What students should observe

The complete workshop should reduce to:

```text
one Parquet file
↓
derive partition columns
↓
write partitioned dataset
↓
inspect folders
↓
read one partition
↓
understand lake organization
```

The central insight is:

> Partitioning connects how data are physically organized with how they are commonly accessed.

---

## Boundaries

Do not introduce:

* Delta Lake;
* Apache Iceberg;
* Apache Hudi;
* ACID implementation details;
* object-store APIs;
* S3 administration;
* cloud credentials;
* small-file optimization;
* compaction;
* table maintenance;
* partition evolution;
* performance benchmarking.

These concepts are unnecessary for this PRE.

---

## Relationship with PRE_05

`PRE_05` establishes:

```text
why Parquet is useful as an analytical format
```

`PRE_06` establishes:

```text
how many Parquet files can represent one organized analytical dataset
```

The progression is:

```text
physical file format
↓
physical dataset organization
```

---

## Relationship with PRE_07

`PRE_06` still deals with regular analytical tabular data.

`PRE_23_nosql_data` will ask:

> What happens when the source itself does not fit naturally into one fixed tabular structure?

---

## Acceptance criteria

The PRE is pedagogically acceptable only when:

1. One small historical dataset drives the complete activity.
2. The notebook uses no more than 6 cells.
3. No code cell exceeds 12 effective lines.
4. Partitioning by year/month is visible.
5. Generated physical directories are inspected.
6. One partition is read independently.
7. Logical row counts remain unchanged.
8. No performance benchmark is required.
9. Object storage is explained conceptually without cloud infrastructure.
10. Data lake and lakehouse are explicitly distinguished.
11. Partitioned Parquet files are not incorrectly presented as a complete lakehouse.
12. No Delta/Iceberg/Hudi implementation is introduced.
13. The instructor can focus on **why data are partitioned**, rather than on filesystem or cloud mechanics.
14. The activity complies with `AGENTS.md`.

---

## Agent implementation instructions

Do not implement while:

```text
Status: DRAFT
```

When implementation is later authorized:

* use a small dataset spanning only a few temporal partitions;
* keep the partition write visible in the notebook;
* keep directory inspection visible;
* do not add a cloud service;
* do not simulate large-scale performance;
* do not implement a lakehouse table format;
* do not hide core partition logic in helper modules;
* preserve the 6-cell and 12-line hard limits.
