from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import  KMeans
import pandas as pd


iris = load_iris()
x = iris.data[:]
print(x)
print(x.shape)

data = pd.read_csv('./iris.data')
data.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']
print(data.head())

plt.scatter(x[:, 0], x[:, 1], marker='o', color='red', label = 'iris')
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.legend(loc = 2)
plt.show()

plt.scatter(x[:, 2], x[:, 3], marker='o', color="blue", label='iris')
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.legend(loc = 2)
plt.show()

# 通过sepal对三种鸢尾花进行可视化
plt.scatter(x[:50, 0], x[:50, 1], marker='o', color='red', label='setosa')
plt.scatter(x[50:100, 0], x[50:100, 1], marker='o', color='yellow', label='versicolor')
plt.scatter(x[100:, 0], x[100:, 1], marker='o', color='blue', label='virginica')
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.legend(loc=2)
plt.show()

# 通过petal对三种鸢尾花进行可视化
plt.scatter(x[:50, 2], x[:50, 3], marker='o', color='red', label='setosa')
plt.scatter(x[50:100, 2], x[50:100, 3], marker='o', color='yellow', label='versicolor')
plt.scatter(x[100:, 2], x[100:, 3], marker='o', color='blue', label='virginica')
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.legend(loc=2)
plt.show()

estimator = KMeans(n_clusters=3)
estimator.fit(x)
label_pred = estimator.labels_
x0 = x[label_pred == 0]
x1 = x[label_pred == 1]
x2 = x[label_pred == 2]
plt.scatter(x0[:, 0], x0[:, 1], c = "red", marker='o', label='setosa')
plt.scatter(x1[:, 0], x1[:, 1], c = "green", marker='*', label='versicolor')
plt.scatter(x2[:, 0], x2[:, 1], c = "blue", marker='+', label='virginica')
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.legend(loc=2)
plt.show()

## 通过petal 聚类
estimator = KMeans(n_clusters=3)
estimator.fit(x)
label_pred = estimator.labels_
x0 = x[label_pred == 0]
x1 = x[label_pred == 1]
x2 = x[label_pred == 2]
plt.scatter(x0[:, 2], x0[:, 3], c = "red", marker='o', label='setosa')
plt.scatter(x1[:, 2], x1[:, 3], c = "green", marker='*', label='versicolor')
plt.scatter(x2[:, 2], x2[:, 3], c = "blue", marker='+', label='virginica')
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.legend(loc=2)
plt.show()

sumDs = []
for i in range(1, 12):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(x)
    sumDs.append(kmeans.inertia_)
    # print(kmeans.inertia_)
plt.plot(range(1, 12), sumDs)
plt.title("the Elbow method")
plt.xlabel('k')
plt.ylabel('inertia')
plt.show()

x = iris.data[:, :2] # sepal

# 创建聚类器
estimator = KMeans(n_clusters=3)
estimator.fit(x)
label_pred = estimator.labels_
x0 = x[label_pred == 0]
x1 = x[label_pred == 1]
x2 = x[label_pred == 2]

plt.scatter(x0[:, 0], x0[:, 1], c = 'red', marker='o', label='setosa')
plt.scatter(x1[:, 0], x1[:, 1], c = 'green', marker='+', label='versicolor')
plt.scatter(x2[:, 0], x2[:, 1], c = 'blue', marker='*', label='virginica')
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.legend(loc=2)
plt.show()


x = iris.data[:, 2: ] # petal

estimator = KMeans(n_clusters=3)
estimator.fit(x)
label_pred = estimator.labels_
x0 = x[label_pred == 0]
x1 = x[label_pred == 1]
x2 = x[label_pred == 2]
plt.scatter(x0[:, 0], x0[:, 1], c = "red", marker='o', label='setosa')
plt.scatter(x1[:, 0], x1[:, 1], c = "green", marker='*', label='versicolor')
plt.scatter(x2[:, 0], x2[:, 1], c = "blue", marker='+', label='virginica')
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.legend(loc=2)
plt.show()