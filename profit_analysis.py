import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("farmers_market_master.csv", parse_dates=["date"])

df["profit"] = (
    (df["price_per_kg"] - df["cost_per_kg"])
    * df["quantity_sold_kg"]
)

profit_by_crop = (
    df.groupby("crop", as_index=False)["profit"]
      .sum()
      .sort_values("profit", ascending=False)
)

top_n = 10
profit_by_crop = profit_by_crop.head(top_n)

fig, ax = plt.subplots(figsize=(12, 7))

bars = ax.barh(
    profit_by_crop["crop"],
    profit_by_crop["profit"]
)

ax.invert_yaxis()

for bar in bars:
    width = bar.get_width()
    ax.text(
        width,
        bar.get_y() + bar.get_height() / 2,
        f" ₹{width:,.0f}",
        va="center"
    )

ax.set_title(
    "Top 10 Crops by Total Profit",
    fontsize=16,
    fontweight="bold"
)
ax.set_xlabel("Total Profit (₹)")
ax.set_ylabel("Crop")
ax.grid(axis="x", linestyle="--", alpha=0.6)

plt.tight_layout()
plt.show()

monthly_profit = (
    df.groupby(df["date"].dt.to_period("M"))["profit"]
      .sum()
      .reset_index()
)

monthly_profit["date"] = monthly_profit["date"].dt.to_timestamp()

monthly_profit["profit_ma_3"] = (
    monthly_profit["profit"]
    .rolling(window=3, min_periods=1)
    .mean()
)

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(
    monthly_profit["date"],
    monthly_profit["profit"],
    marker="o",
    linewidth=2,
    label="Monthly Profit"
)

ax.plot(
    monthly_profit["date"],
    monthly_profit["profit_ma_3"],
    linewidth=2.5,
    label="3-Month Moving Average"
)

best_month = monthly_profit.loc[monthly_profit["profit"].idxmax()]

ax.annotate(
    f"Peak: ₹{best_month['profit']:,.0f}",
    xy=(best_month["date"], best_month["profit"]),
    xytext=(10, 10),
    textcoords="offset points"
)

ax.set_title(
    "Monthly Profit Trend",
    fontsize=16,
    fontweight="bold"
)
ax.set_xlabel("Month")
ax.set_ylabel("Total Profit (₹)")
ax.grid(True, linestyle="--", alpha=0.6)
ax.legend()

plt.tight_layout()
plt.show()

print("\nProfit Summary")
print("-" * 50)
print(f"Total Profit        : ₹{df['profit'].sum():,.2f}")
print(f"Average Monthly Profit: ₹{monthly_profit['profit'].mean():,.2f}")
print(f"Most Profitable Crop : {profit_by_crop.iloc[0]['crop']}")
print(f"Best Month Profit   : ₹{best_month['profit']:,.2f}")
