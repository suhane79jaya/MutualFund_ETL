import requests
import pandas as pd

# MFAPI endpoint
url = "https://api.mfapi.in/mf/125497"

try:
    response = requests.get(url, timeout=10)

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        try:
            data = response.json()
            print("JSON loaded successfully")
        except ValueError:
            print("Response is not valid JSON")
            print(response.text[:500])
    else:
        print("Request failed")
        print(response.text[:500])

except requests.exceptions.RequestException as e:
    print("Request error:", e)

# # Fetch data
# response = requests.get(url)

# # Convert JSON to Python dictionary
# data = response.json()


# Extract NAV history
nav_data = data["data"]

# Convert to DataFrame
df = pd.DataFrame(nav_data)

# Save as CSV
df.to_csv("C:/Users/vnaga/Mutualfund_ETL/data/raw/hdfc_top100_nav_raw.csv", index=False)

print("CSV file saved successfully!")
print(df.head())