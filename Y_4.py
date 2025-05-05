import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import zscore

df=sns.load_dataset('iris')
column = 'sepal_width'
data=df[column]
Q1 = np.percentile(data,25)
Q3 = np.percentile(data,75)
IQR = Q3 - Q1
lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR

#IQR

iqr=data[(data<lower_bound)|(data>upper_bound)]

#Z_score

z_s=np.abs(zscore(data))
z_out=data[z_s>3]
print(f"IQR outliers:\n{iqr}\n")
print(f"Z_score Outliers:\n{z_out}\n")

#BOX plot

plt.figure(figsize=(8,5))
sns.boxplot(x=data)
plt.title(f"Box Plot of {column} with IQR outliers")
plt.xlabel(column)
plt.show()