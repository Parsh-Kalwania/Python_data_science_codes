import matplotlib.pyplot as plt

categories = ['A','B','C','D','E']
values = [1,4,7,8,4]

plt.bar(categories,values,color="powderblue")

plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Basic Bar Chart")

plt.show()