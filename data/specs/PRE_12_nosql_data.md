# PRE Specification

## Identification

**Activity:** `PRE_23_nosql_data`

**Week:** 5

**Status:** `READY`

---

## Activity title

**Cuando una tabla deja de ser natural**

---

## Central engineering insight

Not all data fit naturally into one fixed tabular structure.

A document model can be useful when records share some common fields but also contain nested or variable attributes.

The workshop should answer:

> When does a document representation make the structure clearer than forcing everything into one relational table?

The central lesson is:

```text
different data shape
→
different modeling tradeoff
```

not:

```text
NoSQL is better than SQL
```

---

## Course capability

Introduce only the minimum concepts required to reason about semistructured data:

* fixed schema;
* semistructured data;
* nested attributes;
* optional attributes;
* arrays;
* document model;
* relational alternative;
* SQL versus document-model tradeoff.

The activity should remain conceptual and practical.

It is not a MongoDB tutorial.

---

## Engineering problem

The retailer has a product catalog.

All products share:

```text
product_id
product_name
category
price
```

but different categories require different attributes.

For example:

### Laptop

```text
ram_gb
storage_gb
processor
```

### Shoe

```text
size
color
material
```

### Book

```text
author
isbn
pages
```

Trying to store every possible attribute in one wide table creates many irrelevant empty fields.

Students must compare that representation with a document-oriented representation.

---

## Minimal input dataset

Provide:

```text
data/products.json
```

Recommended size:

```text
6–9 products
3 categories
```

Suggested:

```text
2–3 laptops
2–3 shoes
2–3 books
```

The entire dataset should be understandable visually.

Each document should contain:

```text
product_id
product_name
category
price
attributes
tags
```

where:

```text
attributes
```

is a nested object whose fields vary by category.

---

## Example document

```json
{
  "product_id": "P001",
  "product_name": "Laptop A",
  "category": "Laptop",
  "price": 1200,
  "attributes": {
    "ram_gb": 16,
    "storage_gb": 512,
    "processor": "M3"
  },
  "tags": ["portable", "professional"]
}
```

A shoe should use a different `attributes` structure.

---

## Notebook execution budget

Available teaching allocation:

**approximately 45–55 minutes**

Hard constraints:

```text
maximum notebook cells: 6
recommended cells: 6

maximum effective code lines per code cell: 12
```

No essential modeling logic may be hidden.

`src/` is not required.

---

## Notebook progression

### Cell 1 — Inspect the documents

Load:

```text
data/products.json
```

Display all or most documents.

Students should directly observe:

* common fields;
* nested `attributes`;
* different attribute names by category;
* array-valued `tags`.

Central discussion:

> Which parts of the product structure are stable, and which vary?

---

### Cell 2 — Force the documents into one flat table

Flatten the documents into a single DataFrame.

Students should see columns such as:

```text
ram_gb
storage_gb
processor
size
color
material
author
isbn
pages
```

with many missing values.

Central observation:

```text
possible
≠
natural
```

The purpose is not to claim the table is invalid.

It is to expose the modeling cost.

---

### Cell 3 — Query the document structure directly

Use simple Python operations to answer one category-specific question.

Example:

> Which laptops have at least 16 GB of RAM?

The query should directly access:

```text
attributes.ram_gb
```

without first creating columns for every possible category attribute.

Central discussion:

> Why is the nested representation convenient for variable attributes?

---

### Cell 4 — Add a new product category

Create one additional product with a previously unseen attribute structure.

Example category:

```text
Camera
```

with:

```text
megapixels
sensor_type
optical_zoom
```

Append it to the document collection.

Students should observe that the document representation accepts the new shape naturally.

No schema migration mechanism is required for the example.

---

### Cell 5 — Show the relational alternative

Represent conceptually or with a tiny DataFrame a normalized relational alternative such as:

```text
products
product_attributes
```

where attributes are stored as:

```text
product_id
attribute_name
attribute_value
```

The purpose is to show that relational modeling remains possible.

Central discussion:

> What do we gain and lose with each representation?

Do not build a full relational database.

---

### Cell 6 — Build the comparison artifact

Generate:

```text
submission/model_comparison.csv
```

Required columns:

```text
criterion
relational_model
document_model
case_implication
```

Required criteria:

```text
fixed_schema
nested_data
variable_attributes
relationships
duplication
updates
analytical_integration
```

The artifact should summarize the tradeoffs demonstrated in the notebook.

---

## Required modeling philosophy

The activity must remain neutral.

Do not teach:

```text
SQL old
NoSQL modern
```

or:

```text
NoSQL faster
```

Instead, students should reason from data shape and workload.

The comparison should consider:

* schema regularity;
* nested structure;
* attribute variability;
* relationships;
* update patterns;
* downstream analytics.

---

## Document-model advantage in this case

The document representation is attractive because:

```text
different categories
→
different attributes
```

while preserving one natural representation per product.

The key benefit is structural flexibility.

Do not generalize beyond the case.

---

## Relational-model advantage in this case

The relational alternative may be preferable when:

* relationships across entities dominate;
* consistency constraints are important;
* repeated analytical joins are common;
* structure is stable.

Students should see that the relational option remains valid.

---

## Duplication tradeoff

If nested documents duplicate supplier or category information, mention briefly:

```text
fewer joins
↔
possible duplication and harder updates
```

Do not implement a duplicated supplier example unless the notebook remains comfortably within the cell budget.

Discussion alone is sufficient.

---

## Expected artifact

### `submission/model_comparison.csv`

Required columns:

```text
criterion
relational_model
document_model
case_implication
```

Required criteria:

```text
fixed_schema
nested_data
variable_attributes
relationships
duplication
updates
analytical_integration
```

No additional submission artifact is required.

---

## Visible validation

Only one central validation is required.

Verify that the newly added product category can be represented and queried without changing the structure of existing product documents.

The student should directly observe:

```text
new data shape
without rewriting previous documents
```

---

## Required tests

Repository tests should verify:

1. `data/products.json` exists.
2. Required common fields exist.
3. At least three categories are represented.
4. Category-specific attributes differ across categories.
5. Nested attributes can be accessed correctly.
6. Array-valued tags are represented.
7. The controlled new category can be added.
8. Existing documents remain logically unchanged.
9. `submission/model_comparison.csv` exists.
10. Required comparison criteria are represented.
11. Output ordering is deterministic.

Tests should validate the modeling example rather than any external NoSQL technology.

---

## What students should observe

The complete workshop should reduce to:

```text
heterogeneous product documents
↓
force into flat table
↓
many irrelevant fields
↓
query nested structure
↓
add unseen category
↓
compare relational and document models
```

The essential engineering insight is:

> Data models should fit the shape and access patterns of the data.

---

## Boundaries

Do not introduce:

* MongoDB installation;
* MongoDB query language;
* Cassandra;
* DynamoDB;
* CAP theorem;
* eventual consistency;
* sharding;
* replication;
* distributed NoSQL architecture;
* index design;
* NoSQL performance comparisons.

Those topics are unnecessary for this PRE.

---

## Relationship with PRE_06

`PRE_06` asks:

> How should large tabular analytical data be physically organized?

`PRE_07` asks:

> What happens when the source data are not naturally regular and tabular?

The distinction is:

```text
storage organization
≠
data model
```

---

## Relationship with PRE_08

`PRE_07` introduces semistructured sources.

`PRE_24_batch_ingestion` will then begin the ingestion block by asking:

> How do source data enter a controlled data pipeline?

---

## Acceptance criteria

The PRE is pedagogically acceptable only when:

1. One heterogeneous product catalog drives the complete activity.
2. The notebook uses no more than 6 cells.
3. No code cell exceeds 12 effective lines.
4. The full document structure is visible.
5. Flattening exposes sparse or irrelevant columns.
6. One nested query is demonstrated.
7. One unseen category is added.
8. A relational alternative is acknowledged.
9. SQL and NoSQL are compared by tradeoff, not by superiority.
10. No external NoSQL server is required.
11. `submission/model_comparison.csv` summarizes the decision.
12. The instructor can focus on **why data shape influences modeling choice**.
13. The activity complies with `AGENTS.md`.

---

## Agent implementation instructions

Do not implement while:

```text
Status: DRAFT
```

When implementation is later authorized:

* use only a handful of products;
* keep all documents visually understandable;
* use exactly one nested-query example;
* use exactly one new-category example;
* do not introduce a NoSQL server;
* do not turn the PRE into a MongoDB tutorial;
* do not hide the document logic in helper functions;
* preserve the 6-cell and 12-line hard limits.
