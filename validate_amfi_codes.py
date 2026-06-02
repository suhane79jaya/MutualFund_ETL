import pandas as pd

# Load files
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/all_funds_nav.csv")
print(fund_master.head())
# Convert to string for safe comparison
fund_master["amfi_code"] = fund_master["amfi_code"].astype(str)
nav_history["scheme_code"] = nav_history["scheme_code"].astype(str)

# Unique codes
master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["scheme_code"])

# Comparison
missing_in_nav = master_codes - nav_codes
extra_in_nav = nav_codes - master_codes

print("Total Fund Master Codes:", len(master_codes))
print("Total NAV Codes:", len(nav_codes))

print("\nMissing in NAV History:", len(missing_in_nav))
print("Extra in NAV History:", len(extra_in_nav))

if missing_in_nav:
    print("\nCodes Missing in NAV History:")
    for code in sorted(missing_in_nav):
        print(code)
else:
    print("\nAll AMFI codes have NAV data.")

   