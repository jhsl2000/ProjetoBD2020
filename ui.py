from tkinter import *


def register_user():
    username_info = username.get()
    password_info = password.get()


def register():
    global screen
    screen1 = Toplevel(screen)
    screen1.title("Registar")
    screen1.geometry("1280x720")
    photo2 = PhotoImage(file='NETFLOX.png')
    photo = Label(screen, image=photo2, height=300, width=250)
    photo.pack()

    global username
    global password
    global username_entry
    global password_entry

    username=StringVar()
    password=StringVar()
    Label(screen1, text="Insere os detalhes em baixo: ").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username: ").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text="Password: ").pack()
    password_entry = Entry(screen1, textvariable = password, show="*")
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Registar", command = register_user).pack()


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("1280x720")
    Label(screen2, text= "Insere os detalhes para Login").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    Label(screen2, text = "Username * ").pack()
    username_verify = Entry(screen2, textvariable = username_verify)

    Label(screen2, text = "").pack()
    Label(screen2, text= "Password * ").pack()

    Label(screen2, text="").pack()
    Button(screen2, "Login").pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("1280x720")
    screen.title("Netflox 1.0")
    photo2 = PhotoImage(file='NETFLOX.png')
    photo = Label(screen, image=photo2, height=300, width=250)
    photo.pack()
    Button(text="Login", command=login).pack()
    Label(text="").pack()
    Button(text="Register", command=register).pack()

    screen.mainloop()


main_screen()
