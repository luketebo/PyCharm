import os

"""
    自定义改名工具包
    主要是作用于批量更改windows的文件名
"""


# path = input('文件路劲：')
# path = 'D:\Desktop\截图'

# fileList = os.listdir(path)

# n = 0


# for i in fileList:
#     oldName = path + os.sep + fileList[n]
#
#     newName = path + os.sep + str(n+1) + '.png'
#     print(oldName + '==========>' + newName)
#     # os.rename(oldName, newName)
#
#     n += 1

def ReName(path, number):
    fileList = os.listdir(path)
    f = 0
    for item in fileList:
        oldName = path + os.sep + fileList[f]
        newName = path + os.sep + str(number + 1 + f) + '.png'
        # print(newName)
        os.rename(oldName, newName)
        f += 1


if __name__ == '__main__':
    p = 'D:\Desktop\截图'
    n = 30
    ReName(p, n)
    pass
