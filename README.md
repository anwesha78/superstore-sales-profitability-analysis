# Retail Sales & Profitability Analysis — Superstore

End-to-end retail analytics project: cleaned and analyzed 10K+ orders, engineered time-series and profitability features, built a sales forecast, and published an interactive Tableau dashboard translating the findings into a business recommendation.

**Live Dashboard:** https://public.tableau.com/views/SuperstoreSalesProfitabilityAnalysis_17829393123710/RetailSalesProfitabilityAnalysisSuperstore

## Overview

Retail businesses generate enormous volumes of order-level data but often lack a clear read on *where* profit is actually being made or lost. This project analyzes the Sample Superstore dataset (US retail orders, 2014–2017) to answer three questions a consulting client would actually ask:

1. Is the business growing, and can we forecast near-term sales?
2. Which product categories are profitable, and which are dragging the business down?
3. Is our discounting strategy helping or hurting the bottom line?

## Key Findings

- **Discounts above 20% eliminate profit almost entirely.** Orders with no discount carry a 34% average profit margin; orders discounted 21–30% average **-11.5%** margin, with 91.6% of them losing money outright.
- **Furniture is dragging overall profitability down.** It generates 32% of total sales but only 6% of total profit (2.5% margin vs. 17%+ for Technology and Office Supplies), driven almost entirely by losses on Tables (-$17,725) and Bookcases (-$3,473).
- **Central region underperforms** other regions on margin (7.9% vs. 14.9% in the West) despite comparable sales volume.

**Recommendation:** Cap standard discounts at 20% except for approved clearance SKUs, and review Furniture pricing/supplier costs — particularly for Tables.

## Tech Stack

- **Python:** Pandas, NumPy — data cleaning and feature engineering
- **Scikit-learn:** Linear Regression — sales forecasting
- **Matplotlib:** forecast visualization
- **Tableau Public:** interactive dashboard

## Pipeline

1. **`01_clean_data.py`** — loads raw data, checks for missing values/duplicates, corrects data types (dates, postal codes), and engineers new features: Order Year/Month, Shipping Delay, Profit Margin, Loss flag.
2. **`02_eda.py`** — exploratory analysis: overall business snapshot, discount-vs-profit relationship, category/sub-category performance, regional performance, and monthly sales aggregation.
3. **`03_forecast.py`** — fits a linear regression model on time trend + month-of-year seasonality to forecast the next 3 months of sales (R² = 0.89, MAE ≈ $6,600 on 48 months of historical data).
4. **Tableau dashboard** — three connected visuals (monthly sales trend, profit by category, profit by discount band) plus a written insight/recommendation panel, published to Tableau Public.

## Dataset

Source: Sample Superstore (US retail orders), 9,994 rows, 21 original columns (27 after feature engineering).

## Repository Structure

```
├── 01_clean_data.py          # Cleaning & feature engineering
├── 02_eda.py                 # Exploratory data analysis
├── 03_forecast.py            # Sales forecasting model
├── superstore.csv            # Raw dataset
├── superstore_cleaned.csv    # Cleaned dataset (output of step 1)
├── monthly_sales.csv         # Aggregated monthly sales (output of step 2)
├── sales_forecast.csv        # 3-month forecast output (output of step 3)
├── sales_forecast.png        # Forecast chart
└── README.md
```

<img width="1025" height="783" alt="image" src="https://github.com/user-attachments/assets/7e7f4ab2-f8ed-4451-8874-cd8504908fc5" />


## Author

[Anwesha Sahoo — [https://www.linkedin.com/in/anwesha-sahoo-bb94ab411]
