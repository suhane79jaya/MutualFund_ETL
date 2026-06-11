import pandas as pd
from sqlalchemy import create_engine
import os

# SQLite database path
db_path = "C:/Users/vnaga/MutualFund_ETL/database/mutual_fund.db"

# Create connection
engine = create_engine(f"sqlite:///{db_path}")

# Files and table names
files = {
    "aum_by_fund_house_clean.csv": "dim_fund",
    "investor_transactions_clean.csv": "fact_transactions",
    "nav_history_clean.csv": "fact_nav_history",
    "clean_scheme_performance.csv": "fact_scheme_performance",
    "benchmark_indices_clean.csv": "benchmark_indices",
    "category_inflows_clean.csv":"category_inflows",
    "fund_master_clean.csv":"fund_master",
    "industry_folio_counts_clean.csv":"industry_folio",
    "monthly_sip_inflows_clean.csv":"monthly_sip_inflows",
    "portfolio_holdings_clean.csv":"portfolio_holdings"
}

for file_name, table_name in files.items():
    file_path = os.path.join(r"C:\Users\vnaga\MutualFund_ETL\data", "processed", file_name)
    # print(file_name)
    # print(table_name)
    print(file_path)
    # Read CSV
    df = pd.read_csv(file_path)

    # Load into SQLite
    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"Loaded {len(df)} rows into {table_name}")

print("All datasets loaded successfully.")