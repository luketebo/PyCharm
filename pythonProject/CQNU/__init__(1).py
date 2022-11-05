# 做个GUI
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class CqnuTool:
    def __init__(self):
        self.root = ttk.Window(title="CNU Tools",  size=[1200, 800])
        self.frameTop = ttk.Frame(self.root, relief="groove")
        self.frameCenter = ttk.Frame(self.root, relief="groove")
        self.frameBottom = ttk.Frame(self.root, relief="groove")

        self.b1 = ttk.Button(self.frameTop, text="DreamRoom", bootstyle=SUCCESS)
        self.b2 = ttk.Button(self.frameTop, text="Space", bootstyle=SUCCESS)
        self.b3 = ttk.Button(self.frameTop, text="Space", bootstyle=SUCCESS)

        self.rootLabel_1 = ttk.Label(self.frameCenter, text="Welcome to this Tools ")

        # self.loginRoot = ttk.Window(title="Login", themename="litera", size=[500, 400])
        # #   一层面板
        # self.loginFrame_1 = ttk.Frame(self.loginRoot)
        # self.loginFrame_2 = ttk.Frame(self.loginRoot)
        #
        # # 二层面板
        # self.loginFrame_1_1 = ttk.Frame(self.loginFrame_1)
        # self.loginFrame_1_2 = ttk.Frame(self.loginFrame_1)
        # self.loginFrame_1_3 = ttk.Frame(self.loginFrame_1)
        #
        # self.loginLabel_1 = ttk.Label(self.loginFrame_1_1, text="学号: ")
        # self.loginLabel_2 = ttk.Label(self.loginFrame_1_1, text="密码: ")
        # self.loginInput_1 = ttk.Entry(self.loginFrame_1_1)
        # self.loginInput_2 = ttk.Entry(self.loginFrame_1_1)
        #
        # self.loginCode_1 = ttk.Label(self.loginFrame_1_1, text="验证码")
        # self.loginCode_2 = ttk.Label(self.loginFrame_1_1, text="图片")
        #
        # self.loginButton_1 = ttk.Button(self.loginFrame_1_2, text="Login")
        # self.loginButton_2 = ttk.Button(self.loginFrame_1_2, text="Register")
        #
        # self.loginText_1 = ttk.Text(self.loginFrame_1_3, )
        #
        # self.loginCheck_1 = ttk.Checkbutton(self.loginFrame_2, text="记住密码")
        # self.loginCheck_2 = ttk.Checkbutton(self.loginFrame_2, text="自动登录")
        # self.loginCheck_3 = ttk.Checkbutton(self.loginFrame_2, text="占位")
        # self.loginCheck_4 = ttk.Checkbutton(self.loginFrame_2, text="占位")

    def __index__(self):
        """
        主页
        :return:
        """
        self.frameTop.pack(side=TOP, fill='x')
        self.frameCenter.pack()
        self.frameBottom.pack(side=BOTTOM)
        self.b1.grid(row=0, column=0)
        self.b2.grid(row=0, column=1)
        self.b3.grid(row=0, column=2)
        self.rootLabel_1.pack()
        self.root.mainloop()

        pass

    # def Login(self):
    #     """
    #     登录窗口
    #     :return:
    #     """
    #     self.loginLabel_1.grid(row=0, column=0, pady=5)
    #     self.loginLabel_2.grid(row=1, column=0, pady=5)
    #     self.loginInput_1.grid(row=0, column=1, pady=5)
    #     self.loginInput_2.grid(row=1, column=1, pady=5)
    #     self.loginCode_1.grid(row=2, column=0, pady=15)
    #     self.loginCode_2.grid(row=2, column=1, pady=15)
    #
    #     self.loginButton_1.grid(row=0, column=0, padx=45, pady=5)
    #     self.loginButton_2.grid(row=0, column=1, padx=45, pady=5)
    #
    #     self.loginText_1.pack()
    #
    #     self.loginCheck_1.grid(row=0, column=0, padx=45, pady=5)
    #     self.loginCheck_2.grid(row=1, column=0, padx=45, pady=5)
    #     self.loginCheck_3.grid(row=0, column=1, padx=45, pady=5)
    #     self.loginCheck_4.grid(row=1, column=1, padx=45, pady=5)
    #
    #     # 面板放置
    #     self.loginFrame_1.pack(pady=55)
    #     self.loginFrame_2.pack()
    #
    #     self.loginFrame_1_1.pack()
    #     self.loginFrame_1_2.pack()
    #
    #     # self.loginRoot.mainloop()
    #     pass


if __name__ == "__main__":
    cqnu = CqnuTool()
    cqnu.__index__()

    pass
