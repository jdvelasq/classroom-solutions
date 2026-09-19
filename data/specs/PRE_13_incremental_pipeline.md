# PRE Specification

## Identification

**Activity:** `PRE_13_incremental_pipeline`

**Week:** 9

**Status:** `READY`

---

## Activity title

**Procesar solamente lo que cambió**

---

## Central engineering insight

A data pipeline does not always need to rebuild an entire dataset.

When a reliable current state already exists, a new batch can be compared with that state and only the required changes applied.

The workshop should answer:

> How can we update a dataset using only new changes without creating duplicates or unnecessary rewrites?

The central progression is:

```text
current state
+
new changes
↓
filter using checkpoint
↓
classify
↓
INSERT / UPDATE / UNCHANGED
↓
apply changes
↓
advance checkpoint
↓
safe rerun
```

The essential lesson is:

```text
incremental processing
≠
append everything
```

---

## Course capability

Introduce the minimum incremental-processing concepts required later:

* current state;
* business key;
* change batch;
* insert;
* update;
* unchanged record;
* upsert intuition;
* checkpoint;
* source high-water mark;
* idempotent re-execution.

CDC should be introduced only conceptually.

The term `watermark` must not be used for this batch-incremental mechanism.

---

## Engineering problem

The analytical platform already contains the current customer dataset.

A new customer-change batch arrives.

Some records represent:

```text
new customers
changed customers
customers whose relevant values did not actually change
```

Rebuilding the complete customer dataset from historical source data would be unnecessary.

Simply appending the new batch would create multiple rows for the same customer.

Students must update the current state correctly.

---

## Minimal input state

Provide:

```text
data/customers_current.parquet
```

Recommended size:

```text
5 customers
```

Required fields:

```text
customer_id
customer_name
city
segment
updated_at
```

Required grain:

> One row per customer.

`customer_id` is the business key.

---

## Minimal change batch

Provide:

```text
data/customer_changes.parquet
```

Use exactly three meaningful change records.

### One INSERT

Example:

```text
C006
```

does not yet exist in the current dataset.

---

### One UPDATE

Example:

```text
C002
```

already exists but one relevant attribute has changed.

For example:

```text
city:
Medellín
→
Envigado
```

---

### One UNCHANGED

Example:

```text
C003
```

arrives again with the same relevant business values.

Its later change timestamp alone must not force a business update.

---

## Change metadata

The change batch should contain:

```text
changed_at
```

representing the source change position.

All canonical batch records should initially be newer than the starting checkpoint.

Do not include multiple changes for the same customer in this PRE.

That would add ordering complexity without improving the central lesson.

---

## Initial checkpoint

Provide a simple starting value such as:

```text
2026-09-14T00:00:00
```

The checkpoint represents:

> All source changes up to this position have already been processed successfully.

For this PRE, the checkpoint stores the current:

```text
source high-water mark
```

meaning:

> The greatest source change position that the pipeline has safely processed.

This is a **batch incremental progress marker**.

---

## Terminology rule

Use:

```text
checkpoint
```

for the persisted pipeline progress state.

Use:

```text
source high-water mark
```

for the maximum source position represented by that checkpoint.

Do not use:

```text
watermark
```

in this PRE.

The distinction must be explicit:

```text
source high-water mark
≠
streaming event-time watermark
```

`PRE_17` will introduce `watermark` with a different purpose:

> deciding how far event-time processing may progress while accounting for late events.

---

## Target outputs

Generate:

```text
submission/customers_current.parquet
submission/incremental_report.csv
```

The updated customer dataset must still have:

```text
one row per customer
```

Generated execution state may use:

```text
temp/checkpoint.json
```

---

## Notebook execution budget

Available teaching allocation:

**approximately 75 minutes**

Hard constraints:

```text
maximum notebook cells: 8
recommended cells: 7

maximum effective code lines per code cell: 12
```

All central incremental logic must remain visible.

---

## Notebook progression

### Cell 1 — Inspect current state and incoming changes

Load:

```text
customers_current
customer_changes
```

Display both complete datasets.

State explicitly:

```text
business key = customer_id
```

Central question:

> What would happen if we simply appended these three change records?

Students should recognize that existing customers would be duplicated.

---

### Cell 2 — Apply the checkpoint

Define:

```text
checkpoint
```

and retain only source changes satisfying:

```text
changed_at > checkpoint
```

All canonical change rows should initially remain eligible.

Central discussion:

> Why should a recurring pipeline remember how far it has already processed?

Explain:

```text
checkpoint
→ persisted progress

max processed changed_at
→ source high-water mark
```

No streaming terminology is required.

---

### Cell 3 — Classify the changes

Compare eligible changes with the current state using:

```text
customer_id
```

Classify every incoming record as exactly one of:

```text
INSERT
UPDATE
UNCHANGED
```

The expected result should visibly contain:

```text
1 INSERT
1 UPDATE
1 UNCHANGED
```

Central discussion:

> Why is an existing key not automatically an update?

An update occurs only when relevant business values differ.

---

### Cell 4 — Apply INSERT and UPDATE

Construct the new current state.

Behavior:

```text
INSERT
→ add customer

UPDATE
→ replace current customer values

UNCHANGED
→ keep existing customer
```

The resulting dataset must retain:

```text
one row per customer
```

No historical version table is required.

---

### Cell 5 — Persist state and advance checkpoint

Write:

```text
submission/customers_current.parquet
```

Calculate:

```text
new_high_water_mark = max(changed_at)
```

and persist it as the new checkpoint under:

```text
temp/checkpoint.json
```

Central principle:

```text
successful processing
→
advance checkpoint
```

The checkpoint must advance only after the new current state has been produced successfully.

This matters because:

```text
checkpoint advancement
before successful persistence
→
possible skipped changes
```

---

### Cell 6 — Rerun the same batch

Read the persisted checkpoint.

Apply it to the same:

```text
customer_changes.parquet
```

Expected eligible records:

```text
0
```

The current customer dataset must remain unchanged.

Students should observe:

```text
same batch
+
advanced checkpoint
→
no repeated work
```

This is the central idempotency demonstration.

---

### Cell 7 — Generate the incremental report

Create:

```text
submission/incremental_report.csv
```

Required columns:

```text
action
record_count
```

Required rows:

```text
INSERT
UPDATE
UNCHANGED
```

Expected canonical counts:

```text
INSERT      1
UPDATE      1
UNCHANGED   1
```

Also display explicitly in the notebook:

```text
rerun eligible rows = 0
```

No larger audit structure is required.

---

## Optional eighth cell

Only if class time comfortably permits:

consolidate the already visible logic into:

```text
src/incremental.py
```

Suggested functions:

```text
classify_changes(...)
apply_changes(...)
```

No new behavior may appear there.

A generic incremental framework is not required.

---

## Required code philosophy

Students must directly see:

```text
how already-processed changes are excluded
how new records are identified
how changed records are identified
how unchanged records are identified
how the current state is rebuilt
how the checkpoint advances
why the rerun does nothing
```

Avoid abstractions such as:

```python
target = incremental_engine.upsert(batch)
```

before the actual mechanics have been demonstrated.

The classroom explanation should focus on:

* why full rebuilds may be unnecessary;
* why append is not equivalent to incremental processing;
* why business keys matter;
* why unchanged records should not produce updates;
* why progress must be persisted;
* why checkpoint advancement must follow successful processing;
* why rerunning a batch should be safe.

---

## Business-value comparison

Use only a few fields for change detection.

Recommended:

```text
customer_name
city
segment
```

Do not treat metadata such as:

```text
changed_at
```

as a business-value change.

Otherwise an unchanged customer would incorrectly become an UPDATE merely because the change record has a later source position.

---

## Upsert concept

Introduce:

```text
UPSERT
```

as the combined behavior:

```text
if key does not exist
→ INSERT

if key exists and values changed
→ UPDATE

if key exists and values did not change
→ UNCHANGED
```

Do not require database-specific:

```sql
MERGE
```

syntax.

The visible DataFrame logic is sufficient.

---

## Checkpoint

A checkpoint answers:

> Up to what source position has this pipeline completed processing successfully?

For this activity, it contains one timestamp.

Example:

```text
2026-09-16T10:30:00
```

Do not create:

* checkpoint databases;
* state-management frameworks;
* distributed checkpoint protocols.

---

## Source high-water mark

The source high-water mark is:

```text
max(changed_at)
```

among the successfully processed eligible changes.

It represents the highest source change position included in the completed run.

The pipeline persists that value in its checkpoint.

---

## Important distinction from streaming

This PRE must explicitly preserve the following distinction.

### Incremental source high-water mark

Used to answer:

> Which source changes have already been processed?

Example:

```text
changed_at <= checkpoint
→ already processed
```

### Streaming event-time watermark

Introduced later in `PRE_17`.

Used to answer:

> How far can event-time processing progress while accounting for late events?

These are related notions of progress but they solve different engineering problems.

Do not use the terms interchangeably.

---

## CDC concept

Briefly introduce Change Data Capture as a broader mechanism for obtaining changes from operational systems.

The workshop does **not** implement CDC.

The provided:

```text
customer_changes.parquet
```

simulates an already available change feed.

Do not introduce:

* Debezium;
* database transaction logs;
* Kafka;
* log sequence numbers;
* database triggers.

---

## Idempotency

For this PRE, the observable requirement is:

> Running the pipeline again with the same change batch after the checkpoint has advanced must not change the resulting customer state.

The expected rerun is:

```text
eligible changes = 0
```

No broader exactly-once architecture is required.

---

## Expected artifacts

### `submission/customers_current.parquet`

Required properties:

* one row per customer;
* original unchanged customers preserved;
* updated customer contains new values;
* new customer appears once;
* `customer_id` unique;
* deterministic ordering.

---

### `submission/incremental_report.csv`

Required columns:

```text
action
record_count
```

Required rows:

```text
INSERT
UPDATE
UNCHANGED
```

No additional submission artifact is required.

---

## Generated checkpoint

The execution may generate:

```text
temp/checkpoint.json
```

containing the persisted source high-water mark.

This is execution state, not a graded business-data artifact.

Its format should remain minimal and transparent.

Example:

```json
{
  "high_water_mark": "2026-09-16T10:30:00"
}
```

No execution timestamp should be added unless required, because deterministic output is preferred.

---

## Visible validation

Only two central validations are necessary.

### Validation 1 — Current-state grain

Verify:

```text
customer_id is unique
```

after applying the batch.

### Validation 2 — Safe rerun

Verify:

```text
same batch
+
new checkpoint
→
0 eligible rows
```

and that the current customer state remains logically identical.

---

## Required tests

Repository tests should verify:

1. `data/customers_current.parquet` exists.
2. `data/customer_changes.parquet` exists.
3. Initial `customer_id` values are unique.
4. Exactly one canonical change is classified as `INSERT`.
5. Exactly one is classified as `UPDATE`.
6. Exactly one is classified as `UNCHANGED`.
7. Updated customer receives the expected new values.
8. New customer is inserted exactly once.
9. Unchanged customer retains its existing business values.
10. Final `customer_id` values are unique.
11. Final row count is correct.
12. Checkpoint advances to the maximum successfully processed `changed_at`.
13. Checkpoint does not advance before successful state creation.
14. Reapplying the same batch after checkpoint advancement yields zero eligible rows.
15. Rerun preserves equivalent final logical state.
16. `submission/incremental_report.csv` exists.
17. Report counts match actual classification.
18. No streaming-watermark logic is introduced.

Tests should validate incremental semantics rather than implementation structure.

---

## What students should observe

The complete workshop should reduce to:

```text
current customers
+
change batch
↓
checkpoint filter
↓
INSERT / UPDATE / UNCHANGED
↓
new current state
↓
advance source high-water mark
↓
persist checkpoint
↓
rerun same batch
↓
nothing changes
```

The essential engineering insight is:

> Incremental processing updates only what is new or changed while remembering how far the source has already been processed.

---

## Boundaries

Do not introduce:

* streaming watermarks;
* delete events;
* multiple changes for the same key in one batch;
* historical customer versions;
* slowly changing dimensions;
* database `MERGE`;
* transaction-log CDC;
* Debezium;
* Kafka;
* exactly-once distributed processing;
* late-arriving events.

These concepts are unnecessary for the central lesson.

---

## Relationship with PRE_12

`PRE_12` establishes:

```text
Can I trust the structure of the incoming batch?
```

`PRE_13` establishes:

```text
Which incoming records actually change the current state?
```

---

## Relationship with PRE_14

`PRE_13` answers:

> How should the data itself be updated incrementally?

`PRE_14_pipeline_operations` will answer:

> How should multiple pipeline tasks be executed and recovered operationally?

Do not introduce orchestration here.

---

## Relationship with PRE_17

Terminology must remain intentionally distinct.

`PRE_13` uses:

```text
checkpoint
source high-water mark
```

for batch-incremental source progress.

`PRE_17` uses:

```text
watermark
```

for event-time progress under late-arriving streaming data.

This distinction must survive implementation.

---

## Acceptance criteria

The PRE is pedagogically acceptable only when:

1. The complete current state fits on screen.
2. The complete change batch fits on screen.
3. Exactly three meaningful change records are sufficient.
4. The notebook uses no more than 8 cells.
5. No code cell exceeds 12 effective lines.
6. Business key is explicit.
7. Checkpoint filtering is visible.
8. `INSERT`, `UPDATE`, and `UNCHANGED` are all visible.
9. Business values rather than metadata determine `UPDATE`.
10. The final state preserves one row per customer.
11. Source high-water mark advancement is explicit.
12. Checkpoint advancement occurs only after successful processing.
13. Reprocessing the same batch yields zero eligible changes.
14. CDC is introduced only conceptually.
15. The term `watermark` is reserved for streaming and does not appear as the incremental progress mechanism.
16. No database-specific incremental framework is required.
17. The instructor can focus on **why incremental processing differs from append and full rebuild**.
18. The activity complies with `AGENTS.md`.

---

## Agent implementation instructions

Do not implement while:

```text
Status: DRAFT
```

When implementation is later authorized:

* use exactly one `INSERT`, one `UPDATE`, and one `UNCHANGED` case;
* keep both datasets tiny;
* keep classification logic visible;
* compare only relevant business fields;
* use one simple timestamp checkpoint;
* persist the source high-water mark only after successful state creation;
* do not use the term `watermark` for incremental progress;
* do not add DELETE handling;
* do not add CDC infrastructure;
* do not add historical-version logic;
* do not hide incremental behavior before it has been demonstrated;
* preserve the 8-cell and 12-line hard limits.
