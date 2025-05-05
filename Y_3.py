import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_excel("Dataset\\SALES.xlsx")

price_data = data['Sales_Amt'] 

# Histogram
plt.figure(figsize=(8, 4))
plt.hist(price_data, bins=50, edgecolor='black')
plt.xlabel("Diamond Price")
plt.ylabel("Frequency")
plt.title("Histogram of Diamond Prices")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Mean and Std Dev
mean = np.mean(price_data)
std_dev = np.std(price_data, ddof=0)

# Z-scores
z_scores = (price_data - mean) / std_dev

# Outliers
outliers = price_data[(z_scores > 3) | (z_scores < -3)]

print(f"Mean Price: {mean:.2f}, Std Dev: {std_dev:.2f}")
print(f"Number of outliers: {len(outliers)}")
print(f"Outlier values (first 10 shown):\n{outliers.head(10)}")

# Box plot
plt.figure(figsize=(8, 4))
plt.boxplot(price_data, vert=False, patch_artist=True,
            boxprops=dict(facecolor="lightblue", color="blue", linestyle="dashed"),
            whiskerprops=dict(color="red", linestyle="dashed", linewidth=2),
            capprops=dict(color="black", linestyle="dashed"),
            medianprops=dict(color="red"))

plt.title("Box Plot of Diamond Prices with Outliers")
plt.xlabel("Price")
plt.grid(axis='x', linestyle="--", alpha=0.7)
plt.show()
