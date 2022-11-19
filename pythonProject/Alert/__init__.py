import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import time


class Alert(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(fill=BOTH, expand=YES)
        frame = ttk.Frame(self)
        frame.pack(
            expand=1,
            fill=BOTH
        )

        self.time = ttk.StringVar()
        self.time.set("00:00:00")

        label = ttk.Label(
            master=frame,
            textvariable=self.time,
            font=(None, 35)
        )
        label.pack(side=TOP, pady=(80, 10))

        def start():
            while True:
                times = self.time.get()
                ls = times.split(":")
                first = int(ls[0])
                second = int(ls[1])
                third = int(ls[2])
                time.sleep(1)
                third = third + 1
                if third > 60:
                    third = 0
                    second = second + 1
                    if second > 60:
                        second = 0
                        first = first + 1

                if third < 10:
                    third = "0" + str(third)
                else:
                    third = str(third)
                if second < 10:
                    second = "0" + str(second)
                else:
                    second = str(second)
                if first < 10:
                    first = "0" + str(first)
                else:
                    first = str(first)

                newTime = first + ":" + second + ":" + third
                self.time.set(newTime)
                print(self.time.get())

        Btn = ttk.Button(
            master=frame,
            text="Start",
            style="danger.TButton",
            command=start
        )
        Btn.pack(side=BOTTOM, pady=(10, 80))


if __name__ == "__main__":
    app = ttk.Window(title="Tomato Tools", size=[300, 300], resizable=[False, False])
    tomato = Alert(app)
    app.mainloop()

