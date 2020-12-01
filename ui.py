import psycopg2
import psycopg2.extras

from tkinter import *

import funcoes


"""def teste():
        connection = psycopg2.connect("host=localhost dbname=testes user=postgres password=postgres")
        cursor = connection.cursor()
        cursor.execute(" INSERT INTO utilizador (nome, idade) VALUES ('rodrigo', 15)")
        cursor.execute("SELECT * FROM utilizador")
        connection.commit() 
       
        print("Registado com sucesso")
        for linha in cursor.fetchall():
            nome, idade = linha
            print (linha)
        
        connection.commit()
        cursor.close()
        connection.close()
"""

def register_user():
    email_info = email.get()
    password_info = password.get()
    nome_info = nome.get()
    funcoes.insere_novo_user(email_info, password_info, nome_info)

    email_entry.delete(0, END)
    password_entry.delete(0, END)
    nome_entry.delete(0, END)


def login_verify():

    email1 = email_verify.get()
    password1 = password_verify.get()
    email_entry1.delete(0, END)
    password_entry1.delete(0, END)

    if funcoes.check_login(email1, password1) == 'cliente':
        print("Login bem sucedido!", email1)


def register():
    global screen
    screen1 = Toplevel(screen)
    screen1.title("Registar")
    screen1.geometry("500x300")
    photo2 = PhotoImage(file='NETFLOX.png')
    photo = Label(screen, image=photo2, height=300, width=250)
    photo.pack()

    global email
    global password
    global nome
    global email_entry
    global password_entry
    global nome_entry
    email=StringVar()
    password=StringVar()
    nome=StringVar()

    Label(screen1, text="Insere os detalhes em baixo: ").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Nome: ").pack()
    nome_entry = Entry(screen1, textvariable=nome)
    nome_entry.pack()
    Label(screen1, text="Email: ").pack()
    email_entry = Entry(screen1, textvariable=email)
    email_entry.pack()
    Label(screen1, text="Password: ").pack()
    password_entry = Entry(screen1, textvariable=password, show="*")
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Registar", command=register_user).pack()


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("500x300")
    Label(screen2, text= "Insere os detalhes para Login").pack()
    Label(screen2, text="").pack()

    global email_verify
    global password_verify

    email_verify = StringVar()
    password_verify = StringVar()

    global email_entry1
    global password_entry1

    Label(screen2, text = "Email : ").pack()
    email_entry1 = Entry(screen2, textvariable=email_verify)
    email_entry1.pack()
    Label(screen2, text = "").pack()
    Label(screen2, text="Password : ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify, show='*')
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", command= login_verify).pack()


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
    Label(text="").pack()
    Button(text="Register", padx=4, activebackground='white',activeforeground='black',  command=register).pack()
    #ignorar as seguintes linhas: apenas para espaço entre botoes e copyright
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(screen, text='Copyright Jose Lourenco & Rodrigo Mendes', font={'Arial', 9}).pack()
    screen.mainloop()


main_screen()