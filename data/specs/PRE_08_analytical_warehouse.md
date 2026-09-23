# PRE Specification

## Identification

**Activity:** `PRE_24_analytical_warehouse`

**Week:** 4

**Status:** `READY`

---

## Activity title

**De datos operacionales a datos analíticos**

---

## Central engineering insight

An operational relational model and an analytical model organize the same business information for different purposes.

Operational data are organized around business transactions and entities.

Analytical data are reorganized around an explicit analytical grain.

The workshop should answer:

> Why would we reorganize data that are already correctly stored in relational tables?

The central lesson is:

```text
correct operational structure
≠
convenient analytical structure
```

---

## Course capability

Introduce the minimum analytical-storage concepts required later in the course:

* operational versus analytical data;
* fact table;
* dimension table;
* star schema;
* analytical grain;
* simple data mart.

The activity should not become a complete dimensional-modeling course.

---

## Engineering problem

The retailer already stores sales correctly in operational tables:

```text
customers
orders
products
order_items
```

Analysts repeatedly ask questions such as:

> What were monthly sales by product category?

The operational model can answer the question, but each analysis must reconstruct the analytical context through several joins.

The data team wants a small analytical representation optimized for repeated sales analysis.

---

## Minimal input database

Provide:

```text
data/sales_operational.db
```

Recommended size:

```text
4 customers
5 products
8–10 orders
12–18 order items
3 months
```

The complete business case should remain visually understandable.

Required operational tables:

```text
customers
orders
products
order_items
```

No larger dataset is necessary.

---

## Target analytical model

Create a small star schema.

### `dim_customer`

```text
customer_key
customer_id
customer_name
customer_city
```

### `dim_product`

```text
product_key
product_id
product_name
product_category
```

### `dim_date`

```text
date_key
full_date
year
month
```

### `fact_sales`

Grain:

> One row per order-product line.

Required fields:

```text
order_id
date_key
customer_key
product_key
quantity
unit_price
sales_amount
```

where:

```text
sales_amount = quantity * unit_price
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

Core dimensional-modeling logic must remain visible.

`src/` is not required.

---

## Notebook progression

### Cell 1 — Inspect the operational model

Display the four operational tables.

Ask:

> Where are date, customer, product, quantity, and price stored?

Students should see that the information required for one analytical record is distributed across several operational tables.

---

### Cell 2 — Define the analytical grain

Before creating any table, state explicitly:

```text
one fact row
=
one product line inside one order
```

Use one operational order with several products to show why:

```text
one row per order
```

would lose product-level detail.

Central discussion:

> Why must grain be decided before designing the fact table?

---

### Cell 3 — Create the dimensions

Build:

```text
dim_customer
dim_product
dim_date
```

with simple deterministic surrogate keys.

The code should visibly map business identifiers to analytical keys.

No slowly changing dimension logic is required.

---

### Cell 4 — Create the fact table

Join the operational information required to create:

```text
fact_sales
```

and calculate:

```text
sales_amount
```

Students should see exactly how:

```text
operational transaction
→ analytical fact
```

is constructed.

---

### Cell 5 — Persist the star schema

Create:

```text
submission/sales_mart.db
```

containing:

```text
dim_customer
dim_product
dim_date
fact_sales
```

No additional analytical tables are required.

---

### Cell 6 — Query the analytical model

Answer:

> What were monthly sales by product category?

Use:

```text
fact_sales
+
dim_date
+
dim_product
```

The SQL should be short and directly readable.

This is the central analytical use of the star schema.

---

### Cell 7 — Reconcile with the operational source

Calculate total sales from:

```text
operational tables
```

and from:

```text
fact_sales
```

Verify that both totals are equal.

Central observation:

```text
reorganized data
≠
changed business facts
```

---

## Optional eighth cell

Only if classroom execution remains comfortably within the time budget:

compare the analytical question expressed over:

```text
operational model
```

versus:

```text
star schema
```

The purpose is not performance benchmarking.

The comparison should make visible that the star schema expresses the analytical context more directly.

This cell is optional and should be removed if it adds unnecessary complexity.

---

## Required modeling philosophy

The model must remain deliberately small.

All important modeling decisions should be visible:

```text
grain
dimensions
fact
keys
measure
```

Classroom explanation should focus on:

* why operational and analytical workloads differ;
* why the fact-table grain matters;
* why dimensions provide analytical context;
* why measures belong in the fact table;
* why analytical data can be reorganized without changing business facts.

---

## Surrogate keys

Use simple deterministic integer keys such as:

```text
customer_key
product_key
date_key
```

The workshop should explain only:

> Analytical models often use internal keys distinct from source-system identifiers.

Do not introduce:

* surrogate-key generation services;
* slowly changing dimensions;
* key management strategies;
* historical dimension versions.

---

## Date dimension

Keep `dim_date` minimal.

Required fields:

```text
date_key
full_date
year
month
```

Do not add:

* fiscal calendars;
* quarters;
* holidays;
* week numbering;
* complex date attributes.

The objective is simply to show that time can be represented as analytical context.

---

## Fact measures

Use only:

```text
quantity
unit_price
sales_amount
```

No additional metrics are required.

This keeps the relationship between source transaction and analytical fact transparent.

---

## Expected artifact

### `submission/sales_mart.db`

Must contain exactly the required analytical objects:

```text
dim_customer
dim_product
dim_date
fact_sales
```

The database should be generated programmatically.

---

## Visible validation

Only two central validations are necessary.

### Validation 1 — Fact grain

Verify that:

```text
number of fact rows
=
number of operational order-item rows
```

### Validation 2 — Sales reconciliation

Verify that:

```text
operational total sales
=
fact_sales total sales
```

No long validation section is required.

---

## Required tests

Repository tests should verify:

1. `data/sales_operational.db` exists.
2. `submission/sales_mart.db` exists.
3. All three required dimensions exist.
4. `fact_sales` exists.
5. Dimension surrogate keys are unique.
6. Every fact references valid dimension keys.
7. Fact row count equals operational order-item count.
8. `sales_amount` equals `quantity * unit_price`.
9. Total fact sales reconcile with the operational source.
10. Month-category aggregation produces the expected result.
11. Output is deterministic.

Tests should validate analytical-model semantics rather than implementation style.

---

## What students should observe

The complete workshop should reduce to:

```text
operational tables
↓
analytical question
↓
define grain
↓
dimensions
↓
fact
↓
star schema
↓
analytical query
↓
reconciliation
```

The essential engineering insight is:

> Analytical storage reorganizes reliable source data around how the data will be analyzed.

---

## Boundaries

Do not introduce:

* snowflake schemas;
* slowly changing dimensions;
* conformed dimensions;
* factless fact tables;
* accumulating snapshots;
* periodic snapshots;
* Data Vault;
* cubes;
* OLAP engines;
* cloud data warehouses;
* dbt;
* warehouse performance tuning.

These concepts are not necessary for the central lesson.

---

## Relationship with PRE_03

`PRE_03` asks:

> How do we create a clean current representation of an entity?

`PRE_04` asks:

> How do we reorganize reliable operational data for repeated analytical use?

The distinction should remain clear.

---

## Relationship with PRE_05

`PRE_04` focuses on:

```text
logical analytical organization
```

`PRE_21_data_formats` will focus on:

```text
physical representation of analytical data
```

This establishes a useful transition:

```text
How should analytical data be structured?
↓
How should analytical data be stored physically?
```

---

## Acceptance criteria

The PRE is pedagogically acceptable only when:

1. The operational dataset is small enough to understand visually.
2. One recurring analytical question motivates the complete activity.
3. The notebook uses no more than 8 cells.
4. No code cell exceeds 12 effective lines.
5. Grain is explicitly defined before the fact table is constructed.
6. Exactly one fact table is sufficient.
7. Exactly three small dimensions are sufficient.
8. Surrogate keys are introduced without additional dimension-management complexity.
9. The star schema answers the target analytical question directly.
10. Fact totals reconcile with operational totals.
11. No performance claim is required.
12. No advanced dimensional-modeling topic is introduced.
13. The instructor can focus on **why analytical organization differs from operational organization**.
14. The activity complies with `AGENTS.md`.

---

## Agent implementation instructions

Do not implement while:

```text
Status: DRAFT
```

When implementation is later authorized:

* use the smallest operational database that makes fact and dimension roles obvious;
* keep all dimensional-modeling logic visible;
* do not introduce additional dimensions or facts;
* do not introduce slowly changing dimensions;
* do not use a large dataset to simulate warehouse scale;
* do not hide transformations in helper modules;
* preserve the 8-cell and 12-line hard limits.
