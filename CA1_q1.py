import numpy as np

def day(average):
    if (average<5):
        print("Wind Intensity: Calm")
    elif(average<=15):
        print("Wind Intensity: Breezy")
    elif (average<=30):
        print("Wind Intensity: Windy")
    elif(average>30):
        print("Wind Intensity: Stormy")
    else:
        print("Invalid input")


l=[]
for i in range(7):
    l.append(int(input()))

a1=np.array(l)
average=np.sum(a1)/len(l)
print(f"Average Wind Speed: {average:.1f} mph")
day(average)
