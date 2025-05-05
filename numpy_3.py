import numpy as np

a=np.array([[1,2,3],[4,5,6]])
b=np.array([[11,12,13],[14,15,16]])

print("a+b: ",a+b)
print("a-b: ",a-b)
print("a*b: ",a*b)
print("a**b: ",a**b)


a=np.arange(6).reshape(2,3)
print(a.ndim)
b=np.arange(10,22,2).reshape(3,2)
print(b.ndim)
print("b@a: ",b@a)
print("a.dot(b): ",a.dot(b))

print(a.shape)
print(a.ndim)
print(a.dtype)
print(a.dtype.name)
print(a.itemsize)
print(type(a))

print(a)
print(a[1][0])
print(a[1:4])
print(a[1:4,0:-1])
""" 
import numpy as np
a=np.arange(1,7).reshape(2,3)
b=a
print("Reference variable")
print(a)
print(b)
print(a is b)
print(b is a)
b[0][1]=99
print(a)
print(b)
print("Shallow copy")
c=a.view()
print(a)
print(c)
print(a is c)
print(c is a)
a[0][1]=22
print(a)
print(c)
print("Deep copy")
d=a.copy()
print(a)
print(d)
print(a is d)
print(d is a)
d[0][1]=256
print(a)
print(d)
 """