# 调用Sklearn 中的kmeans
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris


if __name__ == "__main__":
    iris = load_iris()
    print(iris)
    # # 读取数据
    # data = np.genfromtxt(iris, delimiter=" ")
    # # 簇类数量
    # k = 4
    # # 训练模型
    # model = KMeans(n_clusters=k)
    # # 模型训练
    # model.fit(data)
    # # 分类中心点坐标
    # centers = model.cluster_centers_
    # # 预测结果
    # result = model.predict(data)

