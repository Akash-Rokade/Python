import matplotlib.pyplot as plt
import seaborn as sns

iris=sns.load_dataset("iris")
sns.pairplot(data=iris)
plt.show()

