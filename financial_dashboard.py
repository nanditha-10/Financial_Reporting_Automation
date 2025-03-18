import os
import streamlit as st
from google.cloud import bigquery
import pandas as pd
import plotly.express as px

# ✅ Set Google Cloud credentials inside the script
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path_of_your_Credentials.json"

# ✅ Set up BigQuery client
client = bigquery.Client()

# ✅ Your BigQuery table details
PROJECT_ID = "path_of_project_id"
DATASET = "financial_reporting"
TABLE = "financial_data"
TABLE_PATH = f"{PROJECT_ID}.{DATASET}.{TABLE}"

# ✅ Fetch data from BigQuery
@st.cache_data
def fetch_data():
    query = f"SELECT * FROM `{TABLE_PATH}`"
    df = client.query(query).to_dataframe()
    return df

# ✅ Load data
df = fetch_data()

# ✅ Streamlit Dashboard Layout
st.title("📊 Financial Reporting Dashboard")
st.markdown("### Analyze financial trends and key metrics.")

# ✅ Display key metrics
st.subheader("📌 Key Stock Market Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Records", df.shape[0])
col2.metric("Total Volume Traded", f"{df['Volume'].sum():,.0f}")
col3.metric("Average Closing Price", f"${df['Close'].mean():,.2f}")

# ✅ Select stock ticker
tickers = df["Ticker"].unique()
selected_ticker = st.selectbox("Select a Stock", tickers)

# ✅ Filter data
filtered_df = df[df["Ticker"] == selected_ticker]

# ✅ Display stock data table
st.subheader(f"📄 {selected_ticker} Stock Data")
st.dataframe(filtered_df)

# ✅ Stock Price Trend Chart
st.subheader("📈 Stock Price Trends")
fig = px.line(
    filtered_df, 
    x="Date", 
    y=["Open", "High", "Low", "Close"], 
    title=f"Stock Price Trends of {selected_ticker}",
    labels={"Date": "Date", "value": "Price ($)", "variable": "Stock Metric"}
)
st.plotly_chart(fig)

# ✅ Close BigQuery connection
client.close()
