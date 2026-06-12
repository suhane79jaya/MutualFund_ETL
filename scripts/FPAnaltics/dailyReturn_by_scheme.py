import pandas as pd

# Load NAV data
df = pd.read_csv("C:/Users/vnaga/MutualFund_ETL/data/processed/nav_history_clean.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Sort data
df = df.sort_values(["amfi_code", "date"])

#Compute Daily Returns
df["daily_return"] = (
    df.groupby("amfi_code")["nav"]
      .pct_change()
)

print(df[["amfi_code", "date", "nav", "daily_return"]].head(10))

# Validate Distribution
# Summary Statistics
returns = df["daily_return"].dropna()

print(returns.describe())

# Expected:
# Mean close to 0
# Most returns between -5% and +5%
# Very few extreme values

#Detect Outliers
outliers = df[
    (df["daily_return"] > 0.20) |
    (df["daily_return"] < -0.20)
]

print("Outliers:", len(outliers))
print(outliers.head())

# Outliers: 0 means:

# ✅ No daily return was greater than +20%

# ✅ No daily return was less than -20%

# ✅ Your NAV data appears reasonable according to this validation rule

# For mutual funds, this is generally a good sign because daily NAV changes are usually small (often less than ±5%).

print("Daily Return",df["daily_return"].describe())

print("Maximum Return:", df["daily_return"].max())
print("Minimum Return:", df["daily_return"].min())

#finds the 10 rows with the highest daily returns.
print(df.nlargest(10, "daily_return")[[
    "amfi_code",
    "date",
    "daily_return"
]])

print(df.nsmallest(10, "daily_return")[[
    "amfi_code",
    "date",
    "daily_return"
]])
