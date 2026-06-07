import pandas as pd

# Load file
df = pd.read_csv("C:/Users/vnaga/MUTUALFUND_ETL/data/raw/07_scheme_performance.csv")

print("Original Shape:", df.shape)
print(df.columns.tolist())
# ----------------------------------
# Remove duplicates
# ----------------------------------
df = df.drop_duplicates()

# ----------------------------------
# Return columns
# ----------------------------------
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

# ----------------------------------
# Validate numeric return values
# ----------------------------------
for col in return_cols:
    if col in df.columns:

        # Convert to numeric
        df[col] = pd.to_numeric(df[col], errors="coerce")

        invalid_count = df[col].isna().sum()

        print(f"{col} - Invalid Values: {invalid_count}")

# ----------------------------------
# Flag anomalies
# ----------------------------------
anomaly_records = []

for col in return_cols:
    if col in df.columns:

        anomalies = df[
            (df[col] < -100) |
            (df[col] > 200)
        ]

        if not anomalies.empty:
            print(f"\nAnomalies detected in {col}:")
            print(anomalies[[col]])

            anomaly_records.append(anomalies)

# ----------------------------------
# Expense Ratio Validation
# Valid Range: 0.1% – 2.5%
# ----------------------------------
df["expense_ratio_pct"] = pd.to_numeric(
    df["expense_ratio_pct"],
    errors="coerce"
)

invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5) |
    (df["expense_ratio_pct"].isna())
]

print("\nInvalid Expense Ratio Records:")
print(invalid_expense[["expense_ratio_pct"]])

# ----------------------------------
# Keep only valid expense ratios
# ----------------------------------
df = df[
    (df["expense_ratio_pct"] >= 0.1) &
    (df["expense_ratio_pct"] <= 2.5)
]
print("\nValid Expense Ratio Records:")
print(df[["expense_ratio_pct"]])
# ----------------------------------
# Remove rows with missing returns
# ----------------------------------
df = df.dropna(subset=return_cols)

# ----------------------------------
# Save cleaned file
# ----------------------------------
output_file = "C:/Users/vnaga/MUTUALFUND_ETL/data/processed/clean_scheme_performance.csv"

df.to_csv(output_file, index=False)

print("\nCleaning Completed")
print("Final Shape:", df.shape)
print(f"\n cleaning file Saved to: {output_file}")