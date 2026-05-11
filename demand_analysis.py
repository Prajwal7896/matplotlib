import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("farmers_market_master.csv")

crop_demand = (
    df.groupby("crop", as_index=False)["quantity_sold_kg"]
      .sum()
      .sort_values("quantity_sold_kg", ascending=False)
)

top_n = 10
crop_demand = crop_demand.head(top_n)

total_demand = crop_demand["quantity_sold_kg"].sum()
crop_demand["share_pct"] = (
    crop_demand["quantity_sold_kg"] / total_demand * 100
)

fig, ax = plt.subplots(figsize=(12, 7))

bars = ax.barh(
    crop_demand["crop"],
    crop_demand["quantity_sold_kg"]
)

ax.invert_yaxis()

for bar, share in zip(bars, crop_demand["share_pct"]):
    width = bar.get_width()
    ax.text(
        width,
        bar.get_y() + bar.get_height() / 2,
        f" {width:,.0f} kg ({share:.1f}%)",
        va="center"
    )

ax.set_title(
    "Top 10 Crops by Total Demand",
    fontsize=16,
    fontweight="bold"
)
ax.set_xlabel("Quantity Sold (kg)")
ax.set_ylabel("Crop")
ax.grid(axis="x", linestyle="--", alpha=0.6)

plt.tight_layout()
plt.show()

print("\nCrop Demand Summary")
print("-" * 50)
print(crop_demand.to_string(index=False))
