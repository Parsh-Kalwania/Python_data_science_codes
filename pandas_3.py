import pandas as pd
import dtale

df = pd.read_excel("tips.xls")

df_cleaned=df.dropna()
print("Data after dropping missing values:\n",df_cleaned.head(),"\n")

df_filled=df.fillna(0)
print("Data after filling missing values:\n",df_filled.head(),"\n")

grouped_data=df.groupby('day')['total_bill'].sum()
print("Total Bill by day:\n",grouped_data,"\n")

sorted_df=df.sort_values(by='total_bill',ascending=False)
print("Top 5 Total Bill records:\n",sorted_df.head(),"\n")

df['total_bill_in_hundreds']=df['total_bill'].apply(lambda x:x/100)
print("Transformed Total Bill data:\n",df[['total_bill','total_bill_in_hundreds']].head(),"\n")

#df_merged=df.merge(df2, on='Customer_ID',how='inner')
#print(df_merged.head())

#df_combined=pd.concat([df1,df2], axis=0)
#print(df_combined.head())

pivot_table = df.pivot_table(values='total_bill',index='day',columns='Gender', aggfunc='sum')
print("Pivot table:\n",pivot_table,"\n")

print("Total Bill Column:\n",df['total_bill'].head(),"\n")

filtered_df = df.loc[df['total_bill']>20]
print("FIltered Data (total bill > 20):\n",filtered_df.head(),"\n")

print("First 5 rows using iloc:\n",df.iloc[0:5],"\n")

df_renamed=df.rename(columns={'total_bill':'Total_Bill_Amount'})
print("Renamed Column Names:\n",df_renamed.columns,"\n")

