import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.api as sm

df = pd.read_excel("Dataset\\SALES.xlsx")

sample=df['Sales_Cost'].sample(30,random_state=42)
pop_mean=df['Sales_Cost'].mean()
pop_std=df['Sales_Cost'].std()
z_score=(sample.mean()-pop_mean)/(pop_std/np.sqrt(len(sample)))
p_value=stats.norm.sf(abs(z_score))*2 #two -tailed test
print(f"Z-test: Z_score = {z_score:.4f}, p-value = {p_value:.4f}")

#T-test

laptop=df[df['ItemName']=='Laptop']['Sales_Amt']
dvd=df[df['ItemName']=='DVD']['Sales_Amt']
t_stat,p_value=stats.ttest_ind(laptop,dvd)
print(f"T-test: t-statistic = {t_stat:.4f}, p-value = {p_value:.4f}")
