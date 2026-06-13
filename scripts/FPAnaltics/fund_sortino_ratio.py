import pandas as pd
import numpy as np



# Load NAV data and prepare
nav_df = pd.read_csv("C:/Users/vnaga/MutualFund_ETL/data/processed/nav_history_clean.csv")
nav_df.columns

#Compute Daily Returns
nav_df = nav_df.sort_values(["amfi_code", "date"])

nav_df["daily_return"] = (
    nav_df.groupby("amfi_code")["nav"]
      .pct_change()
)

annual_rf = 0.065
daily_rf = annual_rf / 252

results = []

for fund, group in nav_df.groupby("amfi_code"):

    returns = group["daily_return"].dropna()

    if len(returns) < 30:
        continue

    mean_return = returns.mean()

    excess_returns = returns - daily_rf

    downside_returns = excess_returns[excess_returns < 0]

    if len(downside_returns) < 2:
        sortino = np.nan
    else:
        downside_std = downside_returns.std()

        sortino = (
            (mean_return - daily_rf)
            / downside_std
        ) * np.sqrt(252)

    results.append({
        "amfi_code": fund,
        "Sortino_Ratio": round(sortino, 4)
    })

sortino_df = pd.DataFrame(results)
#Rank All Funds
sortino_df = (
    sortino_df
    .sort_values("Sortino_Ratio", ascending=False)
    .reset_index(drop=True)
)

sortino_df["Rank"] = sortino_df.index + 1

print(sortino_df.head(40))