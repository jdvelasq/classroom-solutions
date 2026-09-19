# PRE Specification

## Identification

**Activity:** `PRE_15_distributed_processing`

**Week:** 10

**Status:** `READY`

---

## Activity title

**Entender cómo se distribuye un procesamiento**

---

## Central engineering insight

Distributed processing is not primarily about writing different analytical logic.

It is about executing that logic over data divided into partitions, potentially requiring data to move between partitions.

The workshop should answer:

> What changes when an analytical operation is executed by a distributed processing engine instead of directly in one local DataFrame?

The central progression is:

```text
data
↓
partitions
↓
lazy transformations
↓
action
↓
shuffle when required
↓
distributed result
```

The essential lesson is:

```text
same analytical question
≠
same execution model
```

---

## Course capability

Introduce only the minimum distributed-processing concepts required by the course:

* partition;
* distributed DataFrame;
* transformation;
* action;
* lazy evaluation;
* execution plan;
* narrow transformation intuition;
* shuffle;
* distributed aggregation;
* Spark DataFrame;
* Spark SQL.

The activity should not become a Spark programming course.

---

## Engineering problem

The retailer needs to calculate sales by product category.

The calculation itself is trivial:

```text
sales_amount = quantity * unit_price
```

followed by:

```text
GROUP BY product_category
```

The objective is not to learn a more complicated calculation.

The objective is to understand how a distributed engine executes it.

---

## Minimal input dataset

Provide:

```text
data/sales.csv
```

Recommended size:

```text
30–60 rows
```

Required fields:

```text
transaction_id
product_category
quantity
unit_price
```

Use approximately:

```text
3–4 product categories
```

The entire dataset should remain understandable.

Do not generate hundreds of thousands or millions of rows merely to justify Spark.

---

## Why the dataset remains small

The workshop teaches:

```text
execution structure
```

not:

```text
performance at scale
```

A small dataset allows students to understand the exact analytical result while Spark makes the distributed execution model observable.

The principle is:

```text
use Spark because distribution is the concept
not because the dataset is large
```

---

## Technology

Use:

```text
PySpark
Spark DataFrame API
Spark SQL
```

in local mode.

The canonical classroom configuration must be explicit and deterministic:

```text
master = local[2]
spark.sql.shuffle.partitions = 3
```

Do not use:

```text
local[*]
```

as the canonical configuration because the number of available cores may differ across machines.

No external Spark cluster is required.

---

## Reproducibility principle

The same notebook should behave predictably on different teaching machines.

Therefore the implementation should control the relevant execution settings rather than inherit machine-dependent defaults.

Canonical pedagogical settings:

```text
2 local execution threads
3 shuffle partitions
```

These values are chosen because they make distributed execution visible while remaining small.

They are **not production tuning recommendations**.

---

## Notebook execution budget

Available teaching allocation:

**approximately 150–165 minutes**

Hard constraints:

```text
maximum notebook cells: 14
recommended cells: 10–11

maximum effective code lines per code cell: 12
```

The additional class time is for explaining the execution model, not for adding more Spark features.

---

## Notebook progression

### Cell 1 — Establish the analytical result locally

Load:

```text
data/sales.csv
```

with pandas.

Calculate:

```text
sales_amount
```

and total sales by:

```text
product_category
```

This creates a transparent reference result.

Central discussion:

> We already know how to solve the analytical problem. Why would the execution engine matter?

---

### Cell 2 — Start Spark deterministically

Create a Spark session using:

```text
local[2]
```

and set:

```text
spark.sql.shuffle.partitions = 3
```

Then read the same sales dataset into a Spark DataFrame.

Inspect:

```text
schema
rows
```

The logical data should clearly be the same as in pandas.

Central observation:

```text
same data
different execution engine
```

---

### Cell 3 — Make partitions visible

Use exactly:

```text
3 partitions
```

for the classroom demonstration.

If necessary, apply:

```python
sales = sales.repartition(3)
```

and inspect partition assignment using:

```text
spark_partition_id()
```

Students should directly observe that different records belong to different partitions.

Central discussion:

> What does it mean for one logical DataFrame to be physically divided?

---

## Important note on `repartition(3)`

Explicit repartitioning is used only to make partitioning observable.

It may itself require data redistribution.

Therefore:

```text
repartition(3)
=
pedagogical device
```

not:

```text
recommended production configuration
```

The implementation must state this explicitly.

---

### Cell 4 — Define transformations without executing the result

Create:

```text
sales_amount = quantity * unit_price
```

and optionally one simple row-level filter.

Do not immediately request the resulting rows.

Explain:

```text
transformation defined
≠
transformation executed
```

This establishes lazy evaluation.

---

### Cell 5 — Trigger an action

Use one obvious action such as:

```text
show()
```

or:

```text
count()
```

Students should observe that Spark now executes the previously defined transformations.

Central progression:

```text
transformation
↓
plan recorded
↓
action
↓
execution
```

Do not introduce several action types.

---

### Cell 6 — Perform the distributed aggregation

Calculate:

```text
sales by product_category
```

using the Spark DataFrame API.

This operation should produce the same logical result as the pandas reference.

Central question:

> Records for the same category may begin in different partitions. How can Spark calculate one total per category?

This motivates:

```text
shuffle
```

---

### Cell 7 — Inspect the execution plan

Use:

```python
result.explain()
```

or an equally readable plan representation.

Identify conceptually:

```text
scan
row-level transformation
aggregation
Exchange / shuffle
```

Do not explain every line of the Spark plan.

The instructor should focus on:

> Which operation requires data to move between partitions, and why?

---

### Cell 8 — Express the same aggregation with Spark SQL

Register the transformed DataFrame as a temporary view.

Run the equivalent SQL:

```sql
SELECT
    product_category,
    SUM(sales_amount) AS total_sales
FROM sales
GROUP BY product_category
ORDER BY product_category
```

Compare it with the DataFrame result.

Central insight:

```text
DataFrame API
and
SQL
```

are different interfaces that can express work executed by the same distributed engine.

Do not teach additional Spark SQL syntax.

---

### Cell 9 — Persist the distributed result

Write:

```text
submission/category_sales.parquet
```

using Spark.

Make explicit that Spark writes a logical dataset that may contain multiple physical files.

Connect this to concepts already seen in `PRE_06`.

Central observation:

```text
one logical output
≠
necessarily one physical file
```

---

### Cell 10 — Read back and validate

Read:

```text
submission/category_sales.parquet
```

and compare the Spark result with the pandas reference.

Sort both results explicitly by:

```text
product_category
```

before comparison.

The analytical answer should match even though execution differs.

---

### Cell 11 — Summarize observable execution properties

If retained, generate:

```text
submission/execution_summary.csv
```

Required columns:

```text
metric
value
```

Required metrics:

```text
input_rows
teaching_input_partitions
shuffle_partitions
output_categories
validation_status
```

Expected values should include:

```text
teaching_input_partitions = 3
shuffle_partitions = 3
validation_status = PASS
```

This cell may be combined with Cell 10 if that makes the notebook clearer.

---

## No requirement to use all 14 cells

The limit:

```text
14 cells
```

is a maximum.

The target implementation should remain approximately:

```text
10–11 cells
```

Do not add examples merely because more class time is available.

---

## Required conceptual sequence

Students should distinguish three levels.

### Logical data

```text
sales records
```

### Logical computation

```text
calculate sales_amount
group by category
sum
```

### Physical execution

```text
partitions
tasks
data movement
shuffle
```

The workshop should keep these levels distinct.

---

## Partition concept

A partition is introduced as:

> A portion of a distributed dataset that can be processed as one unit of work.

For the canonical demonstration:

```text
3 partitions
```

are used deliberately.

Do not introduce:

* partition sizing formulas;
* executor-memory tuning;
* partition skew optimization;
* adaptive partition coalescing.

The goal is simply to establish:

```text
one DataFrame
→
multiple partitions
```

---

## Lazy evaluation

Students need only understand:

```text
transformation
→
plan recorded

action
→
plan executed
```

Do not introduce detailed Catalyst internals.

Do not require knowledge of:

* logical-plan optimization phases;
* physical-plan selection rules;
* whole-stage code generation.

---

## Narrow transformation intuition

Use a simple row-level operation such as:

```text
sales_amount = quantity * unit_price
```

to explain:

> Each output row can be produced from its corresponding input row without collecting records by key.

No formal taxonomy of Spark dependencies is required.

---

## Shuffle intuition

Use:

```text
GROUP BY product_category
```

to establish:

> Records with the same key may reside in different partitions, so data must be reorganized before the final aggregation can be completed.

The observable execution plan should support this discussion.

Do not teach shuffle tuning.

---

## Shuffle partition configuration

Set explicitly:

```text
spark.sql.shuffle.partitions = 3
```

for the canonical notebook.

This prevents the example from inheriting a larger environment-dependent default and keeps the resulting plan easier to reason about.

The number:

```text
3
```

has pedagogical value only.

In production, partition counts depend on:

* workload;
* data volume;
* cluster resources;
* operation characteristics.

Do not present the classroom value as a tuning rule.

---

## Spark execution terminology

The instructor may introduce:

```text
job
stage
task
```

only at a high level.

Suggested intuition:

```text
action
→ job

shuffle boundary
→ stage boundary

partition work
→ task
```

These terms should support the execution explanation.

They must not become a separate technical lesson.

---

## DataFrame API versus Spark SQL

The workshop should demonstrate exactly one equivalent aggregation through both interfaces.

Students should observe:

```text
different expression
↓
same analytical result
↓
same Spark execution engine
```

No catalog of Spark SQL functionality is required.

---

## Performance

Do not make timing the central activity.

Do not benchmark:

```text
pandas versus Spark
```

using the tiny classroom dataset.

The small dataset would produce misleading conclusions because distributed execution introduces overhead.

It is appropriate to state:

> Distributed systems become useful when scale or workload exceeds what is convenient for a single-process execution model, but this classroom example exists to expose the execution model rather than demonstrate speed.

---

## Deterministic comparison

Spark does not guarantee a meaningful row order unless it is explicitly requested.

Therefore all graded comparisons must sort by:

```text
product_category
```

before asserting equality.

Tests must compare logical values, not incidental physical output ordering.

Do not rely on:

* partition file names;
* task IDs;
* physical file order;
* exact execution-plan text.

---

## Expected artifacts

### `submission/category_sales.parquet`

Required grain:

> One row per product category.

Required fields:

```text
product_category
total_sales
```

Required properties:

* logically equal to pandas reference result;
* one row per category;
* generated through Spark;
* deterministic when read and explicitly sorted.

---

### `submission/execution_summary.csv`

If retained, required columns:

```text
metric
value
```

Required metrics:

```text
input_rows
teaching_input_partitions
shuffle_partitions
output_categories
validation_status
```

No detailed Spark diagnostic dump is required.

---

## Visible validation

Only two central validations are required.

### Validation 1 — Analytical equivalence

Verify:

```text
pandas category totals
=
Spark category totals
```

after deterministic sorting.

### Validation 2 — Output grain

Verify that every expected:

```text
product_category
```

appears exactly once in the final result.

---

## Required tests

Repository tests should verify:

1. `data/sales.csv` exists.
2. Required input columns exist.
3. Spark can start successfully with `local[2]`.
4. Canonical shuffle partition setting is `3`.
5. Spark result can be generated.
6. `submission/category_sales.parquet` exists.
7. Required output columns exist.
8. Output contains one row per category.
9. Spark category totals equal the reference calculation.
10. Total output sales reconcile with total input sales.
11. `submission/execution_summary.csv` exists if retained.
12. Summary reports `PASS`.
13. Re-execution produces equivalent logical output.

Tests must not depend on:

* machine CPU count;
* exact task identifiers;
* output file names;
* exact Spark physical-plan text;
* execution speed.

---

## Environment requirement

Before implementation is approved, verify compatibility among:

```text
Python
PySpark
Java
```

for the teaching environment.

The implementation report must state the tested versions.

The canonical Spark session should use:

```text
local[2]
```

rather than dynamically selecting all available cores.

Do not modify repository dependencies blindly.

---

## What students should observe

The complete workshop should reduce to:

```text
same analytical problem
↓
Spark DataFrame
↓
3 visible partitions
↓
lazy transformation
↓
action
↓
group-by
↓
shuffle
↓
same analytical answer
```

The essential engineering insight is:

> Distributed processing changes how computation is executed, not the meaning of the analytical question.

---

## Boundaries

Do not introduce:

* Spark cluster administration;
* YARN;
* Kubernetes;
* executors in depth;
* memory tuning;
* caching strategies;
* broadcast joins;
* partition skew;
* speculative execution;
* Spark Streaming;
* GraphX;
* MLlib;
* Catalyst internals;
* large synthetic benchmarks.

These are unnecessary for this PRE.

---

## Relationship with PRE_14

`PRE_14` asks:

> How are pipeline tasks coordinated operationally?

`PRE_15` asks:

> How is the computation inside a data-processing task distributed?

The distinction is:

```text
pipeline orchestration
≠
distributed computation
```

---

## Relationship with PRE_16

`PRE_15` still processes:

```text
bounded data
```

even though the computation is distributed.

`PRE_16_event_streams` will introduce:

```text
unbounded sequence of events
```

This provides the transition from distributed batch processing to streaming concepts.

---

## Acceptance criteria

The PRE is pedagogically acceptable only when:

1. The analytical calculation remains trivial.
2. The source dataset remains small and understandable.
3. Spark is used because distribution is the lesson, not because artificial scale is created.
4. The notebook uses no more than 14 cells.
5. Recommended implementation uses approximately 10–11 cells.
6. No code cell exceeds 12 effective lines.
7. The canonical Spark master is `local[2]`.
8. Canonical shuffle partitions are explicitly set to `3`.
9. Partition count does not depend on machine CPU count.
10. Three partitions are directly observable.
11. Explicit repartitioning is identified as a teaching device.
12. Lazy evaluation is directly observable.
13. Exactly one action is sufficient to establish execution.
14. One aggregation motivates shuffle.
15. The execution plan is inspected without teaching Spark internals.
16. DataFrame API and SQL express one equivalent computation.
17. Spark and pandas results reconcile.
18. Comparisons use explicit deterministic ordering.
19. No performance benchmark is required.
20. No cluster is required.
21. The instructor can focus on **why distributed execution requires partitions and sometimes data movement**, rather than on Spark syntax or infrastructure.
22. The activity complies with `AGENTS.md`.

---

## Agent implementation instructions

Do not implement while:

```text
Status: DRAFT
```

When implementation is later authorized:

* verify Python/PySpark/Java compatibility first;
* use Spark only in local mode;
* use `local[2]` for the canonical Spark session;
* set `spark.sql.shuffle.partitions = 3`;
* use a tiny deterministic dataset;
* keep the analytical problem trivial;
* use exactly three visible partitions for teaching;
* use `repartition(3)` only when needed to expose partitioning;
* state explicitly that repartitioning and the chosen partition counts are pedagogical;
* use exactly one aggregation to motivate shuffle;
* show the execution plan but do not test its exact text;
* explicitly sort logical results before equality comparisons;
* do not generate large synthetic datasets;
* do not benchmark pandas against Spark;
* do not introduce Spark tuning;
* do not introduce a cluster;
* preserve the 14-cell and 12-line hard limits.
