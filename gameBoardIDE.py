import sys
from tkinter import *
from tkinter import Button
import tkinter.messagebox
import winsound


def vp_start_gui():
    """Starting point when module is the main routine."""
    global val, w, root
    root = Tk()
    # root.wm_attributes("-transparentcolor", "white")
    top = New_Toplevel_1(root)
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
    def __init__(self, top=None):
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
            self.Button7.configure(bg="blue")
            a = str(e.widget)
            print(a[2:])

        def music():
            winsound.PlaySound('Vay-Behalash.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)

        # button.configure(background="white")
        # des.configure(background="red")

        self.Button1 = Button(top)
        self.Button1.place(relx=0.10, rely=0.03, height=50, width=50)
        self.Button1.configure(background="gray85")

        self.Button2 = Button(top)
        self.Button2.place(relx=0.18, rely=0.03, height=50, width=50)
        self.Button2.configure(background="#d9d9d9")

        self.Button3 = Button(top)
        self.Button3.place(relx=0.26, rely=0.03, height=50, width=50)
        self.Button3.configure(background="#d9d9d9")

        self.Button4 = Button(top)
        self.Button4.place(relx=0.34, rely=0.03, height=50, width=50)
        self.Button4.configure(background="#d9d9d9")

        self.Button5 = Button(top)
        self.Button5.bind("<Button-1>", show)
        self.Button5.place(relx=0.42, rely=0.03, height=50, width=50)
        self.Button5.configure(background="red")

        self.Button6 = Button(top)
        self.Button6.bind("<Button-1>", color)
        self.Button6.place(relx=0.50, rely=0.03, height=50, width=50)
        self.Button6.configure(background="#d9d9d9")

        self.Button7 = Button(top)
        self.Button7.place(relx=0.58, rely=0.03, height=50, width=50)
        self.Button7.configure(background="#d9d9d9")

        self.Button8 = Button(top)
        self.Button8.place(relx=0.66, rely=0.03, height=50, width=50)
        self.Button8.configure(background="#d9d9d9")

        self.Button9 = Button(top)
        self.Button9.place(relx=0.74, rely=0.03, height=50, width=50)
        self.Button9.configure(background="#d9d9d9")

        self.Button11 = Button(top)
        self.Button11.place(relx=0.10, rely=0.14, height=50, width=50)
        self.Button11.configure(background="#d9d9d9")

        self.Button12 = Button(top)
        self.Button12.place(relx=0.18, rely=0.14, height=50, width=50)
        self.Button12.configure(background="#d9d9d9")

        self.Button13 = Button(top)
        self.Button13.place(relx=0.26, rely=0.14, height=50, width=50)
        self.Button13.configure(background="#d9d9d9")

        self.Button14 = Button(top)
        self.Button14.place(relx=0.34, rely=0.14, height=50, width=50)
        self.Button14.configure(background="#d9d9d9")

        self.Button15 = Button(top)
        self.Button15.place(relx=0.42, rely=0.14, height=50, width=50)
        self.Button15.configure(background="#d9d9d9")

        self.Button16 = Button(top)
        self.Button16.place(relx=0.50, rely=0.14, height=50, width=50)
        self.Button16.configure(background="#d9d9d9")

        self.Button17 = Button(top)
        self.Button17.place(relx=0.58, rely=0.14, height=50, width=50)
        self.Button17.configure(background="#d9d9d9")

        self.Button18 = Button(top)
        self.Button18.place(relx=0.66, rely=0.14, height=50, width=50)
        self.Button18.configure(background="#d9d9d9")

        self.Button19 = Button(top)
        self.Button19.place(relx=0.74, rely=0.14, height=50, width=50)
        self.Button19.configure(background="#d9d9d9")

        self.Button21 = Button(top)
        self.Button21.place(relx=0.10, rely=0.25, height=50, width=50)
        self.Button21.configure(background="#d9d9d9")

        self.Button22 = Button(top)
        self.Button22.place(relx=0.18, rely=0.25, height=50, width=50)
        self.Button22.configure(background="#d9d9d9")

        self.Button23 = Button(top)
        self.Button23.place(relx=0.26, rely=0.25, height=50, width=50)
        self.Button23.configure(background="#d9d9d9")

        self.Button24 = Button(top)
        self.Button24.place(relx=0.34, rely=0.25, height=50, width=50)
        self.Button24.configure(background="#d9d9d9")

        self.Button25 = Button(top)
        self.Button25.place(relx=0.42, rely=0.25, height=50, width=50)
        self.Button25.configure(background="#d9d9d9")

        self.Button24 = Button(top)
        self.Button24.place(relx=0.50, rely=0.25, height=50, width=50)
        self.Button24.configure(background="#d9d9d9")

        self.Button25 = Button(top)
        self.Button25.place(relx=0.58, rely=0.25, height=50, width=50)
        self.Button25.configure(background="#d9d9d9")

        self.Button26 = Button(top)
        self.Button26.place(relx=0.66, rely=0.25, height=50, width=50)
        self.Button26.configure(background="#d9d9d9")

        self.Button27 = Button(top)
        self.Button27.place(relx=0.74, rely=0.25, height=50, width=50)
        self.Button27.configure(background="#d9d9d9")

        self.Button28 = Button(top)
        self.Button28.place(relx=0.10, rely=0.36, height=50, width=50)
        self.Button28.configure(background="#d9d9d9")

        self.Button29 = Button(top)
        self.Button29.place(relx=0.18, rely=0.36, height=50, width=50)
        self.Button29.configure(background="#d9d9d9")

        self.Button30 = Button(top)
        self.Button30.place(relx=0.26, rely=0.36, height=50, width=50)
        self.Button30.configure(background="#d9d9d9")

        self.Button31 = Button(top)
        self.Button31.place(relx=0.34, rely=0.36, height=50, width=50)
        self.Button31.configure(background="#d9d9d9")

        self.Button32 = Button(top)
        self.Button32.place(relx=0.42, rely=0.36, height=50, width=50)
        self.Button32.configure(background="#d9d9d9")

        self.Button33 = Button(top)
        self.Button33.place(relx=0.50, rely=0.36, height=50, width=50)
        self.Button33.configure(background="#d9d9d9")

        self.Button34 = Button(top)
        self.Button34.place(relx=0.58, rely=0.36, height=50, width=50)
        self.Button34.configure(background="#d9d9d9")

        self.Button35 = Button(top)
        self.Button35.place(relx=0.66, rely=0.36, height=50, width=50)
        self.Button35.configure(background="#d9d9d9")

        self.Button36 = Button(top)
        self.Button36.place(relx=0.74, rely=0.36, height=50, width=50)
        self.Button36.configure(background="#d9d9d9")

        self.Button37 = Button(top)
        self.Button37.place(relx=0.10, rely=0.47, height=50, width=50)
        self.Button37.configure(background="#d9d9d9")

        self.Button38 = Button(top)
        self.Button38.place(relx=0.18, rely=0.47, height=50, width=50)
        self.Button38.configure(background="#d9d9d9")

        self.Button39 = Button(top)
        self.Button39.place(relx=0.26, rely=0.47, height=50, width=50)
        self.Button39.configure(background="#d9d9d9")

        self.Button40 = Button(top)
        self.Button40.place(relx=0.34, rely=0.47, height=50, width=50)
        self.Button40.configure(background="#d9d9d9")

        self.Button41 = Button(top)
        self.Button41.place(relx=0.42, rely=0.47, height=50, width=50)
        self.Button41.configure(background="#d9d9d9")

        self.Button42 = Button(top)
        self.Button42.place(relx=0.50, rely=0.47, height=50, width=50)
        self.Button42.configure(background="#d9d9d9")

        self.Button43 = Button(top)
        self.Button43.place(relx=0.58, rely=0.47, height=50, width=50)
        self.Button43.configure(background="#d9d9d9")

        self.Button44 = Button(top)
        self.Button44.place(relx=0.66, rely=0.47, height=50, width=50)
        self.Button44.configure(background="#d9d9d9")

        self.Button45 = Button(top)
        self.Button45.place(relx=0.74, rely=0.47, height=50, width=50)
        self.Button45.configure(background="#d9d9d9")

        self.Button46 = Button(top)
        self.Button46.place(relx=0.10, rely=0.58, height=50, width=50)
        self.Button46.configure(background="#d9d9d9")

        self.Button47 = Button(top)
        self.Button47.place(relx=0.18, rely=0.58, height=50, width=50)
        self.Button47.configure(background="#d9d9d9")

        self.Button48 = Button(top)
        self.Button48.place(relx=0.26, rely=0.58, height=50, width=50)
        self.Button48.configure(background="#d9d9d9")

        self.Button49 = Button(top)
        self.Button49.place(relx=0.34, rely=0.58, height=50, width=50)
        self.Button49.configure(background="#d9d9d9")

        self.Button50 = Button(top)
        self.Button50.place(relx=0.42, rely=0.58, height=50, width=50)
        self.Button50.configure(background="#d9d9d9")

        self.Button51 = Button(top)
        self.Button51.place(relx=0.50, rely=0.58, height=50, width=50)
        self.Button51.configure(background="#d9d9d9")

        self.Button52 = Button(top)
        self.Button52.place(relx=0.58, rely=0.58, height=50, width=50)
        self.Button52.configure(background="#d9d9d9")

        self.Button53 = Button(top)
        self.Button53.place(relx=0.66, rely=0.58, height=50, width=50)
        self.Button53.configure(background="#d9d9d9")

        self.Button54 = Button(top)
        self.Button54.place(relx=0.74, rely=0.58, height=50, width=50)
        self.Button54.configure(background="#d9d9d9")

        self.Button55 = Button(top)
        self.Button55.place(relx=0.10, rely=0.69, height=50, width=50)
        self.Button55.configure(background="#d9d9d9")

        self.Button56 = Button(top)
        self.Button56.place(relx=0.18, rely=0.69, height=50, width=50)
        self.Button56.configure(background="#d9d9d9")

        self.Button57 = Button(top)
        self.Button57.place(relx=0.26, rely=0.69, height=50, width=50)
        self.Button57.configure(background="#d9d9d9")

        self.Button58 = Button(top)
        self.Button58.place(relx=0.34, rely=0.69, height=50, width=50)
        self.Button58.configure(background="#d9d9d9")

        self.Button59 = Button(top)
        self.Button59.place(relx=0.42, rely=0.69, height=50, width=50)
        self.Button59.configure(background="#d9d9d9")

        self.Button60 = Button(top)
        self.Button60.place(relx=0.50, rely=0.69, height=50, width=50)
        self.Button60.configure(background="#d9d9d9")

        self.Button61 = Button(top)
        self.Button61.place(relx=0.58, rely=0.69, height=50, width=50)
        self.Button61.configure(background="#d9d9d9")

        self.Button62 = Button(top)
        self.Button62.place(relx=0.66, rely=0.69, height=50, width=50)
        self.Button62.configure(background="#d9d9d9")

        self.Button63 = Button(top)
        self.Button63.place(relx=0.74, rely=0.69, height=50, width=50)
        self.Button63.configure(background="#d9d9d9")

        self.Button64 = Button(top)
        self.Button64.place(relx=0.10, rely=0.80, height=50, width=50)
        self.Button64.configure(background="#d9d9d9")

        self.Button65 = Button(top)
        self.Button65.place(relx=0.18, rely=0.80, height=50, width=50)
        self.Button65.configure(background="#d9d9d9")

        self.Button66 = Button(top)
        self.Button66.place(relx=0.26, rely=0.80, height=50, width=50)
        self.Button66.configure(background="#d9d9d9")

        self.Button67 = Button(top)
        self.Button67.place(relx=0.34, rely=0.80, height=50, width=50)
        self.Button67.configure(background="#d9d9d9")

        self.Button68 = Button(top)
        self.Button68.place(relx=0.42, rely=0.80, height=50, width=50)
        self.Button68.configure(background="#d9d9d9")

        self.Button69 = Button(top)
        self.Button69.place(relx=0.50, rely=0.80, height=50, width=50)
        self.Button69.configure(background="#d9d9d9")

        self.Button70 = Button(top)
        self.Button70.place(relx=0.58, rely=0.80, height=50, width=50)
        self.Button70.configure(background="#d9d9d9")

        self.Button71 = Button(top)
        self.Button71.place(relx=0.66, rely=0.80, height=50, width=50)
        self.Button71.configure(background="#d9d9d9")

        self.Button72 = Button(top)
        self.Button72.place(relx=0.74, rely=0.80, height=50, width=50)
        self.Button72.configure(background="#d9d9d9")

        self.Button73 = Button(top)
        self.Button73.place(relx=0.10, rely=0.91, height=50, width=50)
        self.Button73.configure(background="#d9d9d9")

        self.Button74 = Button(top)
        self.Button74.place(relx=0.18, rely=0.91, height=50, width=50)
        self.Button74.configure(background="#d9d9d9")

        self.Button75 = Button(top)
        self.Button75.place(relx=0.26, rely=0.91, height=50, width=50)
        self.Button75.configure(background="#d9d9d9")

        self.Button76 = Button(top)
        self.Button76.place(relx=0.34, rely=0.91, height=50, width=50)
        self.Button76.configure(background="#d9d9d9")

        self.Button77 = Button(top)
        self.Button77.place(relx=0.42, rely=0.91, height=50, width=50)
        self.Button77.configure(background="blue")

        self.Button78 = Button(top)
        self.Button78.place(relx=0.50, rely=0.91, height=50, width=50)
        self.Button78.configure(background="#d9d9d9")

        self.Button79 = Button(top)
        self.Button79.place(relx=0.58, rely=0.91, height=50, width=50)
        self.Button79.configure(background="#d9d9d9")

        self.Button80 = Button(top)
        self.Button80.place(relx=0.66, rely=0.91, height=50, width=50)
        self.Button80.configure(background="#d9d9d9")

        self.Button81 = Button(top)
        self.Button81.place(relx=0.74, rely=0.91, height=50, width=50)
        self.Button81.configure(background="#d9d9d9")

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

        self.Hayede = Button(top,command=music)
        self.Hayede.place(relx=0.80, rely=0.88, height=75, width=75)
        self.Hayede.configure(text="Play Hayede",background="#d9d9d9")


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


if __name__ == '__main__':
    vp_start_gui()
