# de_project_1
Data Engineering Sample Project For Learning And Fun


## 1. Making Project Structure

```python
/workspaces/de_project_1/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── curated/
│
├── src/
│   ├── extract/
│   ├── transform/
│   └── load/
│
├── tests/
│
├── config/
│
└── main.py
```


```
Raw data
   ↓
[Extract]
   ↓
[Transform]
   ↓
[Load]
   ↓
[Analytics / BI]
```
## 2. First ETL Module

### 2.1. File Handling (Bash and Python)
- Direct CSV download -> wget
- real sales transactions dataset (500k+ rows)
- Convert the Excel dataset to CSV

- ✔ raw data preserved
- ✔ format standardized (CSV)
- ✔ reproducible conversion step
- ✔ committed code-ready artifact

Now we move from files → pipelines.

### 2.2 STEP A — Create Extraction Module

- Read CSV in chunks (simulate Spark behavior).

Build a “Spark-like” CSV extractor (chunked reading)

This teaches you:

why Spark exists

how memory-safe ingestion works

how big data pipelines actually read files

| Concept       | Pandas      | Spark              |
| ------------- | ----------- | ------------------ |
| Partition     | chunk       | partition          |
| Lazy eval     | generator   | DAG                |
| Resilience    | retry chunk | retry task         |
| Memory safety | chunksize   | distributed memory |


### 2.3. STEP B — Create Clean Transformations

Next, we move into Silver layer transformations:

- schema cleanup

- fix missing values

- fix datatypes

- normalize customer IDs

- filter invalid rows

Raw (Bronze)
  └── online_retail.csv   ✅

Extract (chunked)
  └── read_sales_csv_in_chunks()   ✅

Transform (Silver)   ← WE ARE HERE
  └── clean + standardize per chunk

Load (Silver output)
  └── cleaned CSV (append mode)

Gold
  └── aggregations / analytics (later)

#### What “Transform chunk-by-chunk” really means

Instead of:

read everything → clean → save

We do:

read chunk → clean chunk → write chunk → repeat

This gives us:

- constant memory usage
- fault isolation
- resumability
- Spark-like behavior

Silver-layer rules

For each chunk, we will:

Drop rows with missing CustomerID

Drop rows with Quantity ≤ 0

Drop rows with UnitPrice ≤ 0

Standardize column names (snake_case)

Convert:

InvoiceDate → datetime

CustomerID → int

Add a derived column:

total_price = quantity * unit_price

### 2.4. STEP C — Load into your project’s silver zone

### 2.5. STEP D — Build aggregation jobs

- sales per country

- top 10 products

- monthly revenue

- RFM scoring

### 2.6. STEP E — Eventually implement Spark-like mimic

