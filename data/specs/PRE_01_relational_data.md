# PRE Specification

## Identification

**Activity:** `PRE_01_relational_data`

**Week:** 3

**Status:** `READY`

---

## Activity title

**De un archivo plano a datos relacionales**

---

## Central engineering insight

A flat file may mix several entities and repeatedly store the same information.

Relational design separates those entities and makes their relationships explicit through keys.

The workshop should answer:

> Why should customer, order, product, and order-line information not remain duplicated in one flat table?

---

## Course capability

Minimal relational foundations required by the rest of the course:

* entity;
* table;
* primary key;
* foreign key;
* relationship;
* referential integrity;
* reconstruction through joins.

This is **relational leveling**, not a database-design course.

---

## Engineering problem

The retailer stores sales in:

```text
data/sales.csv
```

Each row represents one product purchased within an order.

The file repeats:

* customer information;
* order information;
* product information.

Students must transform it into a small relational database without losing the original information.

---

## Minimal input dataset

Use the smallest dataset that makes the phenomenon obvious.

Recommended:

```text
8–12 sales lines
3 customers
4 products
4–6 orders
```

At least:

* one customer must have several orders;
* one order must contain several products;
* one product must appear in several orders.

Suggested columns:

```text
order_id
order_date
customer_id
customer_name
customer_city
product_id
product_name
category
unit_price
quantity
```

The complete dataset must fit comfortably on screen.

---

## Target relational model

Create four tables.

### `customers`

```text
customer_id  PK
customer_name
customer_city
```

### `orders`

```text
order_id     PK
order_date
customer_id  FK → customers.customer_id
```

### `products`

```text
product_id   PK
product_name
category
unit_price
```

### `order_items`

```text
order_id     FK → orders.order_id
product_id   FK → products.product_id
quantity

PK = (order_id, product_id)
```

No additional tables are required.

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

The implementation must not hide core relational logic in helper modules.

`src/` is not required for this PRE.

---

## Notebook progression

The completed notebook should require approximately **7 substantive cells**.

### Cell 1 — Load the flat file

Load and display the complete dataset.

Students should immediately see the repeated customer, order, and product information.

Central discussion:

> What different things are represented inside the same row?

---

### Cell 2 — Identify the entities

Use simple selections and `drop_duplicates()` to expose:

```text
customers
orders
products
order_items
```

The code should make the mapping from flat columns to entities explicit.

No formal normalization theory is required.

---

### Cell 3 — Build the four relational tables

Construct the four DataFrames explicitly.

For example:

```python
customers = sales[
    ["customer_id", "customer_name", "customer_city"]
].drop_duplicates()

orders = sales[
    ["order_id", "order_date", "customer_id"]
].drop_duplicates()
```

and equivalent code for `products` and `order_items`.

The transformation must remain visible in the notebook.

---

### Cell 4 — Create the SQLite schema

Create:

```text
customers
orders
products
order_items
```

with explicit:

```text
PRIMARY KEY
FOREIGN KEY
```

constraints.

The SQL should be small enough to read directly.

No schema-generation abstraction is required.

---

### Cell 5 — Load the relational data

Insert the four DataFrames into SQLite.

Generate:

```text
submission/sales.db
```

Students should see the relationship between:

```text
DataFrame
→ relational table
```

---

### Cell 6 — Demonstrate referential integrity

Attempt one intentionally invalid insert.

Example:

```text
order with customer_id = C999
```

SQLite should reject it because the customer does not exist.

Central discussion:

> Why is rejecting this row preferable to silently storing an inconsistent database?

Only one integrity-failure example is required.

---

### Cell 7 — Reconstruct the original information

Use one SQL query joining:

```text
orders
customers
order_items
products
```

Reconstruct the sales representation and compare it with the original flat dataset.

Central observation:

```text
information separated
≠
information lost
```

---

## Required code philosophy

All relational logic must be visible in the notebook.

Do not hide:

* entity extraction;
* schema creation;
* key definitions;
* inserts;
* integrity validation;
* reconstruction query.

The code should explain **what happens**.

Classroom discussion should explain:

* why repetition is problematic;
* why entities are separated;
* why keys are necessary;
* why referential integrity matters;
* why relational data can be reconstructed.

---

## Expected artifact

### `submission/sales.db`

Must contain:

```text
customers
orders
products
order_items
```

with the declared keys and relationships.

No additional submission artifact is necessary.

---

## Visible validation

The notebook only needs two central validations.

### Validation 1

An invalid foreign-key reference is rejected.

### Validation 2

Joining the four tables reconstructs the original logical sales information.

Do not add a long validation section.

---

## Required tests

Repository tests should verify:

1. `submission/sales.db` exists.
2. All four required tables exist.
3. Primary keys are correctly defined.
4. Foreign keys are correctly defined.
5. Customer IDs are unique.
6. Order IDs are unique.
7. Product IDs are unique.
8. `(order_id, product_id)` is unique in `order_items`.
9. Every order references an existing customer.
10. Every order item references an existing order and product.
11. Reconstructed sales contain the expected number of rows.
12. Reconstructed logical information matches the flat source.

These tests may be more comprehensive than the visible notebook validation.

---

## What students should observe

Students should directly see:

```text
flat file
↓
repeated information
↓
entities
↓
tables
↓
primary and foreign keys
↓
relational database
↓
join
↓
original information reconstructed
```

The notebook should make this progression visually obvious.

---

## Boundaries

Do not introduce:

* first, second, or third normal form formally;
* functional dependencies;
* candidate-key theory;
* database administration;
* indexes;
* transactions in depth;
* performance tuning;
* ORM frameworks;
* database servers.

These topics are not necessary for the central engineering insight.

---

## Relationship with PRE_02

`PRE_01` answers:

> How are data represented relationally?

`PRE_02_sql_integration` then answers:

> How can those related tables be queried and integrated with SQL?

The SQLite database created conceptually here establishes the relational model required by the next activity, although `PRE_02` must remain independently executable.

---

## Acceptance criteria

The PRE is pedagogically acceptable only when:

1. The complete source dataset is small enough to inspect visually.
2. Exactly four relational entities are sufficient.
3. The notebook uses no more than 8 cells.
4. No code cell exceeds 12 effective lines.
5. Core teaching logic is fully visible.
6. Variable and table names are self-explanatory.
7. Primary and foreign keys are explicit.
8. One referential-integrity failure is demonstrated.
9. One join reconstructs the original information.
10. The instructor can spend class time explaining **why relational structure exists**, rather than explaining obscure code.
11. No unrelated relational theory is introduced.
12. The activity complies with `AGENTS.md`.

---

## Agent implementation instructions

Do not implement while:

```text
Status: DRAFT
```

When implementation is later authorized, prioritize pedagogical clarity over feature coverage.

Do not expand the activity beyond this specification.

Do not make the dataset larger unless a larger dataset is required to expose a specific phenomenon.

Do not circumvent notebook limits by hiding teaching logic in `src/`.
