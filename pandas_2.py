import pandas as pd
import dtale

df = pd.read_excel("tips.xls")
#df=pd.read_excel('Book8.xlsx')
#df=pd.read_csv('tips.csv')

print("Data loaded successfully!!\n")

print("First 10 rows:\n",df.head(10),"\n")

print("Last 5 rows:\n",df.tail(),"\n")

print("DataFrame info:\n")
df.info()

print("Descriptive statistics:\n",df.describe(),"\n")

print("Shape of DataFrame:",df.shape,"\n")

print("Column names:\n",df.columns,"\n")

print("missing values:\n",df.isnull().sum(),"\n")

print("Print in string:\n",df.to_string)

d = dtale.show(df, host='localhost' , subprocess= False)
print(d.main_url())