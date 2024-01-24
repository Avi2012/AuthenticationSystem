from tkinter import *
from tkinter import messagebox
# Win setup
window = Tk()
window.geometry('300x300')
window.resizable(False, False)
window.title('Authentication System')
DataBase = open('Database.txt', 'a')
DataBase.close()

# Functions
def Open_LogIn():
    LogIn.pack(fill='both', expand=1)
    Main_Frame.pack_forget()

def Open_SignUp_Register():
    SignUp_Register.pack(fill='both', expand=1)
    Main_Frame.pack_forget()

def SignUp_Register_To_Main_Frame():
    Main_Frame.pack(fill='both', expand=1)
    SignUp_Register.pack_forget()

def LogIn_To_Main_Frame():
    Main_Frame.pack(fill='both', expand=1)
    LogIn.pack_forget()

# Pages/Frames setup
Main_Frame = Frame(window, bg='#D1ffBD')
SignUp_Register = Frame(window, bg='#A3D5FF')
LogIn = Frame(window, bg='#A3D5FF')
Main_Frame.pack(fill='both', expand=1)

# Switching between frames
label = Label(Main_Frame, text='Authentication System', bg='#d3d3d3', font=('Arial Rounded MT Bold', 20))
label.pack()

Go_SignUp_Register = Button(Main_Frame, text='SignUp/Register', command=Open_SignUp_Register, bg='#CEFAD0', font=('Arial Rounded MT Bold', 20))
Go_SignUp_Register.pack(pady=20)

Go_LogIn = Button(Main_Frame, text='LogIn', command=Open_LogIn, bg='#CEFAD0', font=('Arial Rounded MT Bold', 21))
Go_LogIn.pack(pady=25)

Button(SignUp_Register, text='🏠', command=SignUp_Register_To_Main_Frame).place(x=0, y=0)
Button(LogIn, text='🏠', command=LogIn_To_Main_Frame).place(x=0, y=0)

# SignUp/Register
def register_user():
    user = Username_Info.get()
    pwd = Password_Info.get()

    with open('Database.txt', 'a') as file:
        file.write(f"{user},{pwd}\n")

    Username_Info.delete(0, END)
    Password_Info.delete(0, END)
    

S_R_Box = Label(SignUp_Register, bg='#6F9CDE')
S_R_Box.pack(pady=40)

def SignUp_Register_Info():
    Label(S_R_Box, text='Username', bg='#6F9CDE', font=('Arial Rounded MT Bold', 30)).pack()
    global Username_Info
    Username_Info = Entry(S_R_Box)
    Username_Info.pack()

    Label(S_R_Box, text='Password', bg='#6F9CDE', font=('Arial Rounded MT Bold', 30)).pack()
    global Password_Info
    Password_Info = Entry(S_R_Box, show='*')
    Password_Info.pack()

    Button(S_R_Box, text='Submit', font=('Arial Rounded MT Bold', 13), command=register_user).pack()

SignUp_Register_Info()

# LogIn
def Check_LogIn():
    username = Username_Entry.get()
    password = Password_Entry.get()

    with open('Database.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            u, p = line.strip().split(",")
            if username == u:
                if password == p:
                    messagebox.showinfo('Susessful', '---Login Successful---')
                    return
                else:
                    messagebox.showerror('Error!', 'Incorrect Password Entered!')
                    return
        messagebox.showerror('Error!', '---Use Not Found---')

L_Box = Label(LogIn, bg='#6F9CDE', pady=200, padx=200)
L_Box.pack(pady=40)

def LogIn_SignIn():
    Label(L_Box, text='Username', bg='#6F9CDE', font=('Arial Rounded MT Bold', 30)).pack()
    global Username_Entry
    Username_Entry = Entry(L_Box)
    Username_Entry.pack()

    Label(L_Box, text='Password', bg='#6F9CDE', font=('Arial Rounded MT Bold', 30)).pack()
    global Password_Entry
    Password_Entry = Entry(L_Box, show='*')
    Password_Entry.pack()

    Button(L_Box, text='LogIn', font=('Arial Rounded MT Bold', 13), command=Check_LogIn).pack()

LogIn_SignIn()

# Calling main
Main_Frame.tkraise()
window.mainloop()
