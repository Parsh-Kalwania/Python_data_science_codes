import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

categories = ['Furniture','Office Supplies','Technology']
profit=[4390.45,3450.50,12340.80]
sales=[80000,23000,90000]

sns.set_style(style='whitegrid')

# Line Chart

plt.figure(figsize=(8,5))
sns.lineplot(x=categories,y=sales)
plt.title("Sales Trend over Ctaegories")
plt.show()

# Bar Chart

plt.figure(figsize=(8,5))
barplot=sns.barplot(x=categories,y=sales,errorbar=None)
plt.title("Average Profit by Category")

for i,value in enumerate(profit):
    barplot.text(i,value+100,f'{value: .2f}', ha='center')
plt.show()

# Pie Chart

plt.figure(figsize=(8,5))
sns.scatterplot(x=sales,y=profit)
plt.title("Sales vs Profit")
plt.show()

# HeatMap

data=pd.DataFrame({'Sales':sales,'Profit':profit})
plt.figure(figsize=(6,4))
corr= data.corr()
sns.heatmap(corr,annot=True,cmap='coolwarm',fmt='.2f',linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()