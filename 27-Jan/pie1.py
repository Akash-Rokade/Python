import matplotlib.pyplot as plt

x=[20,30,50]
plt.pie(x,labels=["Data1","Data2","Data3"],autopct='%1.2f%%')

plt.title("PieChart")
plt.show()
