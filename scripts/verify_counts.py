import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

# engine = create_engine("sqlite:///MutualFund_ETL/database/mutual_fund.db")



BASE_DIR = Path(__file__).resolve().parent.parent

db_dir = BASE_DIR / "database"
db_dir.mkdir(exist_ok=True)

db_path = db_dir / "mutual_fund.db"

engine = create_engine(f"sqlite:///{db_path}")

print("Database:", db_path)
tables = {
    "dim_fund": "C:/Users/vnaga/MutualFund_ETL/data/processed/aum_by_fund_house_clean.csv",
    "fact_transactions": "C:/Users/vnaga/MutualFund_ETL/data/processed/investor_transactions_clean.csv",
    "fact_nav_history": "C:/Users/vnaga/MutualFund_ETL/data/processed/nav_history_clean.csv",
    "fact_scheme_performance": "C:/Users/vnaga/MutualFund_ETL/data/processed/clean_scheme_performance.csv"
}
print("Tables",tables)
for table, csv_file in tables.items():

    csv_rows = len(pd.read_csv(csv_file))

    db_rows = pd.read_sql(
        f"SELECT COUNT(*) AS count FROM {table}",
        engine
    ).iloc[0]["count"]

    status = "MATCH" if csv_rows == db_rows else "MISMATCH"

    print(
        f"{table}: CSV={csv_rows}, DB={db_rows} --> {status}"
    )