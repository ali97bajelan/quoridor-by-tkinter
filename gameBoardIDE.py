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
    Board(root, session, num)
    root.mainloop()


class Board:
    def __init__(self, top=None, session=None, num=None):
        top.geometry("1000x700+200+50")
        top.title("Game Board")
        top.configure(background="gray")

        global color, wall
        color = ['red', 'blue', 'green', 'yellow']
        wall = [0 for i in range(num)]
        self.turn = 0

        def music():
            winsound.PlaySound('Vay-Behalash.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)

        self.status = Label(top, text=" Turn Player %s" % color[self.turn])
        self.status.place(relx=0.85, rely=0.10, height=50, width=120)

        ''' make places for pawns '''
        self.matrix = [[0 for i in range(9)] for j in range(9)]
        self.Button = [[0 for i in range(9)] for j in range(9)]  # main buttons

        i = 0
        j = 0
        x = 0.10
        y = 0.03
        while i < 9:
            while j < 9:
                self.Button[i][j] = Button(top)
                self.Button[i][j].place(relx=x, rely=y, height=50, width=50)
                self.Button[i][j].bind("<Button-1>", lambda a=None, f=i, g=j: self.move(session, f, g, num))
                self.Button[i][j].configure(background="gray88")
                self.matrix[i][j] = "gray88"

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
            self.matrix[4][0] = "yellow"
            self.matrix[4][8] = "green"
        self.Button[0][4].configure(background="red")
        self.Button[8][4].configure(background="blue")
        self.matrix[0][4] = "red"
        self.matrix[8][4] = "blue"

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
                                                                            self.v_wall[a][b], self.v_wall[a + 1][b],
                                                                            num))
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

    def move(self, session, i, j, num):
        # info = json.dumps(self.matrix)
        # t = requests.get(address.url['move'], data=info)
        # print(t.content)
        for a in range(9):
            for b in range(9):
                if self.Button[a][b]['bg'] == color[self.turn]:
                    f = a
                    g = b
                    break
            else:
                continue
            break

        des = self.Button[i][j]
        home = self.Button[f][g]
        if f == i and (g == j + 1 or g == j - 1):
            if g == j + 1:  # *** move to left ***
                if self.v_wall[i][j]['bg'] != 'black':
                    if des['bg'] == 'gray88':
                        des['bg'] = color[self.turn]
                        home['bg'] = 'gray88'
                        self.turn += 1
                    else:
                        tkinter.messagebox.showerror('Error', 'Pay attention to other Player pawns')
                else:
                    tkinter.messagebox.showerror('Error', "Pay attention to walls")
            else:  # *** move to right ***
                if self.v_wall[f][g]['bg'] != 'black':
                    if des['bg'] == 'gray88':
                        des['bg'] = color[self.turn]
                        home['bg'] = 'gray88'
                        self.turn += 1
                    else:
                        tkinter.messagebox.showerror('Error', 'Pay attention to other Player pawns')
                else:
                    tkinter.messagebox.showerror('Error', "Pay attention to walls")

        elif g == j and (f == i + 1 or f == i - 1):
            if f == i + 1:  # *** move to up ***
                if self.h_wall[i][j]['bg'] != 'black':
                    if des['bg'] == 'gray88':
                        des['bg'] = color[self.turn]
                        home['bg'] = 'gray88'
                        self.turn += 1
                    else:
                        tkinter.messagebox.showerror('Error', 'Pay attention to other Player pawns')
                else:
                    tkinter.messagebox.showerror('Error', "Pay attention to walls ")
            else:  # *** move to down ***
                if self.h_wall[f][g]['bg'] != 'black':
                    if des['bg'] == 'gray88':
                        des['bg'] = color[self.turn]
                        home['bg'] = 'gray88'
                        self.turn += 1
                    else:
                        tkinter.messagebox.showerror('Error', 'Pay attention to other Player pawns')
                else:
                    tkinter.messagebox.showerror('Error', "Pay attention to walls")
        else:
            tkinter.messagebox.showerror('Error', 'Choose correct location')

        if self.turn == num:
            self.turn = 0

        self.status['text'] = "turn Player %s" % color[self.turn]
        self.win(num)

    def decied(self, a, b, c, d, num):
        if wall[self.turn] == 20 / num:
            tkinter.messagebox.showerror('Error', ' You don\'t have any wall ')
            return False
        answer = tkinter.messagebox.askyesnocancel('Which side ?',
                                                   'Do you want Horizontal wall?(yes)\n \tVertical(no)')
        if str(answer) == 'True':
            if a['bg'] == 'black' or b['bg'] == 'black':
                tkinter.messagebox.showerror('Error', 'You cannot choose this location')
            else:
                a.configure(bg="black")
                b.configure(bg="black")
                wall[self.turn] += 1
                self.turn += 1

        if str(answer) == 'False':
            if c['bg'] == 'black' or d['bg'] == 'black':
                tkinter.messagebox.showerror('Error', 'You cannot choose this location')
            else:
                c.configure(bg="black")
                d.configure(bg="black")
                wall[self.turn] += 1
                self.turn += 1
        if self.turn == num:
            self.turn = 0

        self.status['text'] = "turn Player %s" % color[self.turn]

    def win(self, num):
        for m in range(9):
            if self.Button[8][m]['bg'] == 'red':
                tkinter.messagebox.showinfo(" Game was finish ", " Congratulation Player Red\n  You Win ")
                root.destroy()
                return False
        for m in range(9):
            if self.Button[0][m]['bg'] == 'blue':
                tkinter.messagebox.showinfo(" Game was finish ", " Congratulation Player Blue\n    You Win ")
                root.destroy()
                return False
        if num == 4:
            for m in range(9):
                if self.Button[m][0]['bg'] == 'green':
                    tkinter.messagebox.showinfo(" Game was finish ", " Congratulation Player Green\n   You Win ")
                    root.destroy()
                    return False
            for m in range(9):
                if self.Button[m][8]['bg'] == 'yellow':
                    tkinter.messagebox.showinfo(" Game was finish ", " Congratulation Player Yellow\n   You Win ")
                    root.destroy()
                    return False
