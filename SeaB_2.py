#Write a python code implementing EDA on "IRIS" dataset using hist, scatter, bar, boxmap and heatmap

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=sns.load_dataset('iris')

#Scatter plot

plt.figure(figsize=(8,5))
sns.scatterplot(data=data, x ='petal_width', y='sepal_width', hue='species',style='species',s=100)
plt.title('petal vs sepal')
plt.show()

#Barplot

plt.figure(figsize=(8,5))
barplot=sns.barplot(data=data, x='petal_width',y='sepal_width',errorbar=None)
plt.title("Petal vs Sepal")
plt.show()

#Heatmap

plt.figure(figsize=(6,4))
corr= data.corr(numeric_only=True)
sns.heatmap(corr,annot=True,cmap='coolwarm',fmt='.2f',linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()

#Histogram
#1
plt.figure(figsize=(8,5))
data.hist(bins=15,edgecolor='blue')
plt.suptitle("petal vs sepal")
plt.show()

#2

plt.figure(figsize=(8,5))
plt.hist(data=data,x='sepal_length',bins=15)
plt.show()

#Box Plot 

plt.figure(figsize=(8,5))
sns.boxplot(data=data, orient="v" , palette='Set3')
plt.title("petal vs sepal")
plt.show()
