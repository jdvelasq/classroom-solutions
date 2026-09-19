# PRE Specification

## Identification

**Activity:** `PRE_02_sql_integration`

**Week:** 3

**Status:** `READY`

---

## Activity title

**Integrar datos con SQL**

---

## Central engineering insight

Relational data are intentionally distributed across tables.

SQL allows those tables to be combined at the correct grain to answer analytical questions.

The workshop should answer:

> How can information distributed across customers, orders, products, and order items be transformed into an analytical result without duplicating or miscounting data?

The central lesson is:

```text
syntactically valid SQL
≠
analytically correct SQL
```

---

## Course capability

Introduce the minimum SQL required throughout the rest of the course:

* `SELECT`;
* `WHERE`;
* `ORDER BY`;
* aggregation;
* `GROUP BY`;
* `HAVING`;
* `JOIN`;
* subquery;
* CTE.

These features must appear as part of one analytical problem.

Do not teach them as independent syntax exercises.

---

## Engineering problem

The retailer stores sales using the relational structure introduced conceptually in `PRE_01`.

The analytical question is:

> How much has each customer purchased?

Answering it requires information from:

```text
customers
orders
order_items
products
```

The final result should contain one row per customer.

---

## Minimal input database

Provide:

```text
data/sales.db
```

The activity must be independently executable.

Recommended size:

```text
4 customers
5 products
6–8 orders
10–15 order items
```

The complete contents of every table should be easy to inspect during class.

Required tables:

```text
customers
orders
products
order_items
```

Use the same logical schema as `PRE_01`.

---

## Target analytical result

Generate:

```text
submission/customer_sales.csv
```

Required grain:

> One row per customer.

Required fields:

```text
customer_id
customer_name
customer_city
number_of_orders
total_units
total_sales
```

The output should make the meaning of every aggregation obvious.

---

## Notebook execution budget

Available teaching allocation:

**approximately 75–80 minutes**

Hard constraints:

```text
maximum notebook cells: 8
recommended cells: 8

maximum effective code lines per code cell: 12
```

Core SQL must be visible directly in the notebook.

`src/` is not required.

---

## Notebook progression

### Cell 1 — Inspect the relational data

Connect to SQLite and inspect the four tables.

The entire dataset should be small enough that students can understand the relationships immediately.

Central discussion:

> Which table contains each piece of information?

---

### Cell 2 — Select and filter

Use a compact query containing:

```sql
SELECT
WHERE
ORDER BY
```

Example analytical question:

> Which products cost more than a selected value?

The purpose is simply to establish the SQL query pattern.

Do not create several syntax examples.

---

### Cell 3 — Aggregate one table

Use `order_items` to calculate:

```text
units per order
```

with:

```sql
GROUP BY
```

Then use a simple `HAVING` condition to retain orders above a threshold.

Central idea:

> Aggregation changes the grain of the result.

---

### Cell 4 — Join orders and customers

Answer:

> Which customer placed each order?

Use:

```sql
JOIN
```

between:

```text
orders
customers
```

Students should see explicitly that the join adds customer information without changing the intended order grain.

---

### Cell 5 — Join order items and products

Construct line-level sales information.

Required derived field:

```text
line_total = quantity * unit_price
```

Use:

```text
order_items
+
products
```

Central idea:

> Integration combines attributes stored in different tables.

---

### Cell 6 — Build customer sales

Join the required tables and aggregate to:

```text
one row per customer
```

Calculate:

```text
number_of_orders
total_units
total_sales
```

This is the central SQL query of the workshop.

The code must remain readable enough to inspect directly.

---

### Cell 7 — Demonstrate the grain error

Show one SQL query that is syntactically valid but analytically wrong.

Recommended case:

```text
COUNT(order_id)
```

after joining:

```text
orders
→ order_items
```

An order containing several products is counted several times.

Then compare with:

```sql
COUNT(DISTINCT order_id)
```

Central discussion:

> Why did the first query run correctly but produce the wrong analytical answer?

This is the most important diagnostic moment of the PRE.

---

### Cell 8 — Structure and persist the final query

Rewrite the final customer-sales calculation using:

* one CTE; and
* one compact subquery.

A suitable subquery may identify customers whose total sales exceed the overall customer average.

Generate:

```text
submission/customer_sales.csv
```

The CTE should improve readability rather than add complexity.

---

## Required SQL philosophy

Every query must be short enough to understand visually.

Prefer:

```sql
SELECT
    ...
FROM ...
JOIN ...
GROUP BY ...
```

over deeply nested SQL.

Use descriptive aliases.

Do not use:

* advanced window functions;
* recursive CTEs;
* complex correlated subqueries;
* vendor-specific SQL;
* unnecessary nested queries.

The code should show **what SQL does**.

Classroom explanation should focus on:

* why the tables need to be joined;
* what grain exists before and after each operation;
* why aggregation changes grain;
* why duplicated rows can corrupt metrics;
* why a CTE can clarify a complex query.

---

## Visible validation

Only two validations are necessary in the notebook.

### Validation 1 — Grain

Verify:

```text
one row per customer
```

in the final result.

### Validation 2 — Reconciliation

Verify that:

```text
sum(customer_sales.total_sales)
```

equals total sales calculated directly from the order lines.

This makes the correctness of the integration observable.

---

## Expected artifact

### `submission/customer_sales.csv`

Required columns:

```text
customer_id
customer_name
customer_city
number_of_orders
total_units
total_sales
```

Required properties:

* one row per customer;
* customer identifiers unique;
* order counts correct;
* units correct;
* sales totals correct;
* deterministic ordering.

No additional submission artifact is required.

---

## Required tests

Repository tests should verify:

1. `data/sales.db` exists.
2. All four required tables exist.
3. `submission/customer_sales.csv` exists.
4. Required output columns exist.
5. `customer_id` is unique.
6. Output grain is one row per customer.
7. `number_of_orders` uses the correct distinct-order logic.
8. Total units reconcile with `order_items`.
9. Total sales reconcile with source order lines.
10. Output ordering is deterministic.

Tests should validate analytical correctness rather than SQL formatting.

---

## What students should observe

The complete workshop should reduce to the following conceptual progression:

```text
tables
↓
select
↓
aggregate
↓
join
↓
aggregate across joined data
↓
grain error
↓
correct analytical result
```

The essential lesson is not remembering SQL syntax.

It is understanding:

> What does each operation do to the grain of the data?

---

## Boundaries

Do not introduce:

* window functions;
* data cleaning;
* deduplication workflows;
* query optimization;
* indexes;
* query plans;
* transactions;
* stored procedures;
* database administration;
* ORM tools.

Those concepts belong elsewhere or outside the course.

---

## Relationship with PRE_01

`PRE_01` establishes:

```text
why relational tables exist
```

`PRE_02` establishes:

```text
how relational tables are recombined analytically
```

The activities are conceptually consecutive but technically independent.

---

## Relationship with PRE_03

`PRE_02` focuses on:

```text
querying
joining
aggregating
```

`PRE_03` will introduce:

```text
transforming
standardizing
deduplicating
```

Do not pull transformation complexity into this activity.

---

## Acceptance criteria

The PRE is pedagogically acceptable only when:

1. The complete database is small enough to inspect visually.
2. One analytical problem drives the entire notebook.
3. The notebook uses no more than 8 cells.
4. No code cell exceeds 12 effective lines.
5. All essential SQL is visible.
6. No essential SQL logic is hidden in Python helpers.
7. `SELECT`, filtering, aggregation, joins, `HAVING`, a subquery, and a CTE appear naturally.
8. One incorrect-grain query is demonstrated.
9. Students can explain why it is wrong without reference to SQL syntax.
10. The final result has one explicit grain.
11. Final totals reconcile with source data.
12. The instructor's explanation can focus on **why grain matters**, rather than explaining obscure SQL.
13. The activity complies with `AGENTS.md`.

---

## Agent implementation instructions

Do not implement while:

```text
Status: DRAFT
```

When implementation is later authorized:

* use the smallest database that demonstrates all required relationships;
* keep all core SQL visible in the notebook;
* keep SQL readable rather than compact;
* do not create additional examples merely to demonstrate syntax;
* do not introduce window functions or transformation topics from `PRE_03`;
* do not circumvent notebook limits by hiding SQL in external files or helper functions.
