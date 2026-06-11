import pandas as pd
from sqlalchemy import create_engine
# SQLite database path
db_path = "C:/Users/vnaga/MutualFund_ETL/database/mutual_fund.db"

# Create connection
engine = create_engine(f"sqlite:///{db_path}")


print("#Top 5 Funds by fund key")
query = """
SELECT fund_house,aum_crore
FROM dim_fund
ORDER BY aum_crore DESC
LIMIT 5;
"""
df = pd.read_sql(query, engine)
print(df)

print("######Average NAV Per Month#######")
query="""SELECT
strftime('%Y-%m', date) AS month,
ROUND(AVG(nav), 2) AS avg_nav
FROM fact_nav_history
GROUP BY month
ORDER BY month;"""

df = pd.read_sql(query, engine)

print(df)

print("#######SIP Year-over-Year Growth######")
query="""SELECT
    strftime('%Y', transaction_date) AS year,
    SUM(amount_inr) AS sip_amount
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY year
ORDER BY year;"""

df = pd.read_sql(query, engine)

print(df)

print("#####Transactions by State####")
query="""SELECT
    state,
    COUNT(*) AS total_transactions,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;"""

df = pd.read_sql(query, engine)

print(df)

print("*****Funds with Expense Ratio Less Than 1%****8")
query="""SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_scheme_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;"""

df = pd.read_sql(query, engine)

print(df)

print("*****Top 10 Investors by Investment Amount****8")
query="""SELECT
    investor_id,
    SUM(amount_inr) AS total_invested
FROM fact_transactions
GROUP BY investor_id
ORDER BY total_invested DESC
LIMIT 10;"""

df = pd.read_sql(query, engine)

print(df)


print("*****Monthly Transaction Volume****")
query="""SELECT
    strftime('%Y-%m', transaction_date) AS month,
    COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY month
ORDER BY month;"""

df = pd.read_sql(query, engine)

print(df)

print("*****Fund Category-wise Average Return*****")
query="""SELECT
    category,
    ROUND(AVG(return_1yr_pct), 2) AS avg_return
FROM fact_scheme_performance
GROUP BY category
ORDER BY avg_return DESC;"""

df = pd.read_sql(query, engine)

print(df)

print("*****Highest NAV Recorded for Each Fund*****")
query="""SELECT
    amfi_code,
    MAX(nav) AS highest_nav
FROM fact_nav_history
GROUP BY amfi_code
ORDER BY highest_nav DESC;"""

df = pd.read_sql(query, engine)

print(df)

print("*****Transaction Type Distribution*****")
query="""SELECT
    transaction_type,
    COUNT(*) AS count_transactions,
    ROUND(100.0 * COUNT(*) /
        (SELECT COUNT(*) FROM fact_transactions), 2)
        AS percentage
FROM fact_transactions
GROUP BY transaction_type;"""

df = pd.read_sql(query, engine)

print(df)