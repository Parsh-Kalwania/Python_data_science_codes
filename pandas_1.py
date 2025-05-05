import pandas as pd 
import numpy as np

l=[12,25,56,88]
df = pd.DataFrame(l,columns=['Roll No'])
print(df)

data=np.array([90,75,50,66])
s=pd.Series(data)
print(s)

data=np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print(s)

data={'a':0.,'b':1.,'c':2.}
s=pd.Series(data)
print(s)

data= {'Ahmed':92,'Ali':55,'Omar':83}
s=pd.Series(data,index=['Ali','Ahmed','Omar'])
print(s)

data={'a':0.0,'b':1.0,'c':2.0}
s = pd.Series(data,index = ['b','c','d','a'])
print(s)

s=pd.Series(5,index=[0,1,2,3])
print(s)

list=['m','i','n','d']
list1=[1,2,3,4]
ser=pd.Series(list)
print(ser)
ser1=pd.Series(list1)
print(ser1)

s=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
l=['c','e']
print("see here\n",s['a'])

a=pd.Series([1,2,3])
print(a)
b=pd.DataFrame()
print(b)
b=pd.DataFrame([1,2,3])
print(b)
b=pd.DataFrame([1,2,3],columns=["RollNo"],index=['A','B','C'])
print(b)

s=b.loc['A'] #passing index we are giving
print(s)
s=b.iloc[1] #passing index
print(s)

e=pd.DataFrame([[1,'a'],[2,'b']],columns=['Roll No', 'Name'],index=['A','B'])
print(e)