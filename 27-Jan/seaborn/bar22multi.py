import matplotlib.pyplot as plt
x=[1,3,5,7,9,10]
y=[6,7,9,10,25,49]
x1=[6,7,9,10,25,49]
y1=[1,3,5,7,9,10]

plt.bar([a+0.25 for a in x],y,label="Bar1",width=0.20,align='edge')
plt.bar(x1,y1,label="Bar2",width=0.25,align='edge')
plt.legend()

plt.show()
