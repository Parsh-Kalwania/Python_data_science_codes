import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=np.array([-1111,-12,-21,-1,-45,34,76,12,78,400])

# 1. IQR Method

Q1=np.percentile(data,25)
Q3=np.percentile(data,75)
IQR=Q3-Q1
lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR
outliers_iqr=data[(data<lower_bound) | (data>upper_bound)]

# 2. Z-score Method

mean=np.mean(data)
std_dev=np.std(data,ddof=1)
z_scores=(data-mean)/std_dev
outliers_z=data[np.abs(z_scores)>3]

# 3. Box Plot Visualization

plt.figure(figsize=(6,4))
plt.boxplot(data)
plt.xlabel("Values")
plt.title("Box Plot for Outlier Detection")
plt.show()

# plot Histogram

plt.figure(figsize=(8,4))
plt.hist(data,bins=10,color='skyblue',edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of data')
plt.show()

# Print Results

print(f"Dataset: {data}")
print(f"Q1: {Q1}, Q3: {Q3}, IQR: {IQR}")
print(f"Lower bound: {lower_bound}, Upper bound: {upper_bound}")
print(f"Outliers detected using IQR: {outliers_iqr}")
print(f"Mean: {mean}, Standard Deviation: {std_dev}")
print(f"Outliers detected using Z-score: {outliers_z}")

print(z_scores)