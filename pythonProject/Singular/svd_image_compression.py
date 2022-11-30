import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img_eg = mpimg.imread('D:\Code-repository\PyCharm\pythonProject\Singular\lena.tiff')
print(img_eg.shape)

U, Sigma, VT = np.linalg.svd(img_eg)

# 取10个奇异值
sval_nums = 10
img_restruct1 = (U[:, 0:sval_nums]).dot(np.diag(Sigma[0:sval_nums])).dot(VT[0:sval_nums, :])
img_restruct1 = img_restruct1.reshape(512, 512)

# 取30个奇异值
sval_nums = 30
img_restruct2 = (U[:, 0:sval_nums]).dot(np.diag(Sigma[0:sval_nums])).dot(VT[0:sval_nums, :])
img_restruct2 = img_restruct2.reshape(512, 512)

# 取70个奇异值
sval_nums = 70
img_restruct3 = (U[:, 0:sval_nums]).dot(np.diag(Sigma[0:sval_nums])).dot(VT[0:sval_nums, :])
img_restruct3 = img_restruct3.reshape(512, 512)

# 取120个奇异值
sval_nums = 120
img_restruct4 = (U[:, 0:sval_nums]).dot(np.diag(Sigma[0:sval_nums])).dot(VT[0:sval_nums, :])
img_restruct4 = img_restruct4.reshape(512, 512)

# 取120个奇异值
sval_nums = 150
img_restruct5 = (U[:, 0:sval_nums]).dot(np.diag(Sigma[0:sval_nums])).dot(VT[0:sval_nums, :])
img_restruct5 = img_restruct5.reshape(512, 512)

# 图像显示
fig, ax = plt.subplots(2, 3, figsize=(24, 16))
ax[0][0].imshow(img_eg, cmap='gray')
ax[0][0].set(title='source')
ax[0][1].imshow(img_restruct1.astype(np.uint8), cmap='gray')
ax[0][1].set(title='nums of sigma = 10')
ax[0][2].imshow(img_restruct1.astype(np.uint8), cmap='gray')
ax[0][2].set(title='nums of sigma = 30')
ax[1][0].imshow(img_restruct1.astype(np.uint8), cmap='gray')
ax[1][0].set(title='nums of sigma = 70')
ax[1][1].imshow(img_restruct1.astype(np.uint8), cmap='gray')
ax[1][1].set(title='nums of sigma = 120')
ax[1][2].imshow(img_restruct1.astype(np.uint8), cmap='gray')
ax[1][2].set(title='nums of sigma = 150')
