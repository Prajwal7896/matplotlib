import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../data/farmers_market_master.csv")
data['date'] = pd.to_datetime(data['date'])

data['profit'] = (data['price_per_kg'] - data['cost_per_kg']) * data['quantity_sold_kg']

profit_by_crop = data.groupby('crop')['profit'].sum()
profit_by_crop.plot(kind='bar')
plt.title("Profit Comparison by Crop")
plt.xlabel("Crop")
plt.ylabel("Total Profit")
plt.show()

monthly_profit = data.groupby(data['date'].dt.month)['profit'].sum()
monthly_profit.plot(marker='o')
plt.title("Monthly Profit Trend")
plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.show()
