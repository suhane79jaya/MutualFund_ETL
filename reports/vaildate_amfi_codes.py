import pandas as pd

# Load files
fund_master = pd.read_csv("../data/raw/01_fund_master.csv")
nav_history = pd.read_csv("../data/raw/all_funds_nav.csv")
# Unique codes
master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["scheme_code"])

# Comparison
missing_in_nav = master_codes - nav_codes
match_pct = (
    (len(master_codes) - len(missing_in_nav))
    / len(master_codes)
) * 100

print("\n===== DATA QUALITY SUMMARY =====")
print(f"Fund Master Codes : {len(master_codes)}")
print(f"NAV Codes         : {len(nav_codes)}")
print(f"Matched Codes     : {len(master_codes)-len(missing_in_nav)}")
print(f"Missing Codes     : {len(missing_in_nav)}")
print(f"Coverage          : {match_pct:.2f}%")