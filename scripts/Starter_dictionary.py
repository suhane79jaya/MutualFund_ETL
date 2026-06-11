import pandas as pd

# Load files
fund_master = pd.read_csv(r"C:\Users\vnaga\MutualFund_ETL\data\raw\01_fund_master.csv")
nav_history = pd.read_csv(r"C:\Users\vnaga\MutualFund_ETL\data\raw\02_nav_history.csv")
fund_house = pd.read_csv(r"C:\Users\vnaga\MutualFund_ETL\data\raw\03_aum_by_fund_house.csv")
monthly_sip = pd.read_csv(r"C:\Users\vnaga\MutualFund_ETL\data\raw\04_monthly_sip_inflows.csv")
category = pd.read_csv(r"C:\Users\vnaga\MutualFund_ETL\data\raw\05_category_inflows.csv")
industry_folio = pd.read_csv(r"C:\Users\vnaga\MutualFund_ETL\data\raw\06_industry_folio_count.csv")
performance = pd.read_csv(r"C:\Users\vnaga\MutualFund_ETL\data\raw\07_scheme_performance.csv")
transactions = pd.read_csv(r"C:\Users\vnaga\MutualFund_ETL\data\raw\08_investor_transactions.csv")
holdings = pd.read_csv(r"C:\Users\vnaga\MutualFund_ETL\data\raw\09_portfolio_holdings.csv")
benchmark = pd.read_csv(r"C:\Users\vnaga\MutualFund_ETL\data\raw\10_benchmark_indices.csv")
# Store DataFrames in a dictionary
dfs = {
    "fund_master": fund_master,
    "nav_history": nav_history,
    "aum_by_fund_house":fund_house,
    "monthly_sip_inflows":monthly_sip,
    "category_inflows":category,
    "industry_folio_count":industry_folio,
    "scheme_performance":performance,
    "portfolio_holdings": holdings,
    "benchmark_indices": benchmark
}

# Create data dictionary
data_dict = []

for table_name, df in dfs.items():
    for col in df.columns:
        data_dict.append({
            "Table": table_name,
            "Column Name": col,
            "Data Type": str(df[col].dtype),
            "Business Definition": "",
            "Source File": f"{table_name}.csv"
        })

# Convert to DataFrame
dictionary_df = pd.DataFrame(data_dict)

with open(r"C:\Users\vnaga\MutualFund_ETL\data_dictionary.md", "w", encoding="utf-8") as f:

    for table_name, df in dfs.items():
        f.write(f"# {table_name}\n\n")

        temp = pd.DataFrame({
            "Column Name": df.columns,
            "Data Type": [str(df[col].dtype) for col in df.columns],
            "Business Definition": ""
        })

        f.write(temp.to_markdown(index=False))
        f.write("\n\n")
