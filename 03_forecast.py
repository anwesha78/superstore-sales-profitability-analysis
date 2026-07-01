"""
Project A - Retail Sales Analytics & Forecasting
Step 3: Sales Forecasting
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

monthly = pd.read_csv("monthly_sales.csv")
monthly["Order Year-Month"] = pd.to_datetime(monthly["Order Year-Month"])
monthly = monthly.sort_values("Order Year-Month").reset_index(drop=True)

# ---- Feature engineering for the model ----
# Time_Index: 0,1,2... captures the overall growth trend
# Month: 1-12, captures seasonality (e.g. Nov/Dec spikes from holiday shopping)
monthly["Time_Index"] = np.arange(len(monthly))
monthly["Month"] = monthly["Order Year-Month"].dt.month

X = monthly[["Time_Index", "Month"]]
y = monthly["Sales"]

# One-hot encode month so the model can learn a separate seasonal effect per month
X_encoded = pd.get_dummies(X, columns=["Month"], drop_first=True)

model = LinearRegression()
model.fit(X_encoded, y)

# ---- Evaluate on the data we have ----
predictions = model.predict(X_encoded)
mae = mean_absolute_error(y, predictions)
r2 = r2_score(y, predictions)
print(f"Model fit on {len(monthly)} months of data")
print(f"Mean Absolute Error: ${mae:,.0f}")
print(f"R² Score: {r2:.3f}  (how much of the sales variation the model explains)")

# ---- Forecast next 3 months ----
last_date = monthly["Order Year-Month"].max()
future_dates = pd.date_range(last_date, periods=4, freq="MS")[1:]  # next 3 months
future = pd.DataFrame({
    "Order Year-Month": future_dates,
    "Time_Index": np.arange(len(monthly), len(monthly) + 3),
    "Month": future_dates.month
})
future_encoded = pd.get_dummies(future[["Time_Index", "Month"]], columns=["Month"], drop_first=True)
future_encoded = future_encoded.reindex(columns=X_encoded.columns, fill_value=0)

future["Predicted_Sales"] = model.predict(future_encoded)

print("\nForecast for next 3 months:")
print(future[["Order Year-Month", "Predicted_Sales"]].to_string(index=False))

# ---- Save chart: actual vs fitted + forecast ----
plt.figure(figsize=(10, 5))
plt.plot(monthly["Order Year-Month"], monthly["Sales"], label="Actual Sales", marker="o")
plt.plot(monthly["Order Year-Month"], predictions, label="Model Fit", linestyle="--")
plt.plot(future["Order Year-Month"], future["Predicted_Sales"], label="Forecast (next 3 months)",
          marker="o", linestyle="--", color="red")
plt.title("Monthly Sales: Actual vs Forecast")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_forecast.png", dpi=150)
print("\nSaved chart: sales_forecast.png")

future.to_csv("sales_forecast.csv", index=False)
print("Saved sales_forecast.csv")