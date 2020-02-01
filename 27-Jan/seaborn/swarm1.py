import matplotlib.pyplot as plt
import seaborn as sns

iris=sns.load_dataset("iris")
sns.swarmplot(x='species',y='sepal_length',data=iris)
plt.show()

