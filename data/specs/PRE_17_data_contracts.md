# PRE Specification

## Identification

**Activity:** `PRE_24_data_contracts`

**Week:** 8

**Status:** `READY`

---

## Activity title

**Detectar cuándo un cambio rompe la interfaz de datos**

---

## Central engineering insight

A data consumer depends on assumptions about the structure it receives.

Those assumptions should be explicit.

The workshop should answer:

> How can a pipeline distinguish between a compatible change and a breaking change in incoming data?

The central progression is:

```text
expected structure
↓
incoming batch
↓
validate contract
↓
compatible / breaking
↓
accept / reject
```

The essential lesson is:

```text
schema changed
≠
schema broken
```

Some changes are compatible.

Others should stop the pipeline.

---

## Course capability

Introduce only the minimum contract concepts required later:

* expected fields;
* required versus optional fields;
* expected type;
* nullable versus non-nullable;
* allowed values;
* compatible change;
* breaking change;
* controlled rejection;
* quarantine.

The activity should not become a general schema-validation framework.

---

## Engineering problem

A customer-data producer sends a file to an analytical pipeline.

The consumer expects:

```text
customer_id
customer_name
segment
city
signup_date
```

One day, the producer changes the file.

Possible changes include:

* removing a required column;
* sending an incompatible value type;
* introducing an unsupported category;
* adding one new optional column.

Students must determine which changes can safely pass and which should be rejected.

---

## Minimal canonical dataset

Provide one valid customer batch:

```text
data/customers_valid.csv
```

Recommended size:

```text
6–10 customers
```

Required fields:

```text
customer_id
customer_name
segment
city
signup_date
```

The complete dataset should fit on screen.

---

## Minimal contract

The contract should remain small and visible.

### `customer_id`

```text
required: yes
nullable: no
unique: yes
```

### `customer_name`

```text
required: yes
nullable: no
```

### `segment`

```text
required: yes
nullable: no
allowed:
- Basic
- Premium
- Corporate
```

### `city`

```text
required: yes
nullable: no
```

### `signup_date`

```text
required: yes
type: date-compatible
```

Do not add more rules.

---

## Controlled change cases

Use exactly four cases.

### Case 1 — Missing required column

```text
segment removed
```

Expected:

```text
BREAKING
REJECT
```

---

### Case 2 — Incompatible date values

Example:

```text
signup_date = "not-a-date"
```

Expected:

```text
BREAKING
REJECT
```

---

### Case 3 — Unsupported category

Example:

```text
segment = "VIP"
```

Expected:

```text
BREAKING
REJECT
```

---

### Case 4 — Additional optional column

Example:

```text
preferred_language
```

Expected:

```text
COMPATIBLE
ACCEPT
```

These four cases are sufficient to establish the concept.

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

All contract logic must first be visible directly in the notebook.

---

## Notebook progression

### Cell 1 — Inspect the valid batch

Load:

```text
data/customers_valid.csv
```

Display the complete dataset.

Central question:

> What assumptions is the consumer making about this file?

Students should identify:

```text
expected columns
required values
allowed segment values
date field
```

---

### Cell 2 — Write the contract explicitly

Represent the consumer expectations in a small Python structure.

For example:

```python
required_columns = {
    "customer_id",
    "customer_name",
    "segment",
    "city",
    "signup_date",
}

allowed_segments = {
    "Basic",
    "Premium",
    "Corporate",
}
```

The contract must be understandable by reading the code.

Do not create a generic contract DSL.

---

### Cell 3 — Validate the canonical batch

Check:

```text
required columns present
customer_id not null
customer_id unique
segment allowed
signup_date parseable
```

The valid batch should produce:

```text
PASS
```

Central discussion:

> The contract makes assumptions executable.

---

### Cell 4 — Demonstrate a structural breaking change

Load or construct the version with:

```text
segment removed
```

Validate it against the same contract.

Expected result:

```text
FAIL
BREAKING
```

Central lesson:

> A required field disappearing changes the interface expected by the consumer.

---

### Cell 5 — Demonstrate semantic/type breaking changes

Evaluate two small cases:

```text
invalid signup_date
unsupported segment
```

Both should fail using the same contract.

No new validation framework should be introduced.

Central observation:

```text
column exists
≠
column satisfies contract
```

---

### Cell 6 — Demonstrate a compatible additive change

Load or construct a batch containing:

```text
preferred_language
```

in addition to all required fields.

Expected result:

```text
PASS
COMPATIBLE
```

Central discussion:

> Why does adding information not necessarily break an existing consumer?

This is the most important contrast in the PRE.

---

### Cell 7 — Quarantine breaking batches and report

For incompatible batches:

```text
REJECT
→ temp/quarantine/
```

Generate:

```text
submission/contract_report.csv
```

Required columns:

```text
batch_name
status
change_type
action
```

Required logical rows:

```text
valid
missing_required_column
invalid_date
unsupported_segment
extra_optional_column
```

No larger reporting structure is required.

---

## Optional eighth cell

Only if time comfortably permits:

consolidate the already visible validation logic into:

```text
src/contracts.py
```

Possible function:

```text
validate_customer_batch(...)
```

No new logic may appear there.

The notebook remains the pedagogical source.

---

## Required code philosophy

The contract must be readable without explanation.

Students should be able to infer:

```text
what fields are required
what values are allowed
what constitutes failure
```

directly from the code.

Avoid abstractions such as:

```python
contract_engine.validate(schema)
```

before students have seen the actual validation rules.

Classroom explanation should focus on:

* why producer and consumer need a stable interface;
* why compatible and breaking changes differ;
* why rejecting unexpected data can be safer than guessing;
* why schema evolution should be intentional.

---

## Contract versus quality

The distinction from `PRE_11` must remain explicit.

### `PRE_11`

Asks:

> Are the values in this batch acceptable?

Examples:

```text
quantity > 0
product exists
transaction_id unique
```

### `PRE_12`

Asks:

> Does this incoming dataset satisfy the interface the consumer expects?

Examples:

```text
required field exists
field is interpretable as expected
allowed semantic domain is preserved
```

Some mechanisms overlap.

The engineering intent differs.

---

## Controlled failure

Do not silently:

* recreate missing required fields;
* rename unexpected columns;
* coerce invalid dates into missing values;
* expand allowed categories automatically.

The rule is:

```text
unexpected breaking change
→ detect
→ reject
→ preserve for inspection
```

---

## Quarantine

Use:

```text
temp/quarantine/
```

Only breaking batches need to appear there.

The mechanism should be simple:

```text
copy rejected input
→ quarantine
```

No production quarantine architecture is required.

---

## Expected artifact

### `submission/contract_report.csv`

Required columns:

```text
batch_name
status
change_type
action
```

Suggested values:

### `status`

```text
PASS
FAIL
```

### `change_type`

```text
NONE
COMPATIBLE
BREAKING
```

### `action`

```text
ACCEPT
REJECT
```

Ordering must be deterministic.

---

## Visible validation

The notebook needs only two central comparisons.

### Breaking

```text
missing required column
→ FAIL
→ REJECT
```

### Compatible

```text
extra optional column
→ PASS
→ ACCEPT
```

These two cases should make the entire contract concept clear.

---

## Required tests

Repository tests should verify:

1. The valid batch passes.
2. Missing required column fails.
3. Invalid date fails.
4. Unsupported segment fails.
5. Extra optional column passes.
6. `customer_id` nullability is enforced.
7. `customer_id` uniqueness is enforced.
8. Breaking batches are quarantined.
9. Compatible batches are not quarantined.
10. `submission/contract_report.csv` exists.
11. Required report columns exist.
12. Report outcomes match actual validation behavior.
13. Re-execution produces equivalent logical results.

Tests should validate contract semantics rather than internal function structure.

---

## What students should observe

The complete workshop should reduce to:

```text
valid interface
↓
explicit contract
↓
breaking change
↓
FAIL
↓
compatible change
↓
PASS
↓
reject or accept
```

The essential engineering insight is:

> Data contracts make producer-consumer assumptions explicit and allow schema evolution to be handled intentionally.

---

## Boundaries

Do not introduce:

* Pydantic;
* Pandera;
* Great Expectations;
* Avro;
* Protobuf;
* Schema Registry;
* schema-version negotiation;
* contract registries;
* distributed governance;
* automated schema migration.

These are unnecessary for the central lesson.

---

## Relationship with PRE_11

`PRE_11` establishes:

```text
data quality expectations
```

`PRE_12` establishes:

```text
producer-consumer interface expectations
```

The distinction must remain visible.

---

## Relationship with PRE_13

`PRE_21_incremental_pipeline` depends on stable assumptions about:

```text
business keys
record shape
change representation
```

A contract helps make those assumptions explicit before incremental updates are applied.

---

## Acceptance criteria

The PRE is pedagogically acceptable only when:

1. The valid dataset fits on screen.
2. The contract contains only the minimum required expectations.
3. Exactly four change cases are sufficient.
4. The notebook uses no more than 8 cells.
5. No code cell exceeds 12 effective lines.
6. Contract logic is visible and readable.
7. One structural breaking change is demonstrated.
8. One semantic/type breaking change is demonstrated.
9. One compatible additive change is demonstrated.
10. Breaking batches are rejected.
11. Compatible batches are accepted.
12. Quarantine remains simple.
13. No schema-validation framework is required.
14. The instructor can focus on **why a change breaks or preserves the interface**.
15. The activity complies with `AGENTS.md`.

---

## Agent implementation instructions

Do not implement while:

```text
Status: DRAFT
```

When implementation is later authorized:

* use one tiny canonical customer dataset;
* use exactly four controlled change cases;
* keep contract rules explicit;
* do not create a generic validation framework;
* do not introduce external schema libraries;
* do not silently repair breaking changes;
* keep quarantine behavior minimal;
* do not hide contract logic before it has been shown;
* preserve the 8-cell and 12-line hard limits.
