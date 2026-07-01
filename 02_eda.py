"""
Project A - Retail Sales Analytics & Forecasting
Step 2: Exploratory Data Analysis
"""

import pandas as pd

df = pd.read_csv("superstore_cleaned.csv", parse_dates=["Order Date", "Ship Date"])

print("=" * 60)
print("1. OVERALL BUSINESS SNAPSHOT")
print("=" * 60)
print(f"Total Sales:  ${df['Sales'].sum():,.0f}")
print(f"Total Profit: ${df['Profit'].sum():,.0f}")
print(f"Overall Profit Margin: {df['Profit'].sum() / df['Sales'].sum() * 100:.1f}%")
print(f"Total Orders: {df['Order ID'].nunique():,}")

print("\n" + "=" * 60)
print("2. THE DISCOUNT-PROFIT RELATIONSHIP (why 18.7% of orders lose money)")
print("=" * 60)
bins = [-0.01, 0, 0.2, 0.3, 0.5, 0.8]
labels = ["0% (no discount)", "1-20%", "21-30%", "31-50%", "51-80%"]
df["Discount Band"] = pd.cut(df["Discount"], bins=bins, labels=labels)
discount_impact = df.groupby("Discount Band", observed=True).agg(
    Orders=("Order ID", "count"),
    Avg_Profit_Margin=("Profit Margin", "mean"),
    Loss_Rate=("Is Loss Making", "mean")
).round(3)
print(discount_impact)

print("\n" + "=" * 60)
print("3. CATEGORY & SUB-CATEGORY PERFORMANCE")
print("=" * 60)
cat_perf = df.groupby("Category").agg(
    Sales=("Sales", "sum"), Profit=("Profit", "sum")
).round(0)
cat_perf["Margin %"] = (cat_perf["Profit"] / cat_perf["Sales"] * 100).round(1)
print(cat_perf.sort_values("Profit", ascending=False))

print("\nWorst 5 sub-categories by profit:")
subcat_perf = df.groupby("Sub-Category").agg(
    Sales=("Sales", "sum"), Profit=("Profit", "sum")
).round(0)
print(subcat_perf.sort_values("Profit").head(5))

print("\n" + "=" * 60)
print("4. REGIONAL PERFORMANCE")
print("=" * 60)
region_perf = df.groupby("Region").agg(
    Sales=("Sales", "sum"), Profit=("Profit", "sum")
).round(0)
region_perf["Margin %"] = (region_perf["Profit"] / region_perf["Sales"] * 100).round(1)
print(region_perf.sort_values("Profit", ascending=False))

print("\n" + "=" * 60)
print("5. MONTHLY SALES TREND (for the forecasting step next)")
print("=" * 60)
monthly = df.groupby("Order Year-Month").agg(Sales=("Sales", "sum")).reset_index()
print(monthly.tail(6))
monthly.to_csv("monthly_sales.csv", index=False)
print("\nSaved monthly_sales.csv for the forecasting step.")