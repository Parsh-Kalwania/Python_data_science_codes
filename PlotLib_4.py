# %%
import matplotlib.pyplot as plt

categories = ['Apple','Banana','Orange','Cherry']
values = [30,20,10,34]

plt.pie(values,labels=categories,autopct='%1.1f%%',startangle=90)

plt.title("Fruit Distribution")

plt.legend(title="Fruits")
plt.show()