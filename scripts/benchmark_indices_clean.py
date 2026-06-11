import pandas as pd

# Load file
df = pd.read_csv("C:/Users/vnaga/MutualFund_ETL/data/raw/10_benchmark_indices.csv")

print("Original Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Trim spaces
for col in df.select_dtypes(include="object"):
    df[col] = df[col].str.strip()

# Standardize index names
if "index_name" in df.columns:
    df["index_name"] = df["index_name"].str.title()

# Convert date
df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)

# Convert index values
df["close_value"] = pd.to_numeric(
    df["close_value"],
    errors="coerce"
)

# Remove invalid rows
df = df.dropna(
    subset=["index_name", "date", "close_value"]
)

# Keep only positive values
df = df[df["close_value"] > 0]

# Sort
df = df.sort_values(
    ["index_name", "date"]
)

# Daily returns
df["daily_return_pct"] = (
    df.groupby("index_name")["close_value"]
      .pct_change() * 100
)

# Save cleaned file
output_file = (
    "C:/Users/vnaga/MutualFund_ETL/data/processed/benchmark_indices_clean.csv"
)

df.to_csv(output_file, index=False)

print("Final Shape:", df.shape)
print(f"Saved to {output_file}")