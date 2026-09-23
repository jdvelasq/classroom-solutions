# PRE Specification

## Identification

**Activity:** `PRE_23_data_quality`

**Week:** 8

**Status:** `READY`

---

## Activity title

**Detectar datos que no deberían pasar**

---

## Central engineering insight

Successful execution does not guarantee acceptable data.

The workshop should answer:

> How can a pipeline decide automatically whether a batch is good enough to continue?

The central progression is:

```text
data
↓
expectation
↓
check
↓
violations
↓
PASS / FAIL
```

The essential lesson is:

```text
software success
≠
data quality
```

---

## Course capability

Introduce the minimum data-quality concepts required by later pipeline work:

* completeness;
* validity;
* uniqueness;
* consistency;
* freshness;
* explicit quality rules;
* violation counts;
* quality gate.

The activity should not become a general data-cleaning workshop.

---

## Engineering problem

A transaction batch loads successfully.

However, it contains a few controlled problems:

* one missing customer identifier;
* one invalid quantity;
* one duplicated transaction identifier;
* one unknown product;
* one transaction outside the expected batch date.

Nothing prevents pandas from loading the file.

The pipeline therefore needs explicit quality checks.

---

## Minimal input data

Provide:

```text
data/transactions.parquet
data/products.parquet
```

Recommended transaction size:

```text
10–15 rows
```

Recommended product size:

```text
4–6 rows
```

The complete datasets should fit comfortably on screen.

---

## Required controlled violations

The transaction dataset should contain exactly one clear example of each core problem.

### Completeness

```text
customer_id = missing
```

### Validity

```text
quantity <= 0
```

### Uniqueness

```text
duplicated transaction_id
```

### Consistency

```text
product_id not present in products
```

### Freshness

```text
transaction_date outside expected batch date
```

The defects should be deliberately simple and easy to identify visually.

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

All quality rules must first be visible directly in the notebook.

---

## Notebook progression

### Cell 1 — Inspect the defective batch

Load:

```text
transactions
products
```

Display the complete transaction batch.

Central question:

> The file loaded. Does that mean the batch is acceptable?

Students should be able to spot some defects visually.

---

### Cell 2 — Completeness and validity

Implement two simple checks:

```text
customer_id must be present
quantity must be > 0
```

Show:

```text
number of violations
```

for each rule.

Central discussion:

> What makes a rule explicit rather than subjective?

---

### Cell 3 — Uniqueness

Check:

```text
transaction_id
```

for duplicates.

Show directly:

```text
row count
distinct transaction_id count
duplicate count
```

Central lesson:

> A duplicated business identifier may preserve valid-looking rows while violating the intended grain.

---

### Cell 4 — Consistency

Verify that every:

```text
transactions.product_id
```

exists in:

```text
products.product_id
```

Expose the unknown product identifier.

Central discussion:

> Why can a value be valid by itself but inconsistent with another dataset?

---

### Cell 5 — Freshness

Define one expected processing date.

For example:

```text
expected_date = 2026-09-15
```

Check that every transaction belongs to that expected date.

Expose the out-of-period record.

No SLA logic is required.

---

### Cell 6 — Build the canonical quality report and gate

Combine the five checks into:

```text
submission/quality_report.csv
```

Required columns:

```text
rule_name
dimension
violations
status
```

Required dimensions:

```text
completeness
validity
uniqueness
consistency
freshness
```

Allowed status values:

```text
PASS
FAIL
```

The canonical report **must correspond to the original defective batch**.

Because the source intentionally contains one violation of every rule, the expected canonical report shows the corresponding failures.

Define the overall batch decision:

```text
all rules PASS
→ batch PASS

any required rule FAIL
→ batch FAIL
```

For the canonical defective batch:

```text
batch status = FAIL
```

This report must not later be overwritten.

---

### Cell 7 — Correct the controlled defects and rerun

Create a corrected copy of the batch programmatically.

Apply **exactly the same five rules**.

Students should observe:

```text
same rules
+
different data
→
different result
```

The corrected batch should produce:

```text
all rules PASS
→ batch PASS
```

Display this second result in the notebook.

Do **not** overwrite:

```text
submission/quality_report.csv
```

The corrected execution exists to demonstrate that the rules respond to the data rather than being changed to obtain a passing result.

---

## Optional eighth cell

Only if time comfortably permits:

consolidate the already visible checks into:

```text
src/quality.py
```

Suggested simple functions:

```text
check_completeness(...)
check_validity(...)
check_uniqueness(...)
check_consistency(...)
check_freshness(...)
```

If used, no new logic may appear here.

For this PRE, consolidation may also be omitted if it reduces notebook clarity.

---

## Required code philosophy

Each rule should be obvious from the code.

For example:

```python
missing_customer_count = (
    transactions["customer_id"].isna().sum()
)
```

and:

```python
invalid_quantity_count = (
    (transactions["quantity"] <= 0).sum()
)
```

The instructor should not need to explain what the expression does.

Classroom explanation should focus on:

* why that condition represents a quality expectation;
* why the rule matters to downstream processing;
* why violation counts are evidence;
* why a pipeline may stop even when no software exception occurred.

---

## Rule philosophy

Use exactly one clear rule per quality dimension.

Do not create:

* dozens of checks;
* weighted scores;
* quality percentages;
* anomaly models;
* complex threshold systems.

The workshop should establish the engineering pattern:

```text
expectation
→ measurement
→ decision
```

---

## Canonical artifact policy

The activity intentionally demonstrates two executions:

```text
defective batch
→ FAIL

corrected batch
→ PASS
```

Only the first execution produces the canonical graded artifact:

```text
submission/quality_report.csv
```

Therefore:

```text
quality_report.csv
=
evidence that the quality rules detect the designed defects
```

The second execution must remain visible in the notebook but must not replace the canonical report.

This removes ambiguity from grading and automated testing.

---

## Overall gate

The batch-level decision remains binary:

```text
PASS
```

or:

```text
FAIL
```

No partial scoring is required.

The important idea is:

> Quality rules can control whether downstream processing proceeds.

---

## Visible validation

The notebook should visibly demonstrate two states.

### Defective batch

```text
five controlled violations
↓
quality report
↓
batch FAIL
```

### Corrected batch

```text
same five rules
+
corrected values
↓
zero violations
↓
batch PASS
```

The rules themselves must not change.

---

## Expected artifact

### `submission/quality_report.csv`

This artifact **must describe the original defective batch**.

Required columns:

```text
rule_name
dimension
violations
status
```

Required properties:

* one row per core rule;
* all five dimensions represented;
* each controlled defect detected;
* violation counts correct;
* status derived programmatically;
* overall canonical batch status is `FAIL`;
* deterministic ordering.

The corrected-batch result is instructional output only and does not overwrite this artifact.

---

## Required tests

Repository tests should verify:

1. Required input datasets exist.
2. The completeness violation is detected.
3. The validity violation is detected.
4. The duplicate identifier is detected.
5. The unknown product is detected.
6. The freshness violation is detected.
7. The defective batch fails the gate.
8. The corrected batch passes the same gate.
9. `submission/quality_report.csv` exists.
10. The canonical report corresponds to the defective batch.
11. Required report columns exist.
12. All five dimensions are represented.
13. Each canonical rule contains the expected violation count.
14. Canonical status values correctly reflect those violations.
15. The corrected demonstration does not overwrite the canonical report.
16. Re-execution produces equivalent logical results.

Tests should validate the rules, not a specific internal implementation.

---

## What students should observe

The complete workshop should reduce to:

```text
batch loads
↓
quality defects exist
↓
five explicit rules
↓
violations detected
↓
batch FAIL
↓
correct data
↓
same rules
↓
batch PASS
```

The essential engineering insight is:

> Data quality becomes actionable when expectations are explicit and executable.

---

## Boundaries

Do not introduce:

* Great Expectations;
* Soda;
* Monte Carlo;
* probabilistic anomaly detection;
* statistical drift;
* data profiling frameworks;
* broad cleaning pipelines;
* schema contracts;
* quarantine architecture;
* observability platforms.

Those topics are unnecessary here or belong later.

---

## Relationship with PRE_10

`PRE_10` establishes:

```text
reproducible pipeline
```

`PRE_11` adds:

```text
quality gate
```

The conceptual progression is:

```text
pipeline runs
↓
data checked
↓
pipeline may continue or stop
```

---

## Relationship with PRE_12

`PRE_11` asks:

> Are the values in this batch acceptable?

`PRE_24_data_contracts` asks:

> Does the incoming data satisfy the interface expected by the consumer?

The two workshops must remain clearly distinct.

---

## Acceptance criteria

The PRE is pedagogically acceptable only when:

1. The entire defective batch fits on screen.
2. Exactly five core quality dimensions are used.
3. Each dimension has one simple visible rule.
4. The notebook uses no more than 8 cells.
5. No code cell exceeds 12 effective lines.
6. Quality logic is visible and readable.
7. The original defective batch clearly fails.
8. `submission/quality_report.csv` preserves that failing evidence.
9. A corrected batch passes using exactly the same rules.
10. The corrected execution does not overwrite the canonical artifact.
11. The quality gate is explicit.
12. No quality framework is required.
13. The activity does not become a data-cleaning workshop.
14. The instructor can focus on **why each expectation matters**, not on explaining complex code.
15. The activity complies with `AGENTS.md`.

---

## Agent implementation instructions

Do not implement while:

```text
Status: DRAFT
```

When implementation is later authorized:

* use a tiny deterministic batch;
* include exactly one obvious violation per core quality dimension;
* keep every rule visible;
* generate `submission/quality_report.csv` from the defective batch;
* never overwrite that artifact with the corrected-batch result;
* apply exactly the same rules to the corrected batch;
* do not add scoring systems;
* do not introduce a data-quality framework;
* do not hide checks in helpers before they have been shown;
* preserve the 8-cell and 12-line hard limits.
