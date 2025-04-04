import pandas as pd
from google.oauth2 import service_account
from pandas_gbq import to_gbq

# Google Cloud details
PROJECT_ID = "Your_project_id"
DATASET_ID = "financial_reporting"  # Use the dataset you created
TABLE_ID = "financial_data"
TABLE_PATH = f"{DATASET_ID}.{TABLE_ID}"

# Load data
file_path = "path_of_merged_financial_data.csv"
df = pd.read_csv(file_path)

# Authenticate using service account JSON
credentials_path = "path_of_your_Credentials.json"
credentials = service_account.Credentials.from_service_account_file(credentials_path)

# Upload to BigQuery
to_gbq(df, TABLE_PATH, project_id=PROJECT_ID, credentials=credentials, if_exists="replace")

print(f"✅ Data successfully uploaded to BigQuery: {TABLE_PATH}")
