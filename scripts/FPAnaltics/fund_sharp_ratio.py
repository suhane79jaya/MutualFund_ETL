import pandas as pd
import numpy as np


# Load NAV data and prepare
df = pd.read_csv("C:/Users/vnaga/MutualFund_ETL/data/processed/nav_history_clean.csv")
df.columns

#Compute Daily Returns
df["daily_return"] = (
    df.groupby("amfi_code")["nav"]
      .pct_change()
)

RF = 0.065  # 6.5%

results = []

for fund, group in df.groupby("amfi_code"):

    returns = group["daily_return"].dropna()

    if len(returns) < 30:
        continue

    # Annualized return
    annual_return = returns.mean() * 252

    # Annualized volatility
    annual_vol = returns.std() * np.sqrt(252)

    # Sharpe Ratio
    sharpe = (annual_return - RF) / annual_vol

    results.append({
        "amfi_code": fund,
        "annual_return": round(annual_return * 100, 2),
        "annual_volatility": round(annual_vol * 100, 2),
        "sharpe_ratio": round(sharpe, 3)
    })

sharpe_df = pd.DataFrame(results)
#Rank Funds
sharpe_df = sharpe_df.sort_values(
    "sharpe_ratio",
    ascending=False
)
#Negative Sharpe means the fund underperformed the risk-free rate
print("Top Funds")
print(sharpe_df.head(10))
print("Bottom Funds")
print(sharpe_df.tail(10))

sharpe_df.to_csv(
    "C:/Users/vnaga/MutualFund_ETL/data/processed/Fund_Per_analytics/fund_sharpe_ratio.csv",
    index=False
)
print("Statiscal Analysis")
print(sharpe_df["sharpe_ratio"].describe())

