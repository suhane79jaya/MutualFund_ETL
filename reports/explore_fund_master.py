import pandas as pd

# Load data
df = pd.read_csv("C:/Users/vnaga/MutualFund_ETL/data/raw/01_fund_master.csv")
print("\n===== SUMMARY =====")

print("Total Schemes:", len(df))
print("Fund Houses:", df["fund_house"].nunique())
print("Categories:", df["category"].nunique())
print("Sub-Categories:", df["sub_category"].nunique())
print("\n=====================")
print("\nTop 10 Fund Houses:")
print(df["fund_house"].value_counts().head(10))
print("\n=====================")
print("\nTop Categories:")
print(df["category"].value_counts())
print("\n=====================")
print("\nTop Sub-Categories:")
print(df["sub_category"].value_counts().head(15))
print("\n=====================")