# 📊 DataFoundation: Financial Reporting Automation Framework with BigQuery and GCP

## 🚀 Streak Projects

This project aims to develop a practical **Financial Reporting Automation Framework** that:

- Consolidates financial data from **Yahoo Finance** and **Kaggle**
- Applies transformations using **Python (Pandas)**
- Loads data into a **dimensional model in BigQuery**
- Automates **period-end analysis**
- Provides **customizable financial statements** through a **Streamlit dashboard**

---

## 🎯 Objective

The primary objective is to **automate the financial reporting process**, normalize financial data, and generate insightful reports.

---

## 🛠 Tools Used

| Tool                           | Purpose                                   |
| ------------------------------ | ----------------------------------------- |
| **Python** (Pandas, yfinance)  | Data extraction, transformation           |
| **BigQuery**                   | Data warehousing                          |
| **Streamlit**                  | Interactive financial reporting dashboard |
| **Yahoo Finance API**          | Stock price & financial data extraction   |
| **Kaggle Financial Open Data** | Historical financial datasets             |

---

## 📂 Dataset Overview

The dataset includes the following key financial data points:

| Column Name      | Description                     |
| ---------------- | ------------------------------- |
| `Date`           | Timestamp of financial data     |
| `Open`           | Opening stock price             |
| `High`           | Highest stock price of the day  |
| `Low`            | Lowest stock price of the day   |
| `Close`          | Closing stock price             |
| `Volume`         | Number of shares traded         |
| `Dividends`      | Dividend payouts                |
| `Stock Splits`   | Stock split events              |
| `Ticker`         | Stock symbol (e.g., AAPL, TSLA) |
| `company_id`     | Unique company identifier       |
| `name_latest`    | Latest company name             |
| `names_previous` | Previous company names          |
| `indicator_id`   | Financial indicator reference   |
| `2010-2016`      | Historical financial data       |

---

## 🔄 Implementation Workflow

### **Step 1: Data Extraction**

- Fetch **real-time & historical stock market data** from `yfinance`.
- Extract **financial data from Kaggle datasets**.

### **Step 2: Data Transformation & Cleaning**

- Use **Pandas** to clean and normalize the data.
- Handle **missing values** and remove duplicates.
- Convert data into a **structured format**.

### **Step 3: Data Loading into BigQuery**

- Store cleaned data in **BigQuery's dimensional model**.
- Optimize table structure for **efficient querying**.

### **Step 4: Financial Analysis & Automation**

- Automate **period-end financial reporting**.
- Generate key financial metrics **(e.g., revenue, profit, stock performance)**.

### **Step 5: Streamlit Dashboard Development**

- Build an **interactive UI** to display financial reports.
- Implement **trend visualizations** using `Plotly`.

---

## 📊 Streamlit Dashboard Features

✅ **Key Financial Metrics Display**

✅ **Stock Price Trends Visualization**

✅ **Customizable Financial Statements**

✅ **Company-wise Data Filtering**

✅ **Real-time Stock Data Updates**

---
🚀 Missing Dataset Notice:

Due to storage limitations, we were unable to upload one dataset. You can download it manually from Kaggle:

🔗 US Stocks Fundamentals Dataset : https://www.kaggle.com/datasets/usfundamentals/us-stocks-fundamentals

Once downloaded, place the dataset in the appropriate directory for further processing.
---

## 💡 How to Run the Project

### **1️⃣ Set up Environment & Dependencies**

```bash
pip install pandas google-cloud-bigquery streamlit yfinance plotly
```

### **2️⃣ Authenticate Google BigQuery**

```bash
set GOOGLE_APPLICATION_CREDENTIALS="path/to/Credentials.json"
or
Add Credientials.json file
```

### **3️⃣ Run Streamlit Dashboard**

```bash
streamlit run financial_dashboard.py
```



## 📢 Contributing

Feel free to contribute by reporting issues, suggesting improvements, or adding new features!

---

## 🔗 License

This project is licensed under the **MIT License**.

