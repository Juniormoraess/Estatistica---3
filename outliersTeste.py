import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv('iris.csv')

plt.boxplot(iris.iloc[:, 1])
plt.show()
plt.boxplot(iris.iloc[:, 1], showfliers = False)
plt.show()

outliers = iris[(iris['Sepal width'] > 4) | (iris['Sepal width'] < 2.1)]
