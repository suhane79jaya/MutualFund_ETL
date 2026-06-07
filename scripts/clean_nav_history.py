import pandas as pd

# Load data
df = pd.read_csv("C:/Users/vnaga/MutualFund_ETL/data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

# -----------------------------------
# 1. Parse dates to datetime
# -----------------------------------
df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce",
    dayfirst=True
)

# Remove rows with invalid dates
df = df.dropna(subset=["date"])

# -----------------------------------
# 2. Remove duplicates
# -----------------------------------
df = df.drop_duplicates()

# -----------------------------------
# 3. Sort by amfi_code and date
# -----------------------------------
df = df.sort_values(
    by=["amfi_code", "date"]
).reset_index(drop=True)

# -----------------------------------
# 4. Validate NAV > 0
# -----------------------------------
df["nav"] = pd.to_numeric(
    df["nav"],
    errors="coerce"
)

invalid_nav = df[
    (df["nav"] <= 0) |
    (df["nav"].isna())
]

print("\nInvalid NAV Records:")
print(invalid_nav)

# Keep only valid NAV values
df = df[df["nav"] > 0]

# -----------------------------------
# 5. Forward-fill missing NAV
#    within each AMFI code
# -----------------------------------
df["nav"] = (
    df.groupby("amfi_code")["nav"]
      .ffill()
)

# -----------------------------------
# 6. Final validation
# -----------------------------------
print("\nCleaned Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDate Range:")
print(df["date"].min(), "to", df["date"].max())

# -----------------------------------
# 7. Save cleaned file
# -----------------------------------
output_path = "C:/Users/vnaga/MutualFund_ETL/data/processed/nav_history_clean.csv"

df.to_csv(output_path, index=False)

print(f"\nCleaned file saved to: {output_path}")