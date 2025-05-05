def grades(average):
    if average>=90 and average<100:
        print("Letter Grade: A")
    elif average>=80 and average<90:
        print("Letter Grade: B")
    elif average>=70 and average<80:
        print("Letter Grade: C")
    elif average>=60 and average<70:
        print("Letter Grade: D")
    elif average<60:
        print("Letter Grade: F")


list1=[int(i) for i in input().split(",")]

length=len(list1)

sum=0
average=0

for i in list1:
    sum+=i

average=sum/length

print(f"Average Grade: {average}")
grades(average)
