"""
最小二乘法解线性回归
"""
import matplotlib.pyplot as plt
import numpy as np

temperatures = [15, 20, 25, 30, 35, 40]
flowers = [136, 140, 155, 160, 157, 175]


def least_squares(X, Y):
    """
    :param X:
    :param Y:
    :return:
    """
    W = (X * X.T).I * X * Y.T
    return W


X = np.mat([[1, 1, 1, 1, 1, 1], temperatures])
Y = np.mat(flowers)

W = least_squares(X, Y)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.scatter(temperatures, flowers, color="green", label="小花数量", linewidths=2)
plt.plot(temperatures, flowers, linewidth=1)
x1 = np.linspace(15, 40, 100)
y1 = W[1, 0] * x1 + W[0, 0]
plt.plot(x1, y1, color='red', label='拟合直线', linewidth=2, linestyle=':')
plt.legend(loc='lower right')
plt.show()
new_tempera = [18, 22, 23]
new_tempera = (np.mat(new_tempera)).T
pro_num = W[1, 0] * new_tempera + W[0, 0]
print(pro_num)
