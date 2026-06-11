import pandas as pd

df = pd.read_csv("C:/Users/vnaga/MutualFund_ETL/data/raw/05_category_inflows.csv")

print("Original Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Trim spaces
for col in df.select_dtypes(include="object"):
    df[col] = df[col].str.strip()

# Standardize category
if "category" in df.columns:
    df["category"] = df["category"].str.title()

# Parse month/date
if "month" in df.columns:
    df["month"] = pd.to_datetime(
        df["month"],
        errors="coerce"
    )

# Remove rows missing key fields
required = ["category", "month", "net_inflow_crore"]

existing = [c for c in required if c in df.columns]

df = df.dropna(subset=existing)

# Sort
df = df.sort_values(["category", "month"])

# Save cleaned file
output_file = "C:/Users/vnaga/MutualFund_ETL/data/processed/category_inflows_clean.csv"

df.to_csv(output_file, index=False)

print("Final Shape:", df.shape)
print(f"Saved to {output_file}")