import numpy as np

cust=int(input("No. of customers: "))
mon=int(input("No. of months: "))

a=np.random.randint(10,50,(cust,mon))
print(a,"\n")

for i in range(0,cust):
    print(f"Customer{i+1}: ")
    print("Maximum: ",np.max(a[i]))
    print("Minimum: ",np.min(a[i]))
    print("Total: ",sum(a[i]))
    print()

print("Maximum across all: ",np.max(a))
print("Minimum across all: ",np.min(a))
print("Total across all: ",np.sum(a))
b=a.flatten()
b.sort()
print("Sorted flattened array: ",b)

print("Reshaped structure: ",a.reshape(mon,cust))