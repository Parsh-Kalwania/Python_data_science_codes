import pandas as pd
import numpy as np

df = pd.read_csv("dataset.csv")
print("First 10 rows:")
print(df.head(10))

print("Last 5 rows:")
print(df.tail(5))

print("Dataset Info:")
print(df.info())

if not df.select_dtypes(include=[np.number]).empty:
    print("Total sum of numerical columns:")
    print(df.select_dtypes(include=[np.number]).sum())
