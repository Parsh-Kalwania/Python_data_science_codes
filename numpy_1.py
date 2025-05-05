import numpy as np

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("a: \n",a)

b=np.eye(3,3,dtype='int')
print("b: \n",b)

print("max: \n",np.max(a))
print("min: \n",np.min(a))
print("sum: \n",np.sum(a,axis=1))
print("sort: \n",np.sort(b))
print("sqrt: \n",np.sqrt(a))
print("transpose: \n",a.T)
print("product: \n",a*b)
print("cumsum column: \n",a.cumsum(axis=0))
print("cumsum row: \n",a.cumsum(axis=1))
print("flatten function: \n",a.flatten())

c=np.arange(1,10,2)
print("c: \n",c)

d=np.zeros((3,3),dtype=int)
print("d: \n",d)

e=np.full((3,3),10)
print("e: \n",e)

print("ones: \n",np.ones((3,3),dtype=int))

z=np.asmatrix('1 2 ; 3 4')
print("Via string input : \n",z)

# Create a NumPy array
arr = np.array([[1, 2], [3, 4]])

# Convert the array to a matrix
mat = np.matrix(arr)

# Demonstrate matrix multiplication behavior
print(arr * arr)  # Element-wise multiplication: [[1 4] [9 16]]
print(mat * mat)  # Matrix multiplication: [[7 10] [15 22]]

#DO ARRAY INPUT MANUALLY
#DO SUM OF ELEMENTS IN 1D, 2D, 3D ARRAY MANUALLY

l=[]
for i in range(1,11):
    l.append(int(input()))

x=np.array(l)
x.shape=(2,5)

print(x)
