import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class KillTool(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super(KillTool, self).__init__(*args, **kwargs)
        self.pack(fill=BOTH, expand=YES)


if __name__ == "__main__":
    app = ttk.Window(title="Kill Tools", size=[1200, 800], resizable=[False, False])
    killTool = KillTool(app)
    app.mainloop()


