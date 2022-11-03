"""
梯度下降法求解线性回归问题
"""
import numpy as np


def gradient(x, y, w):
    """
    计算一阶导函数的值
    :param x: 矩阵，样本集
    :param y: 矩阵, 标签
    :param w: 矩阵，线性回归模型的参数
    :return: 矩阵，一阶导数值
    """
    m, n = np.shape(x)
    g = np.mat(np.zeros((n, 1)))
    for i in range(m):
        err = y[i, 0] - x[i, ] * w
        for j in range(n):
            g[j, ] -= err * x[i, j]
    return g


def lossValue(x, y, w):
    """
    计算损失函数
    :param x: 矩阵，样本集
    :param y: 矩阵，标签
    :param w: 矩阵，线性回归模型参数
    :return: 损失函数值
    """
    k = y - x * w
    return k.T * k / 2


temperatures = [15, 20, 25, 30, 35, 40]
flowers = [136, 140, 155, 160, 157, 175]

X = (np.mat([[1, 1, 1, 1, 1, 1], temperatures])).T
Y = (np.mat(flowers)).T

W = (np.mat([0.0, 0.0])).T

print(W)

# alpha = 0.0005 步长太大，来回震荡，无法收敛
alpha = 0.00025
loss_change = 0.000001
loss = lossValue(X, Y, W)
for i in range(30000):
    W = W - alpha * gradient(X, Y, W)
    newLoss = lossValue(X, Y, W)
    # print(str(i) + ":" + str(W[0]) + ":" + str(W[1]))
    # print(newLoss)
    if abs(loss - newLoss) < loss_change:
        break
    loss = newLoss

new_tempera = [18, 22, 30]
new_tempera = (np.mat([[1, 1, 1, 1], new_tempera])).T
print('===============================')
print(new_tempera)
print(W)
# pro_num = new_tempera * W
# print(pro_num)




