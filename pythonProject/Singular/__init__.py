import numpy as np
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
print("原始样本数据", X)

U, s, V = np.linalg.svd(X)
print("左奇异向量", U)
print("奇异值序列s", s)
print("右奇异向量", V)

U_c = U[:, 0:2]
s_c = np.diag(s[0:2])
V_c = V[0:2, :]

print('压缩后的左奇异值向量', U_c)
print('压缩后的奇异值矩阵', s_c)
print('压缩后的右奇异值向量', V_c)

X_c = np.dot(X, V_c.T)
print('压缩后的样本数据', X_c)

A1 = np.dot(U_c, s_c)
A2 = np.dot(A1, V_c)
print('重建数据', A2)