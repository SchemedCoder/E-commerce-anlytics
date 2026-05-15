# E-Commerce Product Analytics Dashboard & Azure Databricks Pipeline

Project Overview


This repository is built to mimic a real business environment where raw eCommerce datasets are transformed into analytics-ready data products for business decision-making.

---

Business Objective
Modern eCommerce businesses need to answer:

Customer Analytics
- Which acquisition channels drive highest-value users?
- What is customer conversion and retention?
- Which customers generate the most revenue?

 Merchant Analytics
- Which merchants/products drive highest GMV?
- Which product categories perform best?
- What is merchant contribution by order volume?

Funnel Analytics
- Sessions → Product Views → Add to Cart → Checkout → Orders
- Funnel drop-off analysis
- Conversion bottleneck identification

---
 Tech Stack

Data Engineering
- Azure Data Lake (Bronze / Silver / Gold)
- Azure Databricks
- PySpark
- SQL
- Azure Data Factory (Optional)

Analytics
- Power BI / Tableau
- KPI Reporting
- Funnel Analysis

Version Control
- GitHub

---
 Project Architecture

Raw CSV / JSON Data Sources
        ↓
Azure Data Lake (Bronze Layer)
        ↓
Databricks ETL (Silver Layer)
        ↓
Business KPI Aggregation (Gold Layer)
        ↓
SQL Analytics Layer
        ↓
Power BI Dashboard / Stakeholder Reporting
