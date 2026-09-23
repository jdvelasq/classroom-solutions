# PRE Specification

## Identification

**Activity:** `PRE_22_pipeline_operations`

**Week:** 9

**Status:** `READY`

---

## Activity title

**Operar un pipeline cuando algo falla**

---

## Central engineering insight

A pipeline is not only a collection of transformation functions.

In operation, tasks:

* depend on previous tasks;
* may succeed or fail;
* should not execute when an upstream dependency failed;
* may deserve retry when the failure is transient;
* should not be retried blindly when the failure is deterministic;
* must record what happened.

The workshop should answer:

> How should a pipeline execute several dependent tasks when one of them fails?

The central progression is:

```text
tasks
↓
dependencies
↓
execute in order
↓
transient failure → retry
or
deterministic failure → stop
↓
SUCCESS / FAILED / SKIPPED
↓
execution history
```

The essential lesson is:

```text
pipeline logic
≠
pipeline operation
```

---

## Course capability

Introduce only the minimum operational concepts required for a data pipeline:

* task;
* dependency;
* DAG intuition;
* run;
* processing date;
* task status;
* transient failure;
* bounded retry;
* deterministic failure;
* downstream skip;
* execution history;
* backfill intuition.

No external orchestration platform is required.

---

## Engineering problem

A daily sales pipeline contains four tasks:

```text
extract
↓
validate
↓
transform
↓
publish
```

The pipeline is executed for one processing date.

Normally all tasks succeed.

However, two different failure types must be handled correctly.

### Operational transient failure

The source is temporarily unavailable during:

```text
extract
```

A retry may succeed.

### Deterministic data failure

The extracted batch violates a required validation rule.

Repeating the same validation over the same data will not fix the problem.

Downstream tasks should not run.

---

## Minimal pipeline

Use exactly four tasks.

### `extract`

Loads the input batch for the selected processing date.

This is the only task with a controlled transient failure.

---

### `validate`

Checks one simple deterministic data rule.

Recommended rule:

```text
transaction_id must be unique
```

or another equally clear condition.

A failed validation should not be retried in the canonical example.

---

### `transform`

Creates one simple analytical result.

The transformation itself should remain trivial.

---

### `publish`

Writes the final output.

The subject of the PRE is operation, not transformation complexity.

---

## Dependency structure

The complete dependency graph is:

```text
extract
   ↓
validate
   ↓
transform
   ↓
publish
```

This is a valid DAG even though it is linear.

Introduce:

```text
Directed Acyclic Graph
```

only as the term for an explicit dependency graph.

Do not add parallel branches merely to make the example look more sophisticated.

---

## Processing date

Each run must receive explicitly:

```text
processing_date
```

Example:

```text
2026-09-15
```

The same pipeline code should execute for another date by changing only this value.

Central idea:

```text
pipeline code
+
processing date
=
specific pipeline run
```

---

## Controlled execution scenarios

Use exactly three canonical runs.

### Run A — Happy path

```text
extract     SUCCESS
validate    SUCCESS
transform   SUCCESS
publish     SUCCESS
```

---

### Run B — Transient operational failure

```text
extract attempt 1 → FAILED
extract attempt 2 → SUCCESS
validate          → SUCCESS
transform         → SUCCESS
publish           → SUCCESS
```

This demonstrates bounded retry.

---

### Run C — Deterministic validation failure

```text
extract     → SUCCESS
validate    → FAILED
transform   → SKIPPED
publish     → SKIPPED
```

No retry of `validate` is required.

This demonstrates dependency-based stopping.

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

All central operational logic must first remain visible in the notebook.

---

## Notebook progression

### Cell 1 — Define the four tasks

Implement simple functions:

```text
extract(...)
validate(...)
transform(...)
publish(...)
```

Each task should have an obvious input and output.

Keep internal business logic minimal.

Central discussion:

> What makes these four functions separate operational tasks rather than one long script?

---

### Cell 2 — Execute the happy path

Run:

```text
extract
→ validate
→ transform
→ publish
```

for one processing date.

Show:

```text
extract     SUCCESS
validate    SUCCESS
transform   SUCCESS
publish     SUCCESS
```

Students should first understand normal execution.

---

### Cell 3 — Make dependencies and statuses explicit

Represent task order explicitly.

Required statuses:

```text
SUCCESS
FAILED
SKIPPED
```

The execution rule should be visible:

```text
run task
only if upstream task succeeded
```

Central lesson:

> Execution order should follow dependencies, not accidental notebook order.

---

### Cell 4 — Demonstrate transient failure and retry

Configure:

```text
extract
attempt 1 → FAILED
attempt 2 → SUCCESS
```

Use:

```text
max_attempts = 2
```

Then continue normally:

```text
validate  → SUCCESS
transform → SUCCESS
publish   → SUCCESS
```

Central discussion:

> Why can retry make sense when the failure is temporary and external to the data logic?

Examples of transient operational causes may include:

```text
temporary source unavailability
temporary file lock
temporary connection failure
```

Only one simulated cause is required.

---

### Cell 5 — Demonstrate deterministic validation failure

Use another processing date whose extracted batch violates the selected validation rule.

Expected:

```text
extract     → SUCCESS
validate    → FAILED
transform   → SKIPPED
publish     → SKIPPED
```

Do not retry `validate`.

Central discussion:

> If the data themselves violate the rule, what would repeating exactly the same validation accomplish?

The required observation is:

```text
transient operational failure
may deserve retry

deterministic data failure
requires correction or intervention
```

This distinction is the key conceptual improvement of the PRE.

---

### Cell 6 — Execute a historical processing date

Run the same pipeline code for one previous date.

Example:

```text
2026-09-14
```

Introduce:

```text
backfill
```

as:

> Executing the same pipeline for a historical processing period.

No scheduler is required.

No multi-date loop is required.

---

### Cell 7 — Generate execution history

Create:

```text
submission/run_history.csv
```

Required columns:

```text
processing_date
task
attempt
status
```

The history should contain the canonical runs demonstrated in the activity.

Ordering must be deterministic.

---

## Optional eighth cell

Only if classroom time comfortably permits:

consolidate the already visible operational logic into:

```text
src/orchestrator.py
```

Suggested functions:

```text
run_task(...)
run_pipeline(...)
```

No new retry or dependency behavior may appear only after consolidation.

---

## Required operational philosophy

Students must directly see:

```text
which task is running
what it depends on
whether it succeeded
whether it was retried
why another task was skipped
```

Do not begin with:

```python
orchestrator.run(dag)
```

if that hides the mechanics being taught.

The classroom explanation should focus on:

* why task boundaries matter;
* why dependencies determine execution;
* why retry belongs only to suitable failure modes;
* why deterministic failures should not be retried blindly;
* why downstream tasks should not run after upstream failure;
* why execution history matters;
* why the same pipeline may need to run for another processing date.

---

## Failure taxonomy

Use only two failure classes.

### Transient operational failure

Example:

```text
source temporarily unavailable
```

Expected response:

```text
bounded retry
```

---

### Deterministic validation failure

Example:

```text
duplicate transaction_id
```

Expected response:

```text
FAIL
↓
downstream SKIPPED
```

No retry.

This is sufficient.

Do not create a full exception taxonomy.

---

## Retry policy

Use:

```text
max_attempts = 2
```

only for the controlled transient `extract` failure.

Required behavior:

```text
attempt 1 → FAILED
attempt 2 → SUCCESS
```

Do not introduce:

* exponential backoff;
* jitter;
* retry delays;
* exception hierarchies;
* circuit breakers.

The lesson is:

```text
retry is a response to a failure mode
not a universal reaction to failure
```

---

## Validation failure policy

The canonical validation task should be deterministic.

If the batch violates its rule:

```text
validate → FAILED
```

then:

```text
transform → SKIPPED
publish   → SKIPPED
```

The same invalid batch should not be automatically retried.

The next action conceptually would be:

```text
correct or replace the input
then run again
```

but implementing that recovery workflow is outside this PRE.

---

## Task statuses

Use exactly:

```text
SUCCESS
FAILED
SKIPPED
```

Do not add:

* RETRYING;
* QUEUED;
* RUNNING;
* CANCELLED;
* UPSTREAM_FAILED.

Attempts already make retry visible.

The status model should remain minimal.

---

## Scheduling concept

Explain conceptually:

```text
run this pipeline every day
```

but do not implement:

* cron;
* Airflow scheduling;
* Prefect;
* Dagster;
* cloud schedulers.

The processing date is enough to connect:

```text
scheduled period
and
pipeline run
```

---

## Backfill concept

A backfill in this PRE means:

```text
run the same pipeline
for a historical processing_date
```

No separate algorithm is required.

The important observation is:

```text
same pipeline code
+
different historical date
```

---

## DAG concept

Introduce a DAG as a representation of task dependencies.

The classroom graph remains intentionally:

```text
extract
↓
validate
↓
transform
↓
publish
```

Do not add branching just to demonstrate graph terminology.

Students need the dependency principle, not graph complexity.

---

## Expected artifact

### `submission/run_history.csv`

Required columns:

```text
processing_date
task
attempt
status
```

Allowed statuses:

```text
SUCCESS
FAILED
SKIPPED
```

The artifact must preserve enough evidence to reconstruct:

* happy-path execution;
* transient extraction failure and retry;
* deterministic validation failure;
* downstream skipping;
* historical execution.

---

## Visible validation

Only two operational validations are required.

### Validation 1 — Retry behavior

Verify:

```text
extract attempt 1 FAILED
extract attempt 2 SUCCESS
```

and downstream tasks subsequently succeed.

### Validation 2 — Deterministic failure behavior

Verify:

```text
validate FAILED
→
transform SKIPPED
→
publish SKIPPED
```

No retry occurs for the validation task.

---

## Required tests

Repository tests should verify:

1. Exactly four canonical tasks exist logically.
2. Tasks execute in dependency order.
3. Happy-path execution succeeds.
4. Controlled transient `extract` failure occurs.
5. `extract` is retried only within the permitted attempt count.
6. Successful extraction retry allows downstream tasks to execute.
7. Controlled deterministic validation failure occurs.
8. Validation failure is not retried automatically.
9. `transform` becomes `SKIPPED` after validation failure.
10. `publish` becomes `SKIPPED` after validation failure.
11. Historical processing date can be executed with the same task logic.
12. `submission/run_history.csv` exists.
13. Required columns exist.
14. Only valid status values appear.
15. Attempt counts match actual execution.
16. Ordering is deterministic.

Tests should validate operational behavior rather than implementation framework.

---

## What students should observe

The complete workshop should reduce to:

```text
four dependent tasks
↓
successful run
↓
temporary extract failure
↓
retry succeeds
↓
bad data
↓
validation fails
↓
downstream skipped
↓
historical run
↓
execution history
```

The essential engineering insight is:

> Operating a pipeline means responding differently to different failure modes while respecting task dependencies.

---

## Boundaries

Do not introduce:

* Apache Airflow;
* Prefect;
* Dagster;
* Luigi;
* cron implementation;
* distributed task queues;
* parallel branches;
* sensors;
* SLAs;
* alerting systems;
* worker pools;
* production observability;
* complex retry policies;
* automated data remediation.

These are unnecessary for the central lesson.

---

## Relationship with PRE_13

`PRE_13` asks:

> Which data records need to change?

`PRE_14` asks:

> Which pipeline tasks should execute, retry, stop, or be skipped?

The distinction is:

```text
data state
≠
execution state
```

---

## Relationship with PRE_11

`PRE_11` already established:

```text
invalid data
→ quality gate FAIL
```

`PRE_14` now adds the operational consequence:

```text
validation task FAIL
→ dependent tasks SKIPPED
```

The quality rule itself is not retaught here.

---

## Relationship with PRE_15

`PRE_14` executes tasks locally and sequentially.

`PRE_23_distributed_processing` asks:

> What changes when the computation inside a data-processing task is divided across partitions?

Do not introduce distributed execution here.

---

## Acceptance criteria

The PRE is pedagogically acceptable only when:

1. Exactly four tasks are sufficient.
2. Task business logic remains trivial.
3. The notebook uses no more than 8 cells.
4. No code cell exceeds 12 effective lines.
5. Processing date is explicit.
6. Dependency order is explicit.
7. `SUCCESS`, `FAILED`, and `SKIPPED` are observable.
8. Exactly one transient operational failure is demonstrated.
9. The transient failure occurs in `extract`.
10. Retry is bounded.
11. Exactly one deterministic validation failure is demonstrated.
12. Validation failure is not retried automatically.
13. Downstream tasks are skipped after validation failure.
14. One historical processing date demonstrates backfill.
15. Execution history is persisted.
16. No orchestration framework is required.
17. The instructor can focus on **why different failure modes require different operational responses**.
18. The activity complies with `AGENTS.md`.

---

## Agent implementation instructions

Do not implement while:

```text
Status: DRAFT
```

When implementation is later authorized:

* use exactly four small tasks;
* keep the dependency graph linear;
* use exactly one deterministic transient failure in `extract`;
* allow exactly one retry of that failure;
* use exactly one deterministic validation failure;
* do not retry the deterministic validation failure;
* represent `SUCCESS`, `FAILED`, and `SKIPPED` explicitly;
* use one historical processing date for backfill;
* do not add Airflow or another orchestration framework;
* do not add scheduling infrastructure;
* do not hide operational logic before it has been demonstrated;
* preserve the 8-cell and 12-line hard limits.
