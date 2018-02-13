from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import address
import requests
import gameBoardIDE

# from tkinter import Tk,Label
class App:
    def __init__(self, master):
        session = requests.session()
        self.label = ttk.Label(master, text="Welcome to Quridor game")
        self.label.place(relx=0.42, rely=0.01, height=100, width=300)

        self.playButton = ttk.Button(master, text="   Play")
        self.playButton.place(relx=0.42, rely=0.15, height=80, width=150)
        self.playButton.bind("<Button-1>", lambda event: self.start(session))

        self.pLogo = PhotoImage(file='play.png')
        self.small_pLogo = self.pLogo.subsample(5, 5)
        self.playButton.config(image=self.small_pLogo, compound=LEFT)

        self.registerButton = ttk.Button(master, text="Register")
        self.registerButton.place(relx=0.42, rely=0.30, height=80, width=150)
        self.registerButton.bind("<Button-1>", lambda event: self.signup(session))

        self.rLogo = PhotoImage(file='Register.png')
        self.small_rLogo = self.rLogo.subsample(7, 9)
        self.registerButton.config(image=self.small_rLogo, compound=LEFT)

        self.loginButton = ttk.Button(master, text="  Log in", command=lambda e: self.login(session))
        self.loginButton.place(relx=0.42, rely=0.45, height=80, width=150)
        self.loginButton.bind("<Button-1>", lambda event: self.login(session))

        self.lLogo = PhotoImage(file='login.png')
        self.small_lLogo = self.lLogo.subsample(13, 17)
        self.loginButton.config(image=self.small_lLogo, compound=LEFT)

        self.logoutButton = ttk.Button(master, text="Log out")
        self.logoutButton.place(relx=0.42, rely=0.60, height=80, width=150)
        self.logoutButton.bind("<Button-1>", lambda event: self.logout(session))

        self.oLogo = PhotoImage(file='logout.png')
        self.small_oLogo = self.oLogo.subsample(7, 9)
        self.logoutButton.config(image=self.small_oLogo, compound=LEFT)

        self.quitButton = ttk.Button(master, text="Quit", command=master.quit)
        self.quitButton.place(relx=0.42, rely=0.75, height=80, width=150)

        self.qLogo = PhotoImage(file='exit.png')
        self.small_qLogo = self.qLogo.subsample(7, 9)
        self.quitButton.config(image=self.small_qLogo, compound=LEFT)

    def start(self, session):
        inquiry = session.get(address.url['dummy'])
        if "NOT" in str(inquiry.content):
            tkinter.messagebox.showerror("Error", "Really??? You are not Log in")
            return False
        else:
            ques = tkinter.messagebox.askquestion("Which game ?", "Two Players?(yes) \n Four Players?(no)")
            print(ques)
            if str(ques) == "yes":
                print("Bia")
                gameBoardIDE.start_gui(session)

            else:
                print("Na")


    def login(self, session):
        def inquiry():
            if not (usern.get() and passw.get()):
                tkinter.messagebox.showerror("Error", " Please fill all fields ")
                return False
            a = usern.get()
            b = passw.get()
            info = dict(username=a, password=b)
            r = session.post(address.url['login'], data=info)
            print(r.content)
            if "Sorry" in str(r.content):
                tkinter.messagebox.showerror("Error", " Your information is incorrect ")
                return False
            else:
                tkinter.messagebox.showinfo("congralition", " You are logged in ")
                login.destroy()
                return True

        login = Toplevel()
        login.title(' Log in ')
        login.geometry("400x250+500+300")
        login.resizable(width=False, height=False)

        usern_label = ttk.Label(login, text="  Username")
        usern_label.place(relx=0.10, rely=0.20, height=20, width=150)

        usern = ttk.Entry(login, width=30)
        usern.place(relx=0.35, rely=0.20, height=20, width=150)

        passw_label = ttk.Label(login, text="  Password")
        passw_label.place(relx=0.10, rely=0.30, height=20, width=150)

        passw = ttk.Entry(login, width=30)
        passw.place(relx=0.35, rely=0.30, height=20, width=150)

        loginButton = ttk.Button(login, text="Log in", command=inquiry)
        loginButton.place(relx=0.45, rely=0.50, height=30, width=65)

    def signup(self, session):
        def confirm():
            if not (usern.get() and passw.get() and conf.get()):
                tkinter.messagebox.showerror("Error", " Please fill all fields ")
                return False
            a = passw.get()
            b = conf.get()
            c = usern.get()
            if a == b:
                info = dict(username=c, password=a)
                t = requests.post(address.url['register'], data=info)
                if "Already" in str(t.content):
                    tkinter.messagebox.showerror("Error", "You Already registered")
                else:
                    tkinter.messagebox.showinfo("Congraddoffogk", "You are Registered")
                    signup.destroy()
            else:
                tkinter.messagebox.showerror("Error", " Choose same password ")
                return False

        signup = Toplevel()
        signup.title(' Register ')
        signup.geometry("400x250+500+300")
        signup.resizable(width=False, height=False)

        label = ttk.Label(signup, text="Fill the form")
        label.place(relx=0.45, rely=0.05, height=20, width=150)

        usern_label = ttk.Label(signup, text="  Username")
        usern_label.place(relx=0.10, rely=0.20, height=20, width=150)

        usern = ttk.Entry(signup, width=30)
        usern.place(relx=0.35, rely=0.20, height=20, width=150)

        passw_label = ttk.Label(signup, text="  Password")
        passw_label.place(relx=0.10, rely=0.30, height=20, width=150)

        passw = ttk.Entry(signup, width=30)
        passw.place(relx=0.35, rely=0.30, height=20, width=150)

        confirm_label = ttk.Label(signup, text="Confirm Password")
        confirm_label.place(relx=0.05, rely=0.40, height=20, width=150)

        conf = ttk.Entry(signup, width=30)
        conf.place(relx=0.35, rely=0.40, height=20, width=150)

        signupButton = ttk.Button(signup, text="Register", command=confirm)
        signupButton.place(relx=0.45, rely=0.50, height=30, width=65)

    def logout(self, session):
        inquiry = session.get(address.url['dummy'])
        if "NOT" in str(inquiry.content):
            tkinter.messagebox.showerror("Error", "Really??? You are not Log in")
            return False
        else:
            ques = tkinter.messagebox.askyesno("Are you sure?", "   Logout really??")
            if str(ques) == "True":
                command = session.get(address.url['logout'])
                tkinter.messagebox.showinfo("Goodbye", "You are logged out")
                return True
            else:
                return False


def main():
    root = Tk()
    root.geometry("600x550+400+150")
    App(root)
    root.resizable(width=False, height=False)
    root.title("Quridor Game")
    root.mainloop()


if __name__ == "__main__":
    main()
