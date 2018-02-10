from tkinter import *
from tkinter import ttk


# from tkinter import Tk,Label
class App:
    def __init__(self, master):
        frame = ttk.Frame(master)
        frame.grid()
        # f2 = ttk.Frame(master, width=500, height=170)
        # f2.grid()
        # global frame
        self.label = ttk.Label(frame, text="\nWelcome to Quridor game \n \n \n")

        self.label.grid(row=0, column=0, columnspan=1)

        self.playButton = ttk.Button(frame, text="Play", command=self.printMessage)
        self.playButton.grid(row=1, column=0)

        self.pLogo = PhotoImage(file='play.png')
        self.small_pLogo = self.pLogo.subsample(5, 5)
        self.playButton.config(image=self.small_pLogo, compound=LEFT)

        self.registerButton = ttk.Button(frame, text="Register", command=self.signup)
        self.registerButton.grid(row=2, column=0)

        self.rLogo = PhotoImage(file='Register.png')
        self.small_rLogo = self.rLogo.subsample(7, 9)
        self.registerButton.config(image=self.small_rLogo, compound=LEFT)

        self.loginButton = ttk.Button(frame, text="Log in", command=self.login)
        self.loginButton.grid(row=3, column=0)

        self.lLogo = PhotoImage(file='login.png')
        self.small_lLogo = self.lLogo.subsample(13, 17)
        self.loginButton.config(image=self.small_lLogo, compound=LEFT)

        self.logoutButton = ttk.Button(frame, text="Log out", command=self.printMessage)
        self.logoutButton.grid(row=4, column=0)

        self.oLogo = PhotoImage(file='logout.png')
        self.small_oLogo = self.oLogo.subsample(7, 9)
        self.logoutButton.config(image=self.small_oLogo, compound=LEFT)

        self.quitButton = ttk.Button(frame, text="Quit", command=frame.quit)
        self.quitButton.grid(row=5, column=0)

        self.qLogo = PhotoImage(file='exit.png')
        self.small_qLogo = self.qLogo.subsample(7, 9)
        self.quitButton.config(image=self.small_qLogo, compound=LEFT)


    def printMessage(self):
        print("Wow this actually worked!")

    def name(self):
        self.label.config(text="Welcome to Quridor game \n \n \n  Rigester Menu")

    def login(self):
        login = Toplevel()
        Label(login, text="Login").pack()

    def signup(self):
        signup = Toplevel()
        signup.title(' Register ')

        usern_label = ttk.Label(signup, text="Username")
        usern_label.grid(row=1, column=0, columnspan=2)
        # username = StringVar()
        usern = ttk.Entry(signup, width=30)  # , textvariable=username)
        usern.grid(row=1, column=2)

        passw_label = ttk.Label(signup, text="Password")
        passw_label.grid(row=2, column=0, columnspan=2)
        password = StringVar()
        passw = ttk.Entry(signup, width=30, textvariable=password)
        passw.grid(row=2, column=2)

        confirm_label = ttk.Label(signup, text="Confirm Password")
        confirm_label.grid(row=3, column=0, columnspan=2)
        confirm = StringVar()
        conf = ttk.Entry(signup, width=30, textvariable=confirm)
        conf.grid(row=3, column=2)

        signupButton = ttk.Button(signup, text="Register", command=print(passw.get()))
        signupButton.grid(row=4, column=2)
        x = usern.get()
        print(x)


def main():
    root = Tk()
    root.geometry("1000x700+200+50")
    App(root)
    root.resizable(width=False, height=False)
    root.title("Quridor Game")
    root.mainloop()


if __name__ == "__main__":
    main()
