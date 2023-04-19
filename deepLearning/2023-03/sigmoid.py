import numpy as np
import matplotlib.pylab as plt
"""
阶跃函数
h(x) = 1 / (1 + exp(-x))
exp(-x) 相当于 e ** (-x)
"""


def step_function(x):
    """
    简单阶跃函数
    :param x:
    :return:
    """
    if x > 0:
        return 1
    else:
        return 0


def step_function(x):
    y = x > 0
    return y.astype(np.int)


def step_function(x):
    return np.array(x > 0, dtype=np.int)


if __name__ == "__main__":
    pass
