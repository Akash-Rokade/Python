import matplotlib.pyplot as plt
x=[1,3,5,7,9,10]
y=[6,7,9,10,25,49]
x1=[6,7,9,10,25,49]
y1=[1,3,5,7,9,10]

plt.plot(x,y,label='Line1')
plt.plot(x1,y1,label='Line2')
plt.legend()
plt.xticks([1,5,9],['a','b','c'])
plt.yticks([2,4,6,8,10])
plt.title("Lineplot")
plt.show()
