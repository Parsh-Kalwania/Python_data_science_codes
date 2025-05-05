import numpy as np

l=[]
n=int(input("Enter number of elements: "))
for i in range(0,n):
    l.append(int(input("Enter value: ")))

a=np.array(l)
print(a[::-1])
print(a)

a=np.array([1,2,3,4,5])
print("### 1D ###")
print(a*2)

a=np.array(([1,2,3],[4,5,6],(7,8,9)))
b=np.array(([9,8,7],[6,5,4],[3,2,1]))
d=np.zeros([3,3],dtype=int)
s=0
for i in range(0,len(a)):
    for j in range(0,len(b[0])):
        for k in range(0,len(b)):
            d[i][j]=d[i][j]+(a[i][k]*b[k][j])

print("### 2D ###")
print(a)
print("------")
print(b)
print("------")
print(d)
print("------")
print(a@b)
print("------")
print(a.dot(b))
print("------")
print(a*b)