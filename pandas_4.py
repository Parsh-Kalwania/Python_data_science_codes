import pandas as pd
import numpy as np

data = {
    'ID': [1,2,3,4,5],
    'Name':['Alice','Bob',np.nan,'David','Eve'],
    'Age':[25,np.nan,30,np.nan,40],
    'City':['New York','Losl Angeles','Chicago',np.nan,'Houston'],
    'Salary':[50000,60000,np.nan,80000,90000]
}

df=pd.DataFrame(data)
print("Original DataFrame with Missing Values:")
print(df)

print('\nMissing values in each column:')
print(df.isnull().sum())

df_dropped_rows=df.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df_dropped_rows)

df_dropped_cols=df.dropna(axis=1)
print("\nDataFrame after dropping columns with missing values:")
print(df_dropped_cols)

df_filled=df.fillna({'Age':df['Age'].mean(), 'City':'Unknown','Salary':df['Salary'].median()})
print("\nDataFrame after filling missing values:")
print(df_filled)

df_ffill=df.ffill()
print("\nDataFrame after forward filling:")
print(df_ffill)

df_bfill=df.bfill()
print("\nDataFrame after backward filling:")
print(df_bfill)

df_numeric=df.select_dtypes(include=[np.number])
df_interpolated=df_numeric.interpolate()

df_final=df.copy()
df_final[df_numeric.columns]=df_interpolated
print('\nDataFrame after interpolation:')
print(df_final)

cleaned_file_path="D:\VSCode\Dataset\ABC.csv"
df.to_csv(cleaned_file_path,index=False)
print(f"Cleaned data saved to : {cleaned_file_path}")

