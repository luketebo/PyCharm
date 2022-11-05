import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class CqnuTool:
    def __init__(self):
        self.root = ttk.Window(title="CNU", size=[1200, 800])
        self.frameTop = ttk.Frame(self.root, relief="groove")

    def __index__(self):
        self.frameTop.pack()
        self.root.mainloop()


if __name__ == "__main__":
    demo = CqnuTool()
    demo.__index__()
