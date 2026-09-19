# PRE Specification

## Identification

**Activity:** `PRE_19_metadata_lineage`

**Week:** 12

**Status:** `READY`

---

## Activity title

**Saber qué datos existen y de dónde vienen**

---

## Central engineering insight

A data platform becomes difficult to operate when datasets exist but nobody can answer:

* what they contain;
* what one row represents;
* who owns them;
* where they came from;
* what depends on them.

The workshop should answer:

> If an upstream dataset or column changes, how can we determine which downstream data may be affected?

The central progression is:

```text
dataset
↓
metadata
↓
lineage
↓
dependency
↓
impact analysis
```

The essential lesson is:

```text
data without context
≠
operable data
```

---

## Course capability

Introduce only the minimum metadata and lineage concepts required by the course:

* dataset catalog;
* column metadata;
* owner;
* grain;
* classification;
* dataset lineage;
* column lineage;
* transformation description;
* downstream dependency;
* impact analysis.

Governance should appear only through a few concrete metadata fields.

This is not a data-governance framework workshop.

---

## Engineering problem

The retailer has accumulated several datasets through its pipeline.

A product-category field originates in a source system and eventually appears in a dashboard mart.

The source team proposes changing that field.

Before making the change, the data team needs to answer:

> What downstream datasets and columns depend on it?

Without lineage, the answer depends on tribal knowledge.

Students must create enough metadata to answer the question directly.

---

## Minimal platform scenario

Use exactly five datasets.

```text
source_transactions
source_products
raw_transactions
curated_sales
monthly_category_sales
```

Logical lineage:

```text
source_transactions
        ↓
raw_transactions
        ↓
curated_sales
        ↓
monthly_category_sales

source_products
        ↓
curated_sales
```

This graph is sufficient to establish upstream/downstream reasoning.

---

## Minimal input artifacts

Provide tiny deterministic artifacts such as:

```text
data/transactions.csv
data/products.csv
data/raw_transactions.parquet
data/sales_curated.parquet
data/sales_serving.db
```

All datasets should remain small.

The objective is metadata, not data processing.

---

## Controlled privacy example

Include:

```text
customer_email
```

in:

```text
source_transactions
raw_transactions
```

Classify it as:

```text
RESTRICTED
```

It must not appear in:

```text
curated_sales
monthly_category_sales
```

This provides one concrete reason why column metadata and classification matter.

Do not introduce a broader privacy framework.

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

All important metadata and lineage structures must remain visible.

---

## Notebook progression

### Cell 1 — Inspect the platform datasets

Inspect the five supplied datasets.

For each, identify:

```text
name
format
grain
key columns
```

Central question:

> If someone discovered these files without documentation, what would they need to know before using them safely?

Do not perform analytical processing.

---

### Cell 2 — Build the dataset catalog

Create:

```text
submission/data_catalog.csv
```

Required columns:

```text
dataset
layer
grain
format
owner
access_level
location
```

Example layers:

```text
source
raw
curated
serving
```

Example access levels:

```text
RESTRICTED
INTERNAL
```

The catalog should contain exactly the five canonical datasets.

---

### Cell 3 — Build the column catalog

Create:

```text
submission/column_catalog.csv
```

Required columns:

```text
dataset
column_name
data_type
description
classification
```

Use only concise descriptions.

Required classification examples:

```text
customer_email → RESTRICTED
sales_amount   → INTERNAL
product_category → INTERNAL
```

Central discussion:

> Why is knowing a column name and type sometimes insufficient?

---

### Cell 4 — Define dataset lineage

Represent the four required dependency edges:

```text
source_transactions → raw_transactions
raw_transactions → curated_sales
source_products → curated_sales
curated_sales → monthly_category_sales
```

Students should directly observe the upstream/downstream graph.

Central idea:

```text
where data are stored
and
where data came from
```

are different kinds of metadata.

---

### Cell 5 — Define three column-lineage examples

Track exactly three important business derivations.

### Product category

```text
source_products.product_category
→
curated_sales.product_category
→
monthly_category_sales.product_category
```

### Sales amount

```text
raw_transactions.quantity
+
raw_transactions.unit_price
→
curated_sales.sales_amount
→
monthly_category_sales.total_sales
```

### Transaction identifier

```text
source_transactions.transaction_id
→
raw_transactions.transaction_id
→
curated_sales.transaction_id
```

Describe transformations explicitly but briefly.

No automatic SQL parser is required.

---

### Cell 6 — Perform impact analysis

Ask:

> What could be affected if `source_products.product_category` changes?

Traverse the small lineage graph and identify downstream datasets:

```text
curated_sales
monthly_category_sales
```

and corresponding columns.

Central discussion:

> Why should impact analysis happen before an upstream schema or semantic change is deployed?

The traversal logic must remain short and visible.

No graph library is required.

---

### Cell 7 — Persist lineage and validate exposure

Create:

```text
submission/lineage.csv
```

Required columns:

```text
source_dataset
source_column
target_dataset
target_column
transformation
```

Then validate the controlled privacy rule:

```text
customer_email
```

exists in restricted upstream data but does not appear in curated or serving outputs.

Conclude with:

```text
metadata
+
lineage
→
discoverability
+
impact understanding
```

---

## Optional eighth cell

Only if classroom time comfortably permits:

perform the reverse question:

> Where did `monthly_category_sales.total_sales` come from?

Trace upstream:

```text
monthly_category_sales.total_sales
←
curated_sales.sales_amount
←
raw_transactions.quantity + unit_price
```

This reinforces that lineage supports both:

```text
downstream impact
and
upstream provenance
```

No second artifact is required.

---

## Dataset catalog philosophy

The dataset catalog should answer:

```text
What is this dataset?
What does one row represent?
Where is it?
Who is responsible for it?
Who should access it?
```

Do not add dozens of metadata fields.

The catalog is intentionally minimal.

---

## Column catalog philosophy

The column catalog should answer:

```text
What does this field mean?
What type does it have?
How sensitive is it?
```

Do not catalog every possible technical property.

---

## Ownership

Use simple role-level ownership such as:

```text
Sales Operations
Data Engineering
Analytics
```

Do not introduce organizational workflows for stewardship.

The purpose is only to make responsibility explicit.

---

## Classification

Use only:

```text
RESTRICTED
INTERNAL
```

for this workshop.

Do not introduce a complex sensitivity hierarchy.

One controlled sensitive field is enough to establish the idea.

---

## Lineage philosophy

Lineage should make data movement and derivation explicit.

For this workshop:

```text
source
→
raw
→
curated
→
serving
```

is sufficient.

The lineage must describe actual transformations represented by the scenario.

Do not generate decorative graph complexity.

---

## Dataset lineage versus column lineage

### Dataset lineage

Answers:

> Which datasets depend on which datasets?

Example:

```text
curated_sales
→
monthly_category_sales
```

### Column lineage

Answers:

> Which specific field or calculation produced this field?

Example:

```text
curated_sales.sales_amount
→
monthly_category_sales.total_sales
```

Both are useful but solve different levels of the same dependency problem.

---

## Impact analysis

The central impact question is:

```text
source_products.product_category changes
```

Expected affected datasets:

```text
curated_sales
monthly_category_sales
```

Expected affected columns include:

```text
curated_sales.product_category
monthly_category_sales.product_category
```

No risk score is required.

No automated change-management process is required.

---

## Provenance

If discussed, provenance means:

> Understanding the upstream origin of a dataset or field.

For example:

```text
monthly_category_sales.total_sales
```

can be traced back through:

```text
curated_sales.sales_amount
```

to source transaction fields.

Do not introduce separate provenance tooling.

---

## Expected artifacts

### `submission/data_catalog.csv`

Required columns:

```text
dataset
layer
grain
format
owner
access_level
location
```

Required rows:

```text
source_transactions
source_products
raw_transactions
curated_sales
monthly_category_sales
```

---

### `submission/column_catalog.csv`

Required columns:

```text
dataset
column_name
data_type
description
classification
```

The catalog must include at least the columns involved in:

* the controlled privacy example;
* the three lineage examples.

---

### `submission/lineage.csv`

Required columns:

```text
source_dataset
source_column
target_dataset
target_column
transformation
```

It must contain enough information to reconstruct the canonical dataset and column dependencies.

---

## Visible validation

Only two validations are required.

### Validation 1 — Impact

Verify that changing:

```text
source_products.product_category
```

identifies:

```text
curated_sales
monthly_category_sales
```

as downstream dependencies.

### Validation 2 — Sensitive-column exposure

Verify:

```text
customer_email
```

does not appear in:

```text
curated_sales
monthly_category_sales
```

---

## Required tests

Repository tests should verify:

1. All five canonical datasets are represented in the dataset catalog.
2. Required dataset metadata columns exist.
3. Dataset locations are relative.
4. Required column metadata fields exist.
5. `customer_email` is classified as `RESTRICTED`.
6. Required dataset lineage edges exist.
7. Required column-lineage examples exist.
8. `source_products.product_category` reaches `curated_sales`.
9. It also reaches `monthly_category_sales`.
10. `customer_email` does not appear in curated or serving schemas.
11. All three submission artifacts exist.
12. Catalog and lineage ordering is deterministic.
13. Re-execution produces equivalent logical outputs.

Tests should validate metadata semantics rather than notebook formatting.

---

## What students should observe

The complete workshop should reduce to:

```text
five datasets
↓
catalog them
↓
describe important columns
↓
connect dependencies
↓
trace important fields
↓
change one upstream field
↓
identify downstream impact
```

The essential engineering insight is:

> Metadata tells us what data mean; lineage tells us how data depend on one another.

---

## Boundaries

Do not introduce:

* enterprise data catalogs;
* DataHub;
* OpenMetadata;
* Apache Atlas;
* automated SQL lineage parsing;
* governance committees;
* stewardship workflows;
* policy engines;
* IAM implementation;
* role-based access-control systems;
* regulatory compliance frameworks;
* knowledge graphs.

These are unnecessary for the central lesson.

---

## Relationship with PRE_18

`PRE_18` establishes:

```text
stable consumer-facing datasets
```

`PRE_19` asks:

```text
What are those datasets?
Where did they come from?
What depends on them?
```

---

## Relationship with PRE_20

`PRE_19` completes the technical capabilities required to reason about the final architecture.

`PRE_20_end_to_end_architecture` will integrate:

```text
sources
ingestion
storage
processing
quality
contracts
incremental execution
operations
distributed processing
streaming
serving
metadata
lineage
```

into one complete architectural design.

No new technical capability should be introduced in `PRE_20`.

---

## Acceptance criteria

The PRE is pedagogically acceptable only when:

1. Exactly five datasets are sufficient.
2. The lineage graph remains small enough to understand visually.
3. The notebook uses no more than 8 cells.
4. Recommended implementation uses approximately 7 cells.
5. No code cell exceeds 12 effective lines.
6. Dataset metadata are explicit.
7. Column metadata are explicit.
8. Ownership and access classification remain minimal.
9. Exactly three column-lineage examples are sufficient.
10. One downstream impact analysis is performed.
11. One sensitive-field exposure check is performed.
12. No metadata platform is required.
13. No automatic lineage framework is required.
14. The instructor can focus on **why discoverability, provenance, and impact analysis matter**, rather than on catalog-tool syntax.
15. The activity complies with `AGENTS.md`.

---

## Agent implementation instructions

Do not implement while:

```text
Status: DRAFT
```

When implementation is later authorized:

* use exactly five tiny canonical datasets;
* keep metadata fields minimal;
* use exactly three column-lineage examples;
* use one controlled `RESTRICTED` field;
* keep lineage traversal explicit and short;
* do not introduce `networkx` unless implementation evidence shows it materially simplifies the notebook;
* do not introduce a metadata platform;
* do not introduce automatic SQL parsing;
* do not hide lineage logic before it has been demonstrated;
* preserve the 8-cell and 12-line hard limits.
