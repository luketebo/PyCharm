# 三次多项式拟合示例（多项式回归与欠拟合，过拟合）
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np


def myFun(x):
    return 10 + 5 * x + 4 * x ** 2 + 6 * x ** 3


x = (np.linspace(-3, 3, 7)).reshape(-1, 1)
y = myFun(x) + np.random.random(size=len(x)) * 100 - 50

x_p = (np.linspace(-2.5, 2.5, 6)).reshape(-1, 1)

x1 = np.linspace(-3, 3, 100)
y0 = myFun(x1)

featurizer_3 = PolynomialFeatures(degree=3)

x_3 = featurizer_3.fit_transform(x)
x_p_3 = featurizer_3.transform(x_p)


model_3 = LinearRegression()
model_3.fit(x_3, y)

print('--三次多项式模型--')
print('训练集团预测值与样本的误差均方值:' + str(np.mean((model_3.predict(x_3) - y) ** 2)))
print("测试集团预测值与目标函数值的误差均方值：" + str(np.mean((model_3.predict(x_p_3) - myFun(x_p)) ** 2)))
print('系数:' + str(model_3.coef_))

plt.title(u'三次多项式模型预测')
plt.scatter(x, y, color='green', linewidth=2)
plt.plot(x1, y0, color='red', linewidth=1)

y3 = model_3.predict(featurizer_3.fit_transform(x1))
plt.plot(x1, y3, 'b------', linewidth=1)
plt.show()