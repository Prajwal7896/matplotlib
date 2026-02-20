import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../data/farmers_market_master.csv")
data['date'] = pd.to_datetime(data['date'])

tomato = data[data['crop'] == 'Tomato']

plt.plot(tomato['date'], tomato['price_per_kg'], marker='o')
plt.title("Crop Price Trend (Tomato)")
plt.xlabel("Date")
plt.ylabel("Price per Kg")
plt.grid(True)

plt.show()
