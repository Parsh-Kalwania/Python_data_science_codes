import numpy as np
import pandas as pd

num=int(input("Number of students: "))

l=[]
for i in range(num*3):
    l.append(input())

arr1=np.array(l, dtype='float').reshape(num,3)
print("Q1",arr1)

print("Q2",arr1.sum(axis=1))

l1=[]
for i in range (num):
    for j in range(3):
            if(arr1[i][j]<75):
                 l1.append(arr1[num-1])
                 break

arr2=np.array(l1)
print("Q3: ",arr2)

tot_sum = arr1.sum(axis=0)
avg=tot_sum.max()
print("Q4 - Maximum average of a subject: ",tot_sum.max()/num)
index1= list(tot_sum).index(max(tot_sum))
print("Index of that: ",index1)