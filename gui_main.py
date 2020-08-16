import tkinter as tk
from the_real_main_function import working


class Test:
    def __init__(self):
        self.arr = ''
        self.root = tk.Tk()
        self.text = tk.StringVar()
        self.moral = tk.StringVar()
        self.text.set("The path will be shown here")
        self.label = tk.Label(self.root, textvariable=self.text)

        self.button0 = tk.Button(self.root,
                                 text="Start",
                                 command=lambda: self.do_things('s'))
        self.button1 = tk.Button(self.root,
                                 text="Move",
                                 command=lambda: self.do_things(' '))
        self.button2 = tk.Button(self.root,
                                 text="Encounter",
                                 command=lambda: self.do_things('n'))
        self.button3 = tk.Button(self.root,
                                 text="Camp",
                                 command=lambda: self.do_things('c'))
        self.button4 = tk.Button(self.root,
                                 text="Camp,no enc",
                                 command=lambda: self.do_things('x'))
        self.button5 = tk.Button(self.root,
                                 text="Back to S",
                                 command=lambda: self.do_things('b'))
        self.button6 = tk.Button(self.root,
                                 text="Exit",
                                 command=lambda: self.do_things('e'))
        self.morall = tk.Entry(self.root, textvariable=self.moral)
        self.morall.pack()
        self.button0.pack()
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.button4.pack()
        self.button5.pack()
        self.button6.pack()
        self.label.pack()
        self.root.mainloop()
        # print(self.arr)
        # print(self.moral.get())
        print(working(self.arr, self.moral.get(), True))

    def do_things(self, j):
        self.arr += j
        # print(j)
        self.change_text()

    def change_text(self):
        self.text.set(str(self.arr))


app = Test()
