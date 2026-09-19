# PRE Specification

## Identification

**Activity:** `PRE_03_sql_transformation`

**Week:** 4

**Status:** `READY`

---

## Activity title

**Transformar datos con SQL**

---

## Central engineering insight

Operational or staging data are often not directly suitable for analytics.

SQL can transform them into a stable analytical representation by making explicit decisions about:

* types;
* missing values;
* inconsistent categories;
* multiple versions of the same entity.

The workshop should answer:

> How do we transform several imperfect records about the same customer into one clean current representation?

The central lesson is:

```text
duplicate rows
≠
multiple versions of the same entity
```

and therefore:

```text
DISTINCT
≠
deduplication by business rule
```

---

## Course capability

Introduce SQL transformation through one compact case involving:

* `CAST`;
* `NULLIF`;
* `CASE`;
* CTE;
* `ROW_NUMBER()`;
* deterministic deduplication;
* derived table or view.

These features must appear because they solve the customer-curation problem.

They must not be presented as an independent SQL feature catalog.

---

## Engineering problem

An operational system periodically exports customer records.

A customer may appear more than once because the source retains different versions.

The staging table also contains minor inconsistencies such as:

* blank values;
* inconsistent segment labels;
* numeric values stored as text.

The analytical system needs:

```text
one current record per customer
```

with standardized values.

---

## Minimal input database

Provide:

```text
data/customers_staging.db
```

with one table:

```text
customer_staging
```

Recommended size:

```text
10–15 rows
6–8 customers
```

The complete table must fit comfortably on screen.

Suggested columns:

```text
record_id
customer_id
customer_name
city
segment
age
updated_at
```

Use only a few deliberately controlled inconsistencies.

For example:

```text
segment:
"Premium"
"premium"
"CORPORATE"
""

age:
"42"
"35"
""
```

At least two customers must have multiple versions.

---

## Version example

A customer might appear as:

```text
record_id  customer_id  city       segment   age  updated_at
7          C003         Medellín   premium   41   2026-08-01
11         C003         Medellín   Premium   42   2026-09-10
```

The intended analytical representation is the most recent version:

```text
C003  Medellín  Premium  42
```

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

All essential SQL transformation logic must remain visible.

`src/` is not required.

---

## Notebook progression

### Cell 1 — Inspect the staging table

Load and display the complete table.

Students should directly see:

* repeated `customer_id`;
* multiple `updated_at` values;
* inconsistent segment values;
* blank age values.

Central discussion:

> Why is this table not yet a reliable customer dimension?

---

### Cell 2 — Show why `DISTINCT` is insufficient

Execute a query using:

```sql
SELECT DISTINCT ...
```

and show that multiple rows for the same `customer_id` remain because they represent different versions.

Central observation:

```text
DISTINCT removes identical rows.

It does not decide which version of an entity is current.
```

---

### Cell 3 — Standardize values

Use a single readable query containing:

```sql
CASE
NULLIF
CAST
```

For example:

```sql
SELECT
    customer_id,
    customer_name,
    city,
    CASE
        WHEN LOWER(segment) = 'premium' THEN 'Premium'
        WHEN LOWER(segment) = 'corporate' THEN 'Corporate'
        ELSE 'Basic'
    END AS segment,
    CAST(NULLIF(age, '') AS INTEGER) AS age,
    updated_at
FROM customer_staging;
```

The exact code may be refined while preserving its simplicity.

Central discussion:

> Why should these transformations be explicit instead of left to downstream analysts?

---

### Cell 4 — Rank customer versions

Use:

```sql
ROW_NUMBER()
```

with:

```sql
PARTITION BY customer_id
ORDER BY updated_at DESC, record_id DESC
```

The result should visibly assign:

```text
1 = most recent version
2 = older version
```

for customers with history.

Central concept:

> Deduplication requires a rule for deciding which record wins.

---

### Cell 5 — Build the curated result with a CTE

Combine standardization and ranking using one CTE.

Filter:

```text
row_number = 1
```

to produce:

```text
one row per customer
```

The CTE should make the transformation easier to read, not more abstract.

---

### Cell 6 — Create the curated view

Create:

```text
customer_curated
```

as a SQL view containing the final transformation.

The view makes the analytical representation reusable without duplicating the transformation query.

The working database may be created under:

```text
temp/customers_curated.db
```

Do not modify the canonical input database in `data/`.

---

### Cell 7 — Validate and export

Validate:

```text
one row per customer
```

and confirm that controlled customers contain their expected most recent values.

Export:

```text
submission/customers_curated.csv
```

No additional notebook section is required.

---

## Required SQL philosophy

The SQL must be visible and readable.

Prefer explicit intermediate reasoning over compressed queries.

The student should be able to determine from the SQL:

```text
how blank values are handled
how categories are standardized
how types are converted
how the latest record is chosen
```

without requiring the instructor to translate the code line by line.

Classroom explanation should focus on:

* why staging data require transformation;
* why missing and categorical values need explicit treatment;
* why `DISTINCT` is not sufficient;
* why deduplication requires a deterministic business rule;
* why a view can expose a stable analytical representation.

---

## Deterministic deduplication

The deduplication order must be deterministic.

Use:

```sql
ORDER BY updated_at DESC, record_id DESC
```

so that two records with the same timestamp still have a defined winner.

Do not rely on unspecified database row order.

---

## Missing-value treatment

Keep missing-value treatment deliberately small.

One example is sufficient:

```text
age = ""
↓
NULL
```

using:

```sql
NULLIF(age, '')
```

Do not turn this PRE into a general data-cleaning workshop.

---

## Type conversion

One visible conversion is sufficient.

Recommended:

```text
age stored as TEXT
↓
age stored analytically as INTEGER
```

Do not introduce complicated malformed-number parsing.

The objective is to make explicit that staging types and analytical types may differ.

---

## Category standardization

Use one field only.

Recommended:

```text
segment
```

Examples:

```text
premium
Premium
PREMIUM
```

should become:

```text
Premium
```

Do not standardize several unrelated columns.

---

## Expected artifact

### `submission/customers_curated.csv`

Required fields:

```text
customer_id
customer_name
city
segment
age
updated_at
```

Required grain:

> One row per customer.

Required properties:

* `customer_id` unique;
* latest customer version retained;
* segments standardized;
* blank ages represented as missing;
* age represented numerically where present;
* deterministic ordering.

---

## Visible validation

Only two visible validations are necessary.

### Validation 1 — Grain

Verify:

```text
number of rows
=
number of distinct customer_id values
```

### Validation 2 — Version selection

Select one customer known to have multiple versions and verify that the retained row is the expected most recent one.

---

## Required tests

Repository tests should verify:

1. `data/customers_staging.db` exists.
2. `customer_staging` exists.
3. `submission/customers_curated.csv` exists.
4. Required columns exist.
5. `customer_id` is unique.
6. Output contains one row per source customer.
7. Controlled segment variants are standardized correctly.
8. Blank age becomes missing.
9. Non-missing age values are numeric.
10. Controlled duplicated customers retain the expected latest version.
11. Tie-breaking with `record_id` is deterministic.
12. Output ordering is deterministic.

Tests should validate transformation semantics rather than exact SQL formatting.

---

## What students should observe

The complete workshop should reduce to:

```text
staging table
↓
inconsistent values
↓
DISTINCT does not solve entity versions
↓
standardize
↓
rank versions
↓
keep latest
↓
curated view
```

The essential engineering idea is:

> Curated data are produced by explicit and reproducible transformation rules.

---

## Boundaries

Do not introduce:

* general-purpose data-cleaning frameworks;
* fuzzy matching;
* entity resolution;
* advanced missing-data treatment;
* multiple window functions;
* slowly changing dimensions;
* incremental processing;
* data-quality frameworks;
* data contracts;
* dbt;
* stored procedures.

These topics belong later or outside the activity.

---

## Relationship with PRE_02

`PRE_02` focuses on:

```text
integrating tables while preserving analytical grain
```

`PRE_03` focuses on:

```text
transforming imperfect staging records into a stable analytical representation
```

---

## Relationship with PRE_04

The curated customer representation prepares the transition toward analytical storage.

`PRE_04` will ask:

> How should operational data be reorganized for repeated analytical use?

Do not introduce warehouse modeling here.

---

## Acceptance criteria

The PRE is pedagogically acceptable only when:

1. The entire staging table fits comfortably on screen.
2. One customer-curation problem drives the complete workshop.
3. The notebook uses no more than 8 cells.
4. No code cell exceeds 12 effective lines.
5. All central SQL logic is visible.
6. `DISTINCT` is shown to be insufficient for version deduplication.
7. One explicit missing-value treatment is demonstrated.
8. One explicit type conversion is demonstrated.
9. One categorical standardization is demonstrated.
10. `ROW_NUMBER()` implements deterministic version selection.
11. A CTE makes the final transformation readable.
12. A view exposes the curated representation.
13. The final output has one row per customer.
14. The instructor can explain **why each transformation is necessary** instead of explaining obscure SQL syntax.
15. The activity complies with `AGENTS.md`.

---

## Agent implementation instructions

Do not implement while:

```text
Status: DRAFT
```

When implementation is later authorized:

* use a very small staging dataset;
* keep all transformation logic visible in the notebook;
* use only one example for each transformation phenomenon;
* do not add additional cleaning cases;
* do not hide SQL in external files or helper functions;
* do not expand the PRE into a general data-cleaning exercise;
* preserve the 8-cell and 12-line hard limits.
