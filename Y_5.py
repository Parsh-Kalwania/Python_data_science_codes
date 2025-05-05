import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.api as sm

df=sns.load_dataset('iris')

#Z-test

sample=df['sepal_length'].sample(30,random_state=42)
pop_mean=df['sepal_length'].mean()
pop_std=df['sepal_length'].std()
z_score=(sample.mean()-pop_mean)/(pop_std/np.sqrt(len(sample)))
p_value=stats.norm.sf(abs(z_score))*2 #two -tailed test
print(f"Z-test: Z_score = {z_score:.4f}, p-value = {p_value:.4f}")

#T-test

setosa=df[df['species']=='setosa']['sepal_length']
versicolor=df[df['species']=='versicolor']['sepal_length']
t_stat,p_value=stats.ttest_ind(setosa,versicolor)
print(f"T-test: t-statistic = {t_stat:.4f}, p-value = {p_value:.4f}")
