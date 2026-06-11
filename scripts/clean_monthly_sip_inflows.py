
import pandas as pd

# Load file
df = pd.read_csv("C:/Users/vnaga/MutualFund_ETL/data/raw/04_monthly_sip_inflows.csv")

print("Original Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Trim spaces
for col in df.select_dtypes(include="object"):
    df[col] = df[col].str.strip()

# # Standardize fund house names
# if "fund_house" in df.columns:
#     df["fund_house"] = df["fund_house"].str.title()

# Parse month/date column
df["month"] = pd.to_datetime(
    df["month"],
    errors="coerce"
)

# Convert SIP inflows
df["sip_inflow_crore"] = pd.to_numeric(
    df["sip_inflow_crore"],
    errors="coerce"
)

# Remove invalid rows
df = df.dropna(
    subset=["month", "sip_inflow_crore"]
)

# Keep only non-negative inflows
df = df[df["sip_inflow_crore"] >= 0]

# Sort chronologically
df = df.sort_values("month")

# Save cleaned file
output_file = "C:/Users/vnaga/MutualFund_ETL/data/processed/monthly_sip_inflows_clean.csv"

df.to_csv(output_file, index=False)

print("Cleaned Shape:", df.shape)
print(f"Saved to: {output_file}")