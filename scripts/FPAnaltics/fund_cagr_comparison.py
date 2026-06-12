import pandas as pd

# Load NAV data and prepare
df = pd.read_csv("C:/Users/vnaga/MutualFund_ETL/data/processed/nav_history_clean.csv")


df["date"] = pd.to_datetime(df["date"])

df = df.sort_values(["amfi_code", "date"])

#Function to Calculate CAGR
def calculate_cagr(nav_start, nav_end, years):
    return ((nav_end / nav_start) ** (1 / years)) - 1

#from datetime import timedelta
#Calculate CAGR for Each Scheme
latest_date = df["date"].max()

results = []

for scheme, group in df.groupby("amfi_code"):

    group = group.sort_values("date")

    latest_nav = group.iloc[-1]["nav"]

    row = {
        "amfi_code": scheme
    }

    for years in [1, 3, 5]:

        target_date = latest_date - pd.DateOffset(years=years)

        historical = group[
            group["date"] <= target_date
        ]

        if len(historical) > 0:

            start_nav = historical.iloc[-1]["nav"]

            cagr = calculate_cagr(
                start_nav,
                latest_nav,
                years
            )

            row[f"{years}Y_CAGR"] = round(cagr * 100, 2)

        else:
            row[f"{years}Y_CAGR"] = None

    results.append(row)

cagr_table = pd.DataFrame(results)

#View Comparison Table
print(cagr_table.head())

#Rank Funds by 5-Year CAGR
top_funds = cagr_table.sort_values(
    "5Y_CAGR",
    ascending=False
)
print("Top 10 funds")
print(top_funds.head(10))

cagr_table.to_csv(
    "C:/Users/vnaga/MutualFund_ETL/data/processed/Fund_Per_analytics/fund_cagr_comparison.csv",
    index=False
)
print("Validation Checks:")
print(cagr_table.describe())