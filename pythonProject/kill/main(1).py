#
# 恢复文件部分
#
import os
import time

sum: int = 0

def renaming(file):
    """修改后缀"""

    ext = os.path.splitext(file)  # 将文件名路径与后缀名分开

    if ext[1] == '.WNCRY':  # 文件名：ext[0]
        new_name = ext[0] + ''  # 文件后缀：ext[1]
        os.rename(file, new_name)  # tree()已切换工作地址，直接替换后缀
        global sum
        sum = sum + 1


def tree(path):
    """递归函数"""
    files = os.listdir(path)  # 获取当前目录的所有文件及文件夹
    for file in files:
        file_path = os.path.join(path, file)  # 获取该文件的绝对路径
        if os.path.isdir(file_path):  # 判断是否为文件夹
            tree(file_path)  # 开始递归
        else:
            os.chdir(path)  # 修改工作地址（相当于文件指针到指定文件目录地址）
            renaming(file)  # 修改后缀


this_path = os.getcwd()  # 获取当前工作文件的绝对路径（文件夹)
tree(this_path)
print("成功共恢复" + str(sum) + "处文件")


#
# 恢复壁纸部分
#
import os
import random

import win32api


def setWallpaper(path):
    files = os.listdir(path)
    file = random.choice(files)
    file_path = os.path.join(path, file)
    # 打开注册表
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)

    # 2：拉伸  0：居中  6：适应  10：填充
    win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "2")

    #
    # win32api.RegSetValueEx(reg_key,"Wallpaper")

    # SPIF_SENDWININICHANGE:立即生效
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, file_path, win32con.SPIF_SENDWININICHANGE)


setWallpaper(r"C:\Windows\Web\Wallpaper\Landscapes")
print("成功恢复壁纸")



#
# 杀死进程部分
#
import win32gui
from win32.lib import win32con

hwnd_title = dict()

def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})

win32gui.EnumWindows(get_all_hwnd, 0)

for h, t in hwnd_title.items():
    if t is not "":
        print(h, t)

def handle_window(hwnd, extra):
    if win32gui.IsWindowVisible(hwnd):

        if 'Wana Decrypt0r 2.0' in win32gui.GetWindowText(hwnd):
            win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
            print("成功杀死进程")


win32gui.EnumWindows(handle_window, None)

# win32gui.EnumWindows(枚举函数名称, None) 语句是进行句柄ID枚举
# win32gui.GetWindowText(句柄ID) 语句是通过句柄ID来获取进程名称
# win32gui.IsWindowVisible(句柄ID) 语句是查询此句柄ID是否存在，存在返回1 否则返回0
# win32gui.PostMessage(句柄ID, win32con.WM_CLOSE, 0, 0) 语句是通过指定句柄ID来杀死进程


print("窗口将在十秒后自动关闭")
time.sleep(10)
