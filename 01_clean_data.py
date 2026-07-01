"""
Project A - Retail Sales Analytics & Forecasting
Step 1: Data Cleaning & Feature Engineering

Dataset: Sample Superstore (US retail orders, 2014-2017)
"""

import pandas as pd
import numpy as np

# ---- Load ----
df = pd.read_csv("superstore.csv", encoding="latin1")
print(f"Loaded {df.shape[0]} rows, {df.shape[1]} columns")

# ---- Data quality checks (document these even if the news is good) ----
print("\nMissing values per column:")
print(df.isnull().sum()[df.isnull().sum() > 0] if df.isnull().sum().sum() > 0 else "None found")

print(f"\nDuplicate rows: {df.duplicated().sum()}")
df = df.drop_duplicates()

# ---- Type corrections ----
# Dates are stored as strings — must convert before any time-based analysis
df["Order Date"] = pd.to_datetime(df["Order Date"], format="%m/%d/%Y")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%m/%d/%Y")

# Postal Code is an ID, not a quantity — keep as string so it's never summed/averaged by mistake
df["Postal Code"] = df["Postal Code"].astype(str)

# ---- Sanity checks on numeric fields ----
# Negative or zero sales/profit rows are worth flagging, not silently dropping
print(f"\nOrders with negative profit (losses): {(df['Profit'] < 0).sum()} "
      f"({(df['Profit'] < 0).mean()*100:.1f}% of all orders)")
print(f"Orders with zero quantity: {(df['Quantity'] == 0).sum()}")
print(f"Discount range: {df['Discount'].min()} to {df['Discount'].max()}")

# ---- Feature engineering ----
df["Order Year"] = df["Order Date"].dt.year
df["Order Month"] = df["Order Date"].dt.month
df["Order Year-Month"] = df["Order Date"].dt.to_period("M").astype(str)
df["Shipping Delay (days)"] = (df["Ship Date"] - df["Order Date"]).dt.days

df["Profit Margin"] = np.where(df["Sales"] != 0, df["Profit"] / df["Sales"], 0)
df["Is Loss Making"] = df["Profit"] < 0

# ---- Save cleaned dataset ----
df.to_csv("superstore_cleaned.csv", index=False)
print(f"\nSaved cleaned dataset: {df.shape[0]} rows, {df.shape[1]} columns -> superstore_cleaned.csv")