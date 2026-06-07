import pandas as pd

# Load data
df = pd.read_csv("C:/Users/vnaga/MutualFund_ETL/data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

# --------------------------------------------------
# 1. Standardize transaction_type
# --------------------------------------------------

df["transaction_type"] = df["transaction_type"].astype(str).str.strip().str.lower()

transaction_mapping = {
    "sip": "SIP",
    "systematic investment plan": "SIP",

    "lumpsum": "Lumpsum",
    "lump sum": "Lumpsum",

    "redemption": "Redemption",
    "redeem": "Redemption"
}

df["transaction_type"] = df["transaction_type"].replace(transaction_mapping)

# Find invalid transaction types
invalid_txn = df[
    ~df["transaction_type"].isin(["SIP", "Lumpsum", "Redemption"])
]

print("\nInvalid Transaction Types:")
print(invalid_txn[["transaction_type"]])

# --------------------------------------------------
# 2. Validate amount > 0
# --------------------------------------------------

df["amount_inr"] = pd.to_numeric(df["amount_inr"], errors="coerce")

invalid_amount = df[df["amount_inr"] <= 0]

print("\nInvalid Amount Records:")
print(invalid_amount[["amount_inr"]])

# Remove invalid amounts
df = df[df["amount_inr"] > 0]

# --------------------------------------------------
# 3. Fix date formats
# --------------------------------------------------

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce",
    dayfirst=True
)

invalid_dates = df[df["transaction_date"].isna()]

print("\nInvalid Dates:")
print(invalid_dates[["transaction_date"]])

# Remove invalid dates
df = df.dropna(subset=["transaction_date"])

# --------------------------------------------------
# 4. Validate KYC status
# --------------------------------------------------

df["kyc_status"] = (
    df["kyc_status"]
    .astype(str)
    .str.strip()
    .str.upper()
)

valid_kyc = ["VERIFIED", "PENDING", "REJECTED"]

invalid_kyc = df[~df["kyc_status"].isin(valid_kyc)]

print("\nInvalid KYC Status Records:")
print(invalid_kyc[["kyc_status"]])

# --------------------------------------------------
# 5. Remove duplicates
# --------------------------------------------------

df = df.drop_duplicates()

print("\nCleaned Shape:", df.shape)

# --------------------------------------------------
# 6. Save cleaned file
# --------------------------------------------------

output_file = "C:/Users/vnaga/MutualFund_ETL/data/processed/investor_transactions_clean.csv"
df.to_csv(output_file, index=False)

print(f"\nCleaned file saved to: {output_file}")