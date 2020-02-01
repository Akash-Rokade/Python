import matplotlib.pyplot as plt
import seaborn as sns

iris=sns.load_dataset("iris")
sns.barplot(x='sepal_width',y='sepal_length',data=iris)
plt.show()

