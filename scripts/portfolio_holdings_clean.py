import pandas as pd

df = pd.read_csv("C:/Users/vnaga/MutualFund_ETL/data/raw/09_portfolio_holdings.csv")

print("Original Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Trim spaces
for col in df.select_dtypes(include="object"):
    df[col] = df[col].str.strip()

# Parse dates
if "portfolio_date" in df.columns:
    df["portfolio_date"] = pd.to_datetime(
        df["portfolio_date"],
        errors="coerce"
    )


# Convert market value
if "market_value_cr" in df.columns:
    df["market_value_cr"] = pd.to_numeric(
        df["market_value_cr"],
        errors="coerce"
    )



# Validate market value
df = df[df["market_value_cr"] >= 0]

# Save cleaned file
output_file = (
    "C:/Users/vnaga/MutualFund_ETL/data/processed/portfolio_holdings_clean.csv"
)

df.to_csv(output_file, index=False)

print("Final Shape:", df.shape)
print(f"Saved to {output_file}")