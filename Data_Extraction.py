# import pandas as pd
# import yfinance as yf
# from google.cloud import bigquery

# # Load company data
# companies = pd.read_csv(r"C:\Users\ANANDITH\Desktop\Financial Reporting Automation\companies.csv")
# indicators = pd.read_csv(r"C:\Users\ANANDITH\Desktop\Financial Reporting Automation\indicators_by_company.csv")

# # Get stock tickers manually or via API
# tickers = {"Sandisk Corp": "SNDK", "Medallion Financial Corp": "MFIN"}

# # Extract Yahoo Finance stock data
# def get_stock_data(ticker):
#     stock = yf.Ticker(ticker)
#     df = stock.history(period="5y")  # Get last 5 years of data
#     df['Ticker'] = ticker
#     return df.reset_index()

# # Collect stock data for all tickers
# stock_data = pd.concat([get_stock_data(t) for t in tickers.values()])
# stock_data.to_csv(r"C:\Users\ANANDITH\Desktop\Financial Reporting Automation\yahoo_finance_dataset.csv", index=False)  # Save locally
import pandas as pd
import yfinance as yf

# Define correct tickers
tickers = {"Apple Inc": "AAPL", "Microsoft Corp": "MSFT"}  # Use well-known companies for testing

# Extract Yahoo Finance stock data
def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    df = stock.history(period="5y")  # Get last 5 years of data
    
    if df.empty:
        print(f"❌ No data found for {ticker}!")
        return pd.DataFrame()  # Return empty DataFrame if no data

    df['Ticker'] = ticker
    print(f"✅ Data fetched for {ticker}")
    return df.reset_index()

# Collect stock data for all tickers
stock_data_list = [get_stock_data(t) for t in tickers.values()]
stock_data = pd.concat(stock_data_list, ignore_index=True)

# Save only if data exists
if not stock_data.empty:
    stock_data.to_csv(r"C:\Users\ANANDITH\Desktop\Financial Reporting Automation\yahoo_finance_dataset.csv", index=False)
    print("📁 Data saved successfully!")

# Display first few rows
print(stock_data.head())
