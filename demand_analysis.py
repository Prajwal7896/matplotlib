import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../data/farmers_market_master.csv")

demand = data.groupby('crop')['quantity_sold_kg'].sum()

demand.plot(kind='bar')
plt.title("Crop Demand Analysis")
plt.xlabel("Crop")
plt.ylabel("Total Quantity Sold (kg)")

plt.show()
