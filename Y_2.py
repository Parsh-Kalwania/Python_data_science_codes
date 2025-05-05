import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

diamonds=sns.load_dataset("diamonds")
print(diamonds.info())
data=diamonds["price"].values

#Histogram

plt.figure(figsize=(8,4))
plt.hist(data,bins=50,edgecolor='black')
plt.xlabel("diamond price")
plt.ylabel("frequency")
plt.title("Histogram of DIamond Prices")
plt.grid(axis='y',linestyle='--',alpha=0.7)
plt.show()

#Mean and Std Dev

mean=np.mean(data)
std_dev=np.std(data,ddof=0)

#Z-scores

z_scores=(data-mean)/std_dev

#Outliers

outliers=data[(z_scores>3) | (z_scores<-3)]
print(f"Mean Price: {mean:.2f}, Std Dev: {std_dev:.2f}")
print(f"Number of outliers: {len(outliers)}")
print(f"Outlier values (first 10 shown): {outliers[:10]}")
 #Box plot

plt.figure(figsize=(8,4))
plt.boxplot(data,vert=False,patch_artist=True,boxprops=dict(facecolor="lightblue",color="blue",linestyle="dashed"),
                                                            whiskerprops=dict(color="red",linestyle="dashed",linewidth=2),
                                                            capprops=dict(color="black",linestyle="dashed"),
                                                            medianprops=dict(color="red"))

plt.title("Box Plot of diamond prices with outliers")
plt.xlabel("Price")
plt.grid(axis='x',linestyle="--",alpha=0.7)

#Mark outliers

for outlier in outliers:
    plt.scatter(outlier)