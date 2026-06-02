import requests
import pandas as pd

schemes = {
    "SBI Bluechip": "119551",
    "ICICI Bluechip": "120503",
    "Nippon Large Cap": "118632",
    "Axis Bluechip": "119092",
    "Kotak Bluechip": "120841"
}

all_data = []

for scheme_name, scheme_code in schemes.items():
    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame(data["data"])
    df["scheme_name"] = scheme_name
    df["scheme_code"] = scheme_code

    all_data.append(df)

final_df = pd.concat(all_data, ignore_index=True)

final_df.to_csv("data/raw/all_funds_nav.csv", index=False)

print("Combined CSV saved successfully!")