# 🌾 Farmers Market Data Analysis

A data analytics project that explores farmers market sales data using Python, Pandas, and Matplotlib. The project focuses on identifying pricing trends, crop demand patterns, and profit insights to support data-driven decision-making for farmers and agricultural businesses.

---

## 📌 Project Overview

This project analyzes a real-world farmers market dataset to answer key business questions such as:

- How do crop prices change over time?
- Which crops have the highest demand?
- Which crops generate the most profit?
- How does profit vary month by month?

The analysis includes professional data preprocessing, feature engineering, and visualizations suitable for a data analyst or AI/ML internship portfolio.

---

## 🎯 Business Objectives

- Monitor crop price trends.
- Identify top-selling crops by quantity.
- Compare profitability across crops.
- Track monthly profit performance.
- Generate actionable insights for farmers and market managers.

---

## 🛠️ Technologies Used

- Python
- [Pandas](https://pandas.pydata.org?utm_source=chatgpt.com)
- [Matplotlib](https://matplotlib.org?utm_source=chatgpt.com)
- Jupyter Notebook / VS Code

---

## 📂 Dataset

**File:** `farmers_market_master.csv`

### Key Columns

| Column | Description |
|------|------|
| `date` | Transaction date |
| `crop` | Crop name |
| `price_per_kg` | Selling price per kilogram |
| `cost_per_kg` | Production cost per kilogram |
| `quantity_sold_kg` | Quantity sold |
| `market` | Market location |
| `weather` | Weather condition |

---

## 📈 Analyses Performed

### 1. Crop Price Trend Analysis
Tracks historical price movements for crops such as Tomato using line charts and moving averages.

### 2. Demand Analysis
Ranks crops by total quantity sold to identify highest-demand produce.

### 3. Profit Analysis
Calculates profit using:

```python
profit = (price_per_kg - cost_per_kg) * quantity_sold_kg
