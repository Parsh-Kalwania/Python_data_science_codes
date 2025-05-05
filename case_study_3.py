import numpy as np 
import pandas as pd

df = pd.read_csv("D:\\VSCode\\Dataset\\rainfall in india 1901-2015.csv")

print("Columnwise null values: ",df.isnull().sum())

print("Percentage of missing data: ",df.isnull().mean() * 100)

print("Shape before dropping: ",df.shape)
df_dropna_rows=df.dropna()
print("Shape after dropping rows: ",df_dropna_rows.shape)

df_dropna_cols=df.dropna(axis=1)
print("Shape after dropping columns: ",df_dropna_cols.shape)