import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_excel("D:\\Download\\A2041175501_27_2025_sales dataset.xlsx")

print(data.info())
print(data.cov(numeric_only=True)["Sales_Amt"]["Sales_Qty"])
print(data.corr(numeric_only=True)["Sales_Amt"]["Sales_Qty"])

plt.figure(figsize=(6,4))
corr= data.corr(numeric_only=True)
sns.heatmap(corr,annot=True,cmap='coolwarm',fmt='.2f',linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(data=data, x ='Sales_Amt', y='Sales_Qty',s=100)
plt.title('Amt vs Qty')
plt.show()

plt.figure(figsize=(8,5))
plt.hist(data=data,x='Sales_Amt',bins=15)
plt.show()