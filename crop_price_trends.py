import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, AutoDateLocator

df = pd.read_csv("farmers_market_master.csv", parse_dates=["date"])

tomato = (
    df.loc[df["crop"].str.strip().str.lower() == "tomato", ["date", "price_per_kg"]]
      .dropna()
      .sort_values("date")
      .groupby("date", as_index=False)["price_per_kg"]
      .mean()
)

rolling_window = 7
tomato["price_ma_7d"] = (
    tomato["price_per_kg"]
    .rolling(window=rolling_window, min_periods=1)
    .mean()
)

summary = {
    "records": len(tomato),
    "start_date": tomato["date"].min().date(),
    "end_date": tomato["date"].max().date(),
    "avg_price": tomato["price_per_kg"].mean(),
    "min_price": tomato["price_per_kg"].min(),
    "max_price": tomato["price_per_kg"].max(),
    "volatility_pct": tomato["price_per_kg"].pct_change().std() * 100,
}

print("Tomato Price Summary")
print("-" * 40)
for key, value in summary.items():
    if isinstance(value, float):
        print(f"{key:15}: {value:.2f}")
    else:
        print(f"{key:15}: {value}")

fig, ax = plt.subplots(figsize=(14, 7))

ax.plot(
    tomato["date"],
    tomato["price_per_kg"],
    label="Daily Price",
    linewidth=1.8,
    marker="o",
    markersize=4,
    alpha=0.75,
)

ax.plot(
    tomato["date"],
    tomato["price_ma_7d"],
    label="7-Day Moving Average",
    linewidth=2.5,
)

peak_idx = tomato["price_per_kg"].idxmax()
low_idx = tomato["price_per_kg"].idxmin()

ax.scatter(
    tomato.loc[peak_idx, "date"],
    tomato.loc[peak_idx, "price_per_kg"],
    s=100,
    zorder=5,
    label="Peak Price",
)

ax.scatter(
    tomato.loc[low_idx, "date"],
    tomato.loc[low_idx, "price_per_kg"],
    s=100,
    zorder=5,
    label="Lowest Price",
)

ax.annotate(
    f"Peak: ₹{tomato.loc[peak_idx, 'price_per_kg']:.2f}",
    xy=(
        tomato.loc[peak_idx, "date"],
        tomato.loc[peak_idx, "price_per_kg"],
    ),
    xytext=(10, 10),
    textcoords="offset points",
)

ax.annotate(
    f"Low: ₹{tomato.loc[low_idx, 'price_per_kg']:.2f}",
    xy=(
        tomato.loc[low_idx, "date"],
        tomato.loc[low_idx, "price_per_kg"],
    ),
    xytext=(10, -15),
    textcoords="offset points",
)

ax.set_title("Tomato Price Trend Analysis", fontsize=18, fontweight="bold")
ax.set_xlabel("Date", fontsize=12)
ax.set_ylabel("Price per Kg (₹)", fontsize=12)

ax.xaxis.set_major_locator(AutoDateLocator())
ax.xaxis.set_major_formatter(DateFormatter("%d-%b-%Y"))

ax.grid(True, linestyle="--", alpha=0.6)
ax.legend()
fig.autofmt_xdate()
plt.tight_layout()
plt.show()
