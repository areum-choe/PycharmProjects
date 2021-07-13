import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

iris = sns.load_dataset("iris")
print(iris)

iris.head()

sns.barplot(x='sepal_length',y='petal_length',data=iris)
plt.show()

sns.jointplot(x="sepal_length", y="sepal_width", data=iris)
plt.suptitle("꽃받침의 길이와 넓이의 joinplot")
plt.show()