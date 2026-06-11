import pandas as pd

# Load file
df = pd.read_csv("C:/Users/vnaga/MutualFund_ETL/data/raw/06_industry_folio_count.csv")

print("Original Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Trim spaces
for col in df.select_dtypes(include="object"):
    df[col] = df[col].str.strip()

# # Standardize category
# if "category" in df.columns:
#     df["category"] = df["category"].str.title()

# Parse dates
if "month" in df.columns:
    df["month"] = pd.to_datetime(
        df["month"],
        errors="coerce"
    )

# Convert folio counts
df["total_folios_crore"] = pd.to_numeric(
    df["total_folios_crore"],
    errors="coerce"
)

# Remove invalid records
df = df.dropna(
    subset=["month", "total_folios_crore"]
)

# Keep only non-negative counts
df = df[df["total_folios_crore"] >= 0]

# Sort
df = df.sort_values(
    ["month"]
)

# Save cleaned file
output_file = (
    "C:/Users/vnaga/MutualFund_ETL/data/processed/industry_folio_counts_clean.csv"
)

df.to_csv(output_file, index=False)

print("Final Shape:", df.shape)
print(f"Saved to {output_file}")