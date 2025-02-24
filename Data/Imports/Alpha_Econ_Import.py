import requests
import pandas as pd
import time
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# API Key
API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

# Base URL
BASE_URL = "https://www.alphavantage.co/query"

# Functions and Parameters
economic_indicators = {
    "REAL_GDP": "REAL_GDP",
    "REAL_GDP_PER_CAPITA": "REAL_GDP_PER_CAPITA",
    "FEDERAL_FUNDS_RATE": "FEDERAL_FUNDS_RATE",
    "TREASURY_YIELD_3M": {"function": "TREASURY_YIELD", "maturity": "3month"},
    "TREASURY_YIELD_2Y": {"function": "TREASURY_YIELD", "maturity": "2year"},
    "TREASURY_YIELD_10Y": {"function": "TREASURY_YIELD", "maturity": "10year"},
    "TREASURY_YIELD_30Y": {"function": "TREASURY_YIELD", "maturity": "30year"},
    "INFLATION": "INFLATION",
    "CPI": "CPI",
    "RETAIL_SALES": "RETAIL_SALES",
    "UNEMPLOYMENT": "UNEMPLOYMENT",
    "NONFARM_PAYROLL": "NONFARM_PAYROLL"
}

# Data Storage
dataframes = []

# Function to fetch data from Alpha Vantage API
def fetch_data(params):
    params["apikey"] = API_KEY
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching {params['function']}: {response.status_code}")
        return None

# Loop through each indicator
for indicator, details in economic_indicators.items():
    print(f"Fetching {indicator}...")
    
    if isinstance(details, dict):
        params = {"function": details["function"], "interval": "monthly", "maturity": details["maturity"]}
    else:
        params = {"function": details}
    
    # Fetch data
    json_data = fetch_data(params)

    if json_data:
        try:
            # Identify if the response is a dictionary or a list
            if isinstance(json_data, dict):
                # Find the key containing time series data
                time_series_key = next((key for key in json_data.keys() if "Time Series" in key or "data" in key), None)

                if time_series_key and isinstance(json_data[time_series_key], dict):
                    # Convert JSON dictionary to DataFrame
                    df = pd.DataFrame.from_dict(json_data[time_series_key], orient="index")

                    # Reset index and rename columns
                    df.reset_index(inplace=True)
                    df.rename(columns={"index": "date"}, inplace=True)
                    df["date"] = pd.to_datetime(df["date"])
                    df["indicator"] = indicator
                    dataframes.append(df)

                elif time_series_key and isinstance(json_data[time_series_key], list):
                    # Convert JSON list to DataFrame
                    df = pd.DataFrame(json_data[time_series_key])

                    # Ensure a 'date' column exists
                    if "date" in df.columns:
                        df["date"] = pd.to_datetime(df["date"])
                    else:
                        print(f"Warning: No 'date' column found in {indicator}. Data may be missing.")
                    
                    df["indicator"] = indicator
                    dataframes.append(df)
                
                else:
                    print(f"Unexpected format for {indicator}. Skipping.")

            else:
                print(f"Unexpected data type for {indicator}: {type(json_data)}")

        except Exception as e:
            print(f"Error processing {indicator}: {e}")

    # Sleep to avoid rate limits
    time.sleep(20)

# Combine all data
if dataframes:
    final_df = pd.concat(dataframes, ignore_index=True)
    final_df.to_csv("economic_indicators.csv", index=False)
    print("Data collection complete. Saved as 'economic_indicators.csv'.")
else:
    print("No data was collected. Check API responses.")
