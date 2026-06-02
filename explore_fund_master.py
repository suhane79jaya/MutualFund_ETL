import pandas as pd

# Load data
df = pd.read_csv("data/raw/01_fund_master.csv")

# Basic information
print("Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df)
#Explore fund master — print unique fund houses, 
# categories, sub-categories, risk grades. Understand AMFI scheme code structure.

#print unique fund house
print("\nUnique Fund Houses:")
print(df["fund_house"].unique())

print("\nNumber of Fund Houses:")
print(df["fund_house"].nunique())

#print unique categories
print("\nUnique Categories:")
print(df["category"].unique())

print("\nNumber of Categories:")
print(df["category"].nunique())
#Unique Subcategories
print("\nUnique Sub-Categories:")
print(df["sub_category"].unique())

print("\nNumber of Sub-Categories:")
print(df["sub_category"].nunique())

print(df.columns)

print("\nRisk Grades:")
print(df["risk_category"].value_counts())

#The AMFI/MFAPI scheme code is a unique identifier for each scheme.
print(df[["amfi_code", "scheme_name"]].head(20))

#check uniqueness
print("Total Records:", len(df))
print("Unique Scheme Codes:", df["amfi_code"].nunique())