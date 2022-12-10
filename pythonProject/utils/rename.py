import os

"""
    自定义改名工具包
    主要是作用于批量更改windows的文件名
"""


def ReName(path, number):
    fileList = os.listdir(path)
    f = 0
    for item in fileList:
        oldName = path + os.sep + fileList[f]
        newName = path + os.sep + str(number + 1 + f) + '.jpeg'
        # print(newName)
        os.rename(oldName, newName)
        print(oldName + '=========>' + newName + '\n')
        f += 1


if __name__ == '__main__':
    p = "D:\Desktop\照片"
    n = 76
    ReName(p, n)
    pass
