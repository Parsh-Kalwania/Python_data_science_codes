import numpy as np

def grades(average):
    if average>=90 and average<=100:
        print("Letter Grade: A")
    elif average>=80 and average<90:
        print("Letter Grade: B")
    elif average>=70 and average<80:
        print("Letter Grade: C")
    elif average>=60 and average<70:
        print("Letter Grade: D")
    elif average<60:
        print("Letter Grade: F")

l=[]
size=int(input("Total no of students: "))

for i in range(0,size*5):
    l.append(int(input()))

a=np.array(l).reshape(size,5)

for i in range(0,size):
    print(f"Student {i+1}:")
    average=(np.sum(a[i])/5)
    print("Average Grade:",average)
    grades(average)
    print("\n")