import numpy as np
from scipy import stats

data=[12.1,13.4,13.8,14.0,13.9,13.3,12.9,13.7,13.5,14.1]
statistic , p_value=stats.shapiro(data)
print("Shapiro-Wilk Test Statistic: ",statistic)
print("p-value: ",p_value)

#Interpretation

alpha=0.05
if p_value<alpha:
    print("The data looks Gausian (normal distribution) - fail to reject H0")
else:
    print("THe data does NOT look Gaussian - reject H0")