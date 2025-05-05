import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,30,40,50]

plt.plot(x,y,marker='p',color='pink',label='Line1')

'''marker:
o - circle
s - square 
D - diamond
x - cross
h - hexagon
* - star
^ - triangle
+ - plus sign
. - small dot
v - triangle down
p - pentagon'''

plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.title("Basic Line Plot")

plt.legend()

plt.show()