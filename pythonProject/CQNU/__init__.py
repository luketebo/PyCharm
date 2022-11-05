import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class Login(ttk.Toplevel):
    """
    Login 弹窗
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Login")

        loginRoot = ttk.Frame(self)
        loginRoot.pack()

        frame = ttk.Frame(loginRoot)
        frame.pack()

        loginLabel_1 = ttk.Label(frame, text="学号： ")
        loginLabel_1.grid(row=0, column=0)
        loginLabel_2 = ttk.Label(frame, text="密码： ")
        loginLabel_2.grid(row=1, column=0)
        loginInput_1 = ttk.Entry(frame)
        loginInput_1.grid(row=0, column=1)
        loginInput_2 = ttk.Entry(frame)
        loginInput_2.grid(row=1, column=1)

        frame = ttk.Frame(loginRoot)
        frame.pack()

        label = ttk.Label(frame, text="验证码")
        label.grid(row=0, column=0)

        label = ttk.Label(frame, text="图片")
        label.grid(row=0, column=1)

        pass


class CqnuTool(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(fill=BOTH, expand=YES)
        # 顶部按钮栏
        buttonBar = ttk.Frame(self, style="primary.TFrame")
        buttonBar.pack(fill=X, pady=1, side=TOP)

        # DreamRoom btn
        def dreamRoom():
            login = Login()
            pass
        btn = ttk.Button(
            master=buttonBar, text="DreamRoom",
            compound=LEFT,
            command=dreamRoom()
        )
        btn.pack(side=LEFT, ipadx=5, ipady=5, padx=(1, 0), pady=1)

        # Sports btn
        def sportBook():
            pass
        btn = ttk.Button(
            master=buttonBar, text="SportBook",
            compound=LEFT,
            command=sportBook()
        )
        btn.pack(side=LEFT, ipadx=5, ipady=5, padx=(1, 0), pady=1)

        pass

    def main(self):
        pass


if __name__ == "__main__":
    app = ttk.Window(title="CNU Tools", size=[1200, 800])
    cqnu = CqnuTool(app)
    app.mainloop()
