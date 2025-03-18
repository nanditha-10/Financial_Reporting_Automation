

import pandas as pd

# Load datasets
stock_data = pd.read_csv("path_of_your_yahoo_finance_dataset.csv")
indicators = pd.read_csv("path_of_your_indicators_by_company.csv")
companies = pd.read_csv("path_of_your_companies.csv")

# Merge stock data with company details
merged_data = stock_data.merge(companies, left_on="Ticker", right_on="name_latest", how="left")

# Merge with indicators
final_data = merged_data.merge(indicators, on="company_id", how="left")

# Convert Date column to datetime format with UTC to fix FutureWarning
if "Date" in final_data.columns:
    final_data["Date"] = pd.to_datetime(final_data["Date"], errors="coerce", utc=True)

# Fill missing values
for col in final_data.select_dtypes(include=['number']).columns:
    final_data[col] = final_data[col].fillna(0)  # Fill NaN in numeric columns with 0

for col in final_data.select_dtypes(include=['object']).columns:
    final_data[col] = final_data[col].fillna("Unknown")  # Fill NaN in text columns with "Unknown"

# Save merged data
output_path = r"C:\Users\ANANDITH\Desktop\Financial Reporting Automation\merged_financial_data.csv"
final_data.to_csv(output_path, index=False)

print("✅ Merged data saved successfully (missing details handled).")
print(final_data.head())
