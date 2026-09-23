# PRE Specification

## Identification

**Activity:** `PRE_22_data_serving`

**Week:** 12

**Status:** `READY`

---

## Activity title

**Preparar datos para quien los va a consumir**

---

## Central engineering insight

Reliable curated data are not necessarily the final representation required by every consumer.

Different consumers may require:

* different grain;
* different columns;
* different access mechanisms.

The workshop should answer:

> How can one curated dataset be exposed through stable representations designed for different analytical consumers?

The central progression is:

```text
curated data
↓
consumer need
↓
choose grain
↓
shape serving dataset
↓
publish stable interface
```

The essential lesson is:

```text
curated for reuse
≠
served for consumption
```

---

## Course capability

Introduce only the minimum serving concepts required by the course:

* serving layer;
* consumer-oriented representation;
* serving grain;
* stable schema;
* detailed serving dataset;
* aggregated serving dataset;
* analytical mart;
* consumer interface;
* serving metadata.

The activity should not become an API-development workshop.

---

## Engineering problem

The retailer already has a reliable curated sales dataset.

Two consumers need it.

### Consumer 1 — Data analyst

Needs transaction-level data for flexible analysis.

### Consumer 2 — Dashboard

Needs only:

> Monthly sales by product category.

Giving both consumers the complete internal pipeline structure would unnecessarily couple them to implementation details.

Students must create stable serving representations for both needs.

---

## Minimal input dataset

Provide:

```text
data/sales_curated.parquet
```

Recommended size:

```text
20–30 transactions
```

covering:

```text
3 months
3–4 product categories
```

Required fields:

```text
transaction_id
transaction_date
customer_id
product_id
product_name
product_category
quantity
unit_price
sales_amount
```

The complete dataset should remain understandable.

---

## Consumer 1 serving representation

Create:

```text
submission/sales_detail.parquet
```

Required grain:

> One row per transaction.

Expose only stable consumer-facing fields:

```text
transaction_id
transaction_date
customer_id
product_id
product_name
product_category
quantity
sales_amount
```

Do not expose internal pipeline metadata.

---

## Consumer 2 serving representation

Create:

```text
submission/sales_serving.db
```

containing:

```text
monthly_category_sales
```

Required grain:

> One row per month and product category.

Required fields:

```text
year
month
product_category
transaction_count
units_sold
total_sales
```

This is the dashboard-oriented serving mart.

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

All important serving decisions must remain visible.

---

## Notebook progression

### Cell 1 — Inspect curated data

Load:

```text
data/sales_curated.parquet
```

Display its grain and fields.

State explicitly:

```text
current grain
=
one row per transaction
```

Central question:

> Is one reliable internal dataset necessarily the best interface for every consumer?

---

### Cell 2 — Define the two consumer needs

State the required grain for each consumer.

```text
analyst
→ one row per transaction

dashboard
→ one row per month and category
```

Show the fields each consumer needs.

Central discussion:

> Why should serving design begin with the consumer rather than with the storage technology?

No code-heavy modeling is required.

---

### Cell 3 — Build the detailed serving dataset

Select the stable transaction-level fields.

Persist:

```text
submission/sales_detail.parquet
```

Students should observe:

```text
curated dataset
→ explicit consumer-facing schema
```

No transformation beyond selection and ordering is necessary.

---

### Cell 4 — Build the dashboard mart

Derive:

```text
year
month
```

from `transaction_date`.

Aggregate by:

```text
year
month
product_category
```

Calculate only:

```text
transaction_count
units_sold
total_sales
```

Central idea:

> Serving grain follows the consumer question.

---

### Cell 5 — Publish the dashboard mart

Create:

```text
submission/sales_serving.db
```

and persist:

```text
monthly_category_sales
```

as a SQLite table.

The code should visibly show:

```text
serving DataFrame
→ stable SQL-accessible table
```

No database server is required.

---

### Cell 6 — Consume the two interfaces

Demonstrate exactly one read from each representation.

#### Analyst

Read:

```text
sales_detail.parquet
```

and inspect transactions.

#### Dashboard

Query:

```sql
SELECT *
FROM monthly_category_sales
ORDER BY year, month, product_category;
```

Central observation:

```text
same business data
↓
different consumer interfaces
```

---

### Cell 7 — Validate and generate the manifest

Validate:

```text
detail total sales
=
curated total sales

mart total sales
=
curated total sales
```

Generate:

```text
submission/serving_manifest.csv
```

Required columns:

```text
dataset
consumer
grain
format
location
```

Required rows:

```text
sales_detail
monthly_category_sales
```

No additional report is required.

---

## Optional eighth cell

Only if classroom time comfortably permits:

consolidate the already visible publishing logic into:

```text
src/serving.py
```

Suggested functions:

```text
build_sales_detail(...)
build_monthly_category_sales(...)
```

No new logic may appear there.

The notebook remains the pedagogical source.

---

## Required serving philosophy

Students must be able to answer for every served dataset:

```text
Who consumes it?
What does one row represent?
Which fields are exposed?
How is it accessed?
```

These questions are more important than the storage technology.

Classroom explanation should focus on:

* why curated and serving layers differ;
* why consumers may require different grains;
* why unnecessary internal fields should not become part of the consumer interface;
* why stable schemas reduce downstream coupling;
* why serving formats depend on access patterns.

---

## Stable schema

The detailed dataset intentionally exposes only:

```text
transaction_id
transaction_date
customer_id
product_id
product_name
product_category
quantity
sales_amount
```

Internal pipeline changes should not automatically alter this consumer-facing schema.

The central intuition is:

```text
internal implementation may evolve
while
consumer interface remains stable
```

Do not introduce formal schema versioning.

---

## Serving grain

The grain must be explicit before each serving representation is created.

### Detailed interface

```text
one transaction
```

### Dashboard interface

```text
one month × product category
```

This reinforces concepts introduced earlier in:

```text
PRE_02
PRE_04
```

without reteaching them.

---

## File versus SQL interface

The activity uses two simple access patterns.

### Parquet

Appropriate for:

```text
flexible analytical processing
```

### SQLite table

Appropriate for:

```text
simple SQL consumption
```

Do not imply that these are the only or universally preferred serving technologies.

They are transparent local teaching representations.

---

## Consumer coupling

Students should understand that exposing:

```text
temp/
raw/
staging/
internal pipeline columns
```

directly to consumers creates unnecessary dependency on implementation details.

Serving provides a deliberate boundary:

```text
internal pipeline
|
serving interface
|
consumer
```

---

## Expected artifacts

### `submission/sales_detail.parquet`

Required properties:

* one row per transaction;
* stable exposed schema;
* transaction identifiers unique;
* business totals preserved;
* deterministic logical content.

---

### `submission/sales_serving.db`

Must contain:

```text
monthly_category_sales
```

Required columns:

```text
year
month
product_category
transaction_count
units_sold
total_sales
```

Required grain:

> One row per year, month, and product category.

---

### `submission/serving_manifest.csv`

Required columns:

```text
dataset
consumer
grain
format
location
```

Required logical rows:

```text
sales_detail
monthly_category_sales
```

---

## Visible validation

Only two validations are required.

### Validation 1 — Detailed serving

Verify:

```text
curated total sales
=
sales_detail total sales
```

### Validation 2 — Aggregated serving

Verify:

```text
curated total sales
=
sum(monthly_category_sales.total_sales)
```

Thus:

```text
change of representation
≠
change of business facts
```

---

## Required tests

Repository tests should verify:

1. `data/sales_curated.parquet` exists.
2. `submission/sales_detail.parquet` exists.
3. Detailed required columns exist.
4. `transaction_id` is unique in detailed serving data.
5. Detailed row count matches curated transaction count.
6. Detailed total sales reconcile with curated data.
7. `submission/sales_serving.db` exists.
8. `monthly_category_sales` exists.
9. Required mart columns exist.
10. Mart grain is unique by year/month/category.
11. Mart total sales reconcile with curated data.
12. `submission/serving_manifest.csv` exists.
13. Exactly the required serving datasets are represented.
14. Locations are relative and deterministic.
15. Re-execution produces equivalent logical outputs.

Tests should validate serving contracts rather than implementation structure.

---

## What students should observe

The complete workshop should reduce to:

```text
one curated dataset
↓
two consumers
↓
two required grains
↓
detail Parquet
+
aggregated SQL mart
↓
stable serving interfaces
↓
reconciled business totals
```

The essential engineering insight is:

> Serving data means shaping reliable internal data around a consumer's access needs while preserving a stable boundary.

---

## Boundaries

Do not introduce:

* REST APIs;
* FastAPI;
* GraphQL;
* application backends;
* BI tools;
* semantic layers;
* OLAP servers;
* caching;
* serving infrastructure;
* authentication;
* authorization implementation;
* data-product SLAs.

These concepts are unnecessary for the central lesson or belong to the later Data Products course.

---

## Relationship with PRE_17

`PRE_17` establishes reliable derived analytical results.

`PRE_18` asks:

> How should reliable data be exposed to a downstream consumer?

---

## Relationship with PRE_19

`PRE_18` creates stable consumer-facing datasets.

`PRE_23_metadata_lineage` will ask:

> How do consumers and operators know what those datasets are, where they came from, and what depends on them?

---

## Relationship with Data Products

This PRE deliberately stops at:

```text
reliable consumer-facing data interface
```

It does not extend into:

```text
complete data product
```

which may additionally involve:

* product ownership;
* user experience;
* service-level objectives;
* APIs;
* monitoring;
* product lifecycle;
* business adoption.

Those concerns belong outside this course.

---

## Acceptance criteria

The PRE is pedagogically acceptable only when:

1. One curated dataset drives the entire activity.
2. Exactly two consumer needs are sufficient.
3. Exactly two serving representations are created.
4. The notebook uses no more than 8 cells.
5. Recommended implementation uses approximately 7 cells.
6. No code cell exceeds 12 effective lines.
7. Consumer and grain are explicit before implementation.
8. Detailed serving schema is intentionally selected.
9. Dashboard aggregation has an explicit grain.
10. Both interfaces can be consumed directly.
11. Both outputs reconcile with curated business totals.
12. No API or BI platform is required.
13. Serving is not presented as a complete data product.
14. The instructor can focus on **why consumer needs determine serving shape and interface**.
15. The activity complies with `AGENTS.md`.

---

## Agent implementation instructions

Do not implement while:

```text
Status: DRAFT
```

When implementation is later authorized:

* use one tiny deterministic curated dataset;
* use exactly two consumer personas;
* use exactly two serving representations;
* keep all schema and grain decisions visible;
* use Parquet and SQLite only as transparent teaching interfaces;
* do not introduce APIs;
* do not introduce dashboards;
* do not expand the activity into data-product design;
* do not hide publishing logic before it has been demonstrated;
* preserve the 8-cell and 12-line hard limits.
