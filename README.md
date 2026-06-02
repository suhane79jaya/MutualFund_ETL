MutualFund_ETL is an end-to-end Extract, Transform, and Load (ETL) project designed to collect, process, validate, and analyze mutual fund data from publicly available sources. The project focuses on Indian mutual funds and leverages AMFI scheme codes and NAV (Net Asset Value) data to build a reliable and scalable data pipeline for investment analysis and reporting.

The ETL workflow begins by extracting mutual fund master data and historical NAV data using APIs and structured datasets. Fund information such as scheme code, fund house, category, sub-category, and risk classification is collected and stored in a raw data layer. Historical NAV records for selected schemes are fetched through API endpoints and saved for further processing.

In the transformation stage, the project performs data cleaning, validation, and standardization. Date formats are normalized, numeric fields are converted to appropriate data types, missing values are identified, and duplicate records are removed. AMFI scheme codes are validated to ensure consistency between the fund master dataset and NAV history data. Data quality checks are implemented to measure completeness, uniqueness, and integrity of the collected information.

The processed datasets are then organized into structured folders that support analytical workflows and reporting. The project follows a layered data architecture consisting of raw, processed, and final datasets, enabling reproducibility and easier maintenance of the pipeline.

Key features of the repository include:

Automated NAV data extraction from mutual fund APIs.
Fund master data exploration and profiling.
AMFI scheme code validation and data quality reporting.
Data cleaning and transformation using Python and Pandas.
Structured project organization following ETL best practices.
Export of processed datasets for dashboards, visualization tools, and further analytics.

The project serves as a practical example of data engineering concepts including data ingestion, transformation, validation, and storage. It can be extended to support advanced analytics such as SIP return calculations, fund performance comparisons, risk analysis, portfolio tracking, and business intelligence dashboards using tools such as Power BI, Tableau, or Looker Studio.

This repository is suitable for students, aspiring data analysts, data engineers, and finance enthusiasts looking to gain hands-on experience in building real-world ETL pipelines using Python and mutual fund datasets.
