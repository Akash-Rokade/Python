import matplotlib.pyplot as plt

x=[[1,3,5],[3,10,100]]
y=[6,7,9,10,25,49]

plt.boxplot(x)
plt.title("Boxplot")
plt.xlabel("Value of X")
plt.show()
