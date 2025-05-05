import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,15,20,25,40]

plt.plot(x,y,marker='*',linestyle='-',color='red',label='Line 1')

plt.scatter(x,y,color='blue',marker='o',s=100)

plt.xlabel("X-label")
plt.ylabel("Y-label")
plt.title("Scatter Plot Diagram")

plt.show()