import pandas as pd

# Load file
df = pd.read_csv("C:/Users/vnaga/MutualFund_ETL/data/raw/03_aum_by_fund_house.csv")

print("Original Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Trim spaces
for col in df.select_dtypes(include="object"):
    df[col] = df[col].str.strip()

# Standardize fund house names
df["fund_house"] = df["fund_house"].str.title()

# Convert date
df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)

# Convert AUM to numeric
df["aum_crore"] = pd.to_numeric(
    df["aum_crore"],
    errors="coerce"
)

# Remove invalid rows
df = df.dropna(
    subset=["fund_house", "date", "aum_crore"]
)

# Keep only positive AUM
df = df[df["aum_crore"] > 0]

# Sort
df = df.sort_values(
    ["fund_house", "date"]
)

# Save cleaned file
output_file = "C:/Users/vnaga/MutualFund_ETL/data/processed/aum_by_fund_house_clean.csv"

df.to_csv(output_file, index=False)

print("Cleaned Shape:", df.shape)
print(f"Saved to {output_file}")