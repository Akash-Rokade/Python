import matplotlib.pyplot as plt

x=[1,3,5,3,10,10]
y=[6,7,9,10,25,49]
plt.subplot(221)#2 row 2 column and 1st position
plt.bar(x,y)
plt.title("Bar plot")
plt.subplot(222)#2 rows 2 columns and 2nd position
plt.scatter(x,y)
plt.title("Scatter plot")

plt.subplot(223)#2 rows 2 columns and 3rd position
plt.pie(x)
plt.title("piechart plot")

plt.subplot(224)#2 rows 2 columns and 4th position
plt.boxplot(x)
plt.title("box plot")
plt.show()

