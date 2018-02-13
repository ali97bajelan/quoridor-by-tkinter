from tkinter import *
from tkinter import Button
import tkinter.messagebox
import requests
import winsound
import address
import json


def start_gui(session):
    """Starting point when module is the main routine."""
    global val, w, root
    root = Tk()
    # root.wm_attributes("-transparentcolor", "white")
    top = New_Toplevel_1(root, session)
    # _support.init(root, top)
    root.mainloop()


w = None


def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = New_Toplevel_1(w)
    # _support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None


class New_Toplevel_1:
    def __init__(self, top=None, session=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#d9d9d9'  # X11 color: 'gray85'

        top.geometry("1000x700+200+50")
        top.title("New Toplevel 1")
        top.configure(background="gray")

        def show(e):
            print("hi")

        def color(e):  # des, button):
            print(e.x_root)
            e.widget.configure(bg="red")
            self.Button[0][6].configure(bg="blue")
            a = str(e.widget)
            print(a[2:])

        def music():
            winsound.PlaySound('Vay-Behalash.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)

        # button.configure(background="white")
        # des.configure(background="red")

        self.Button = [[0 for i in range(9)] for j in range(9)]

        i = 0
        j = 0
        x = 0.10
        y = 0.03
        while i < 9:
            while j < 9:
                self.Button[i][j] = Button(top)
                self.Button[i][j].place(relx=x, rely=y, height=50, width=50)
                self.Button[i][j].configure(background="#d9d9d9")
                j += 1
                x += 0.08
            j = 0
            x = 0.10
            y += 0.11
            i += 1

        self.Button[0][4].bind("<Button-1>", show)

        self.Button[0][5].bind("<Button-1>", color)

        self.Button[8][4].bind("<Button-1>", lambda event: self.move(session))

        print(self.Button)

        self.Button101 = Button(top)
        self.Button101.place(relx=0.10, rely=0.11, height=15, width=50)

        self.Button102 = Button(top)
        self.Button102.place(relx=0.18, rely=0.11, height=15, width=50)

        self.Button103 = Button(top)
        self.Button103.place(relx=0.26, rely=0.11, height=15, width=50)

        self.Button104 = Button(top)
        self.Button104.place(relx=0.34, rely=0.11, height=15, width=50)

        self.Button105 = Button(top)
        self.Button105.place(relx=0.42, rely=0.11, height=15, width=50)

        self.Button106 = Button(top)
        self.Button106.place(relx=0.50, rely=0.11, height=15, width=50)

        self.Button205 = Button(top)
        self.Button205.place(relx=0.48, rely=0.03, height=50, width=15)

        self.Button215 = Button(top)
        self.Button215.place(relx=0.48, rely=0.14, height=50, width=15)

        self.Button304 = Button(top)
        self.Button304.place(relx=0.48, rely=0.11, height=15, width=15)
        self.Button304.bind("<Button-1>",
                            lambda event: self.decied(self.Button105, self.Button106, self.Button205, self.Button215))

        self.Hayede = Button(top, command=music)
        self.Hayede.place(relx=0.80, rely=0.88, height=75, width=75)
        self.Hayede.configure(text="Play Hayede", background="#d9d9d9")

    def move(self, session):
        info = json.dumps(self.Button)
        t = requests.get(address.url['move'], data=info)
        print(t.content)
        # print(self.Button[8][4]['bg'],e.widget['rely'])

    def decied(self, a, b, c, d):
        answer = tkinter.messagebox.askyesnocancel('Which side ?', 'Do you want Horizontal wall?(yes)\n \tVertical(no)')
        # print(e.widget)
        print(answer)
        if str(answer) == 'True':
            a.configure(bg="black")
            b.configure(bg="black")

            print("are")
        if str(answer) == 'False':
            c.configure(bg="black")
            d.configure(bg="black")
            print("Heh")
