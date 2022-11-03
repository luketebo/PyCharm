import numpy as np
import matplotlib.pyplot as plt
import random


def myFun(x):
    return 10 + 5 * x + 4 * x ** 2 + 6 * x ** 3


x = np.linspace(-3, 3, 7)
x_p = (np.linspace(-2.5, 2.5, 6)).reshape(-1, 1)

y = myFun(x) + np.random.random(size=len(x)) * 100 - 50

plt.rcParams['axes.unicode_minus'] = False
plt.rc('font', family='SimHei', size=13)
plt.title(u'目标函数与训练样本')
plt.scatter(x, y, color='green', linewidth=2)

x1 = np.linspace(-3, 3, 100)
y0 = myFun(x1)
plt.plot(x1, y0, color='red', linewidth=1)
plt.show()
