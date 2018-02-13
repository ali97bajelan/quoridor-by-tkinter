from tkinter import *
from tkinter import Button
import tkinter.messagebox
import requests
import winsound
import address
import json


def start_gui(session, num):
    """Starting point when module is the main routine."""
    global root
    root = Tk()
    top = NewToplevel(root, session, num)
    root.mainloop()


class NewToplevel:
    def __init__(self, top=None, session=None, num=None):

        top.geometry("1000x700+200+50")
        top.title("Game Board")
        top.configure(background="gray")

        def music():
            winsound.PlaySound('Vay-Behalash.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)

        self.Button = [[0 for i in range(9)] for j in range(9)]  # main buttons

        i = 0
        j = 0
        x = 0.10
        y = 0.03
        while i < 9:
            while j < 9:
                self.Button[i][j] = Button(top)
                self.Button[i][j].place(relx=x, rely=y, height=50, width=50)
                self.Button[i][j].bind("<Button-1>", lambda a=None, f=i, g=j: self.move(session, f, g))
                self.Button[i][j].configure(background="#d9d9d9")

                j += 1
                x += 0.08
            j = 0
            x = 0.10
            y += 0.11
            i += 1
        ''' make players color '''
        if num == 4:
            self.Button[4][0].configure(background="yellow")
            self.Button[4][8].configure(background="green")
        self.Button[0][4].configure(background="red")
        self.Button[8][4].configure(background="blue")

        ''' make horizontal walls'''

        self.h_wall = [[0 for z in range(9)] for w in range(8)]
        i = 0
        j = 0
        x = 0.10
        y = 0.11
        while i < 8:
            while j < 9:
                self.h_wall[i][j] = Button(top)
                self.h_wall[i][j].place(relx=x, rely=y, height=15, width=50)
                self.h_wall[i][j].configure(background="white")
                j += 1
                x += 0.08
            j = 0
            x = 0.10
            y += 0.11
            i += 1

        ''' make vertical walls'''

        self.v_wall = [[0 for z in range(8)] for w in range(9)]
        i = 0
        j = 0
        x = 0.16
        y = 0.03
        while i < 9:
            while j < 8:
                self.v_wall[i][j] = Button(top)
                self.v_wall[i][j].place(relx=x, rely=y, height=50, width=15)
                self.v_wall[i][j].configure(background="white")
                j += 1
                x += 0.08
            j = 0
            x = 0.16
            y += 0.11
            i += 1

        ''' make center buttons of walls'''

        self.c_wall = [[0 for z in range(8)] for w in range(8)]
        i = 0
        j = 0
        x = 0.16
        y = 0.11
        while i < 8:
            while j < 8:
                self.c_wall[i][j] = Button(top)
                self.c_wall[i][j].place(relx=x, rely=y, height=15, width=15)
                self.c_wall[i][j].bind("<Button-1>",
                                       lambda f=None, a=i, b=j: self.decied(self.h_wall[a][b], self.h_wall[a][b + 1],
                                                                            self.v_wall[a][b], self.v_wall[a + 1][b]))
                self.c_wall[i][j].configure(background="white")

                j += 1
                x += 0.08
            j = 0
            x = 0.16
            y += 0.11
            i += 1

        self.Hayede = Button(top, command=music)
        self.Hayede.place(relx=0.80, rely=0.88, height=75, width=75)
        self.Hayede.configure(text="Play Hayede", background="#d9d9d9")

    def move(self, session, i, j):
        # info = json.dumps(self.Button)
        # t = requests.get(address.url['move'], data=info)
        # print(t.content)
        # while
        x = self.Button[i][j]
        if i == 0 and j == 0:
            a = self.Button[1][0]
            b = self.Button[0][1]
        elif i == 8 and j == 8:
            a = self.Button[8][7]
            b = self.Button[7][8]
        elif i == 0 and j == 8:
            a = self.Button[1][8]
            b = self.Button[0][7]
        elif i == 8 and j == 0:
            a = self.Button[8][1]
            b = self.Button[7][0]
        elif i == 0 and j != 0:
            a = self.Button[i][j + 1]
            b = self.Button[i][j - 1]
            c = self.Button[i + 1][j]
        elif j == 0 and i != 0:
            a = self.Button[i][j + 1]
            b = self.Button[i - 1][j]
            c = self.Button[i + 1][j]
        elif i == 8 and j != 8:
            a = self.Button[i][j + 1]
            b = self.Button[i][j - 1]
            c = self.Button[i - 1][j]
        elif j == 8 and i != 8:
            a = self.Button[i][j - 1]
            b = self.Button[i - 1][j]
            c = self.Button[i + 1][j]
        else:
            a = self.Button[i][j - 1]
            b = self.Button[i - 1][j]
            c = self.Button[i + 1][j]
            d = self.Button[i][j + 1]
        try:
            if a['bg'] == 'red':
                a['bg'] = 'gray88'
                x['bg'] = 'red'
                return True
            if b['bg'] == 'red':
                b['bg'] = 'gray88'
                x['bg'] = 'red'
                return True
            if c['bg'] == 'red':
                c['bg'] = 'gray88'
                x['bg'] = 'red'
                return True
            if d['bg'] == 'red':
                d['bg'] = 'gray88'
                x['bg'] = 'red'
                return True
        except UnboundLocalError:
            pass

    def decied(self, a, b, c, d):
        answer = tkinter.messagebox.askyesnocancel('Which side ?', 'Do you want Horizontal wall?(yes)\n \tVertical(no)')
        if str(answer) == 'True':
            if a['bg'] == 'black' or b['bg'] == 'black':
                tkinter.messagebox.showerror('Error', 'You cannot choose this location')
            else:
                a.configure(bg="black")
                b.configure(bg="black")

        if str(answer) == 'False':
            if c['bg'] == 'black' or d['bg'] == 'black':
                tkinter.messagebox.showerror('Error', 'You cannot choose this location')
            else:
                c.configure(bg="black")
                d.configure(bg="black")
