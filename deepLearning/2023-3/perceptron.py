import numpy as np


def AND(x1, x2):
    """
    简单感知机
    AND(0,0) AND(1,0) AND(0,1) AND(1,1)
    :param x1:
    :param x2:
    :return:
    """
    w1, w2, theta = 0.5, 0.5, 0.7
    temp = x1 * w1 + x2 * w2
    if temp <= theta:
        return 0
    elif temp > theta:
        return 1


def AND_(x1, x2):
    """
    与门
    :param x1:
    :param x2:
    :return:
    """
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def NAND(x1, x2):
    """
    与非门
    :param x1:
    :param x2:
    :return:
    """
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def OR(x1, x2):
    """
    或门
    :param x1:
    :param x2:
    :return:
    """
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def XOR(x1, x2):
    """
    异或门
    XOR(0,0) 0
    XOR(1,0) 1
    XOR(0,1) 1
    XOR(1,1) 0
    XOR
    :param x1:
    :param x2:
    :return:
    """
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND_(s1, s2)
    return y


if __name__ == '__main__':
    print(XOR(0, 0))
