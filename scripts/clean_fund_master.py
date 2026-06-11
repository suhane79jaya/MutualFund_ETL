import pandas as pd

df = pd.read_csv("C:/Users/vnaga/MutualFund_ETL/data/raw/01_fund_master.csv")

# Remove duplicates
df = df.drop_duplicates()

# Trim spaces
for col in df.select_dtypes(include="object"):
    df[col] = df[col].str.strip()

# Standardize text
for col in ["fund_house", "category", "subcategory"]:
    if col in df.columns:
        df[col] = df[col].str.title()

# Date conversion
if "launch_date" in df.columns:
    df["launch_date"] = pd.to_datetime(
        df["launch_date"],
        errors="coerce"
    )

# Numeric AMFI code
if "amfi_code" in df.columns:
    df["amfi_code"] = pd.to_numeric(
        df["amfi_code"],
        errors="coerce"
    )

# Remove records missing key fields
required = [
    "scheme_name",
    "amfi_code"
]

existing_required = [
    col for col in required
    if col in df.columns
]

df = df.dropna(
    subset=existing_required
)

# # Remove duplicate scheme IDs
# if "scheme_id" in df.columns:
#     df = df.drop_duplicates(
#         subset=["scheme_id"]
#     )

# Save cleaned file
df.to_csv(
    "C:/Users/vnaga/MutualFund_ETL/data/processed/fund_master_clean.csv",
    index=False
)

print("Cleaning complete")
print("Final Shape:", df.shape)