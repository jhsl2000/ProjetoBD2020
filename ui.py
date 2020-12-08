import psycopg2
import psycopg2.extras

from tkinter import *

import funcoes


def logout():
    screen3.destroy()


def voltar():
    screen4.destroy()


def register_user():
    screen1 = Toplevel()
    email_info = email.get()
    password_info = password.get()
    nome_info = nome.get()
    funcoes.insere_novo_user(email_info, password_info, nome_info)

    email_entry.delete(0, END)
    password_entry.delete(0, END)
    nome_entry.delete(0, END)

    if funcoes.confirma_novo_user(email_info, password_info) == 'registado':
        Label(screen1, text='Resgistado com sucesso!').pack()
        Button(screen1, text='Continuar para login', command=login).pack()
    else:
        Label(screen1, text='Erro').pack()


def login_verify():
    global screen2
    email1 = email_verify.get()
    password1 = password_verify.get()
    email_entry1.delete(0, END)
    password_entry1.delete(0, END)

    if funcoes.check_login(email1, password1) == 'cliente':
        print("Login bem sucedido!", email1)
        Label(screen2, text='Login bem sucedido!').pack()
        Button(screen2, text="Continuar", command=main_menu).pack()

    elif funcoes.check_login(email1, password1) == 'admin':

        print("Login bem sucedido!", email1)
        Label(screen2, text='Login bem sucedido admin!').pack()
        Button(screen2, text="Continuar", command=admin_main_menu).pack()

    elif funcoes.check_login(email1, password1) == 0:
        print("Login invalido!")
        Label1 = Label(screen2, text='Login Inválido!')
        Label1.pack()


def saldo():
    global screen7
    screen7 = Toplevel(screen)
    screen7.title("Adicionar Saldo")
    screen7.geometry("700x600")
    screen7.resizable(0, 0)
    screen7.propagate(0)
    global Entry1
    global Entry2
    global saldo_email
    global saldo_quantia 
    saldo_email = StringVar()
    saldo_quantia = DoubleVar()

    Label(screen7, text="").pack()
    Label(screen7, text="Insira o email que pretende adicionar saldo:").pack()
    Entry1 = Entry(screen7, textvariable=saldo_email)
    Entry1.pack()
    Label(screen7, text="").pack()
    Label(screen7, text="Insira a quantia:").pack()
    Entry2= Entry(screen7, textvariable=saldo_quantia)
    Entry2.pack()
    Label(screen7, text="").pack()
    Button(screen7, text="Enviar", command=enviar_saldo).pack()


def enviar_saldo():
    global screen
    saldo_email_info = saldo_email.get()
    saldo_quantia_info = saldo_quantia.get()
    funcoes.add_saldo(saldo_email_info, saldo_quantia_info)


    Entry1.delete(0, END)
    Entry2.delete(0, END)

    if funcoes.add_saldo(saldo_email_info, saldo_quantia_info) == 'confirma':
        Label(screen, text='Saldo atualizado!').pack()
    else:
        Label(screen, text='Erro').pack()

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
    email = StringVar()
    password = StringVar()
    nome = StringVar()

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


def artigos():
    global screen4
    screen4 = Tk()
    screen4.title("Artigos")
    screen4.geometry("700x600")
    screen4.resizable(0, 0)
    screen4.propagate(0)

    Label(screen4, text="").pack()
    Label(screen4, text="").pack()
    Label(screen4, text="").pack()
    Label(screen4, text="").pack()
    Label(screen4, text="").pack()
    Label(screen4, text="").pack()
    Button(screen4, height=2, width=10, text="Filmes", command=filmes).pack()
    Label(screen4, text="").pack()
    Label(screen4, text="").pack()
    Label(screen4, text="").pack()
    Button(screen4, height=2, width=10, text="Series", command=series).pack()
    Label(screen4, text="").pack()
    Label(screen4, text="").pack()
    Label(screen4, text="").pack()
    Button(screen4, height=2, width=10, text="Voltar", command=voltar).pack()

'''
def adicionar_artigos():
    global screen
    screen = Tk()
    screen.title("Artigos")
    screen.geometry("1280x720")
    screen.resizable(0, 0)
    screen.propagate(0)
    global nome_artigo
    global tempo
    global tipo_artigo

    nome_artigo = StringVar()
    tempo = StringVar()
    tipo_artigo = StringVar()

    Label(screen, text="").pack()
    Label(screen, text="").pack()
    Label(screen, text="").pack()
    Label(screen, text="Nome:").pack()
    Entry(screen, textvariable=nome_artigo).pack()
    Label(screen, text="").pack()
    Label(screen, text="Tempo disponivel em dias:").pack()
    Entry(screen, textvariable=tempo).pack()
    Label(screen, text="").pack()
    Label(screen, text="Tipo do artigo:").pack()
    Entry(screen, textvariable=tipo_artigo).pack()
'''

def filmes():
    global screen5
    screen5 = Tk()
    screen5.title("Filmes")
    screen5.geometry("1280x720")
    screen5.resizable(0, 0)
    screen5.propagate(0)


def series():
    global screen6
    screen6 = Tk()
    screen6.title("Series")
    screen6.geometry("1280x720")
    screen6.resizable(0, 0)
    screen6.propagate(0)


def main_menu():
    screen2.destroy()
    global screen3
    screen3 = Tk()
    screen3.title("Menu principal")
    screen3.geometry("1280x720")
    screen3.resizable(0, 0)
    photo3 = PhotoImage(file='NETFLOX.png')
    photo = Label(screen, image=photo3, height=300, width=250)
    photo.pack()
    screen3.propagate(0)

    # Label(screen3, text="saldo=").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Button(screen3, height=2, width=10, text="Artigos", command=artigos).pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Button(screen3, height=2, width=12, text="Carrinho").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Button(screen3, height=2, width=12, text="Caixa de Entrada").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Button(screen3, text="Logout", fg="red", command=logout).pack()


def admin_main_menu():
    screen2.destroy()
    global screen3
    screen3 = Tk()
    screen3.title("Menu principal")
    screen3.geometry("1280x720")
    screen3.resizable(0, 0)
    photo3 = PhotoImage(file='NETFLOX.png')
    photo = Label(screen, image=photo3, height=300, width=250)
    photo.pack()
    screen3.propagate(0)

    # Label(screen3, text="saldo=").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Button(screen3, height=2, width=15, text="Adicionar Artigos", command=adicionar_artigos).pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Button(screen3, height=2, width=15, text="Alterar preco artigo").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Button(screen3, height=2, width=15, text="Adicionar saldo", command=saldo).pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Button(screen3, height=2, width=15, text="Mensagens").pack()


def adicionar_artigos():
    global screen8
    screen8 = Toplevel(screen)
    screen8.title("Adicionar Artigos")
    screen8.geometry("700x600")
    screen8.resizable(0, 0)
    screen8.propagate(0)
    Label(screen8, text="").pack()
    Label(screen8, text="").pack()
    Label(screen8, text="").pack()
    Label(screen8, text="Que tipo de artigo pretende adicionar?").pack()
    Label(screen8, text="").pack()
    Label(screen8, text="").pack()
    Label(screen8, text="").pack()
    Label(screen8, text="").pack()
    Label(screen8, text="").pack()
    Label(screen8, text="").pack()
    Button(screen8, height=2, width=15, text="Filme", command=add_filme).pack()
    Label(screen8, text="").pack()
    Label(screen8, text="").pack()
    Label(screen8, text="").pack()
    Button(screen8, height=2, width=15, text="Série", command=add_serie).pack()
    Label(screen8, text="").pack()
    Label(screen8, text="").pack()
    Label(screen8, text="").pack()
    Button(screen8, height=2, width=15, text="Documentário", command=add_documentario).pack()



def add_filme():
    global screen
    global tipo_artigo
    global Entry1
    global nome_artigo
    global Entry2
    global horas_disp
    global Entry3
    global preco_artigo
    nome_artigo = StringVar()
    horas_disp = IntVar()
    preco_artigo = DoubleVar()
    tipo_artigo = StringVar()
    screen8.destroy()
    screen = Toplevel(screen)
    screen.title("Adicionar Filme")
    screen.geometry("700x600")
    screen.resizable(0, 0)
    screen.propagate(0)
    
    Label(screen, text="").pack()
    Label(screen, text="").pack()
    Label(screen, text="").pack()
    tipo_artigo = 'Filme'
    Label(screen, text="Insira o nome do filme que pretende adicionar:").pack()
    Entry1 = Entry(screen, textvariable=nome_artigo)
    Entry1.pack()
    Label(screen, text="").pack()
    Label(screen, text="").pack()
    Label(screen, text="").pack()
    Label(screen, text="Insira o número de horas que pretende que o filme esteja disponível:").pack()
    Entry2 = Entry(screen, textvariable=horas_disp)
    Entry2.pack()
    Label(screen, text="").pack()
    Label(screen, text="").pack()
    Label(screen, text="").pack()
    Label(screen, text="Insira o preço do filme:").pack()
    Entry3 = Entry(screen, textvariable=preco_artigo)
    Entry3.pack()
    Label(screen, text="").pack()
    Label(screen, text="").pack()
    Button(screen, text="Enviar", command=enviar_artigo).pack()


    




    
def add_serie():
    global screen
    global tipo_artigo
    global Entry1
    global nome_artigo
    global Entry2
    global horas_disp
    global Entry3
    global preco_artigo
    nome_artigo = StringVar()
    horas_disp = IntVar()
    preco_artigo = DoubleVar()
    tipo_artigo = StringVar()
    screen8.destroy()
    screen7 = Toplevel(screen)
    screen7.title("Adicionar Série")
    screen7.geometry("700x600")
    screen7.resizable(0, 0)
    screen7.propagate(0)
    
    tipo_artigo = 'Série'
    Label(screen, text="Insira o nome da série que pretende adicionar:").pack()
    Entry1 = Entry(screen, textvariable=nome_artigo)
    Entry1.pack()
    Label(screen, text="Insira o número de horas que pretende que a série esteja disponível:").pack()
    Entry2 = Entry(screen, textvariable=horas_disp)
    Entry2.pack()
    Label(screen, text="Insira o preço da série:").pack()
    Entry3 = Entry(screen, textvariable=preco_artigo)
    Entry3.pack()




def add_documentario():
    global screen
    global tipo_artigo
    global Entry1
    global nome_artigo
    global Entry2
    global horas_disp
    global Entry3
    global preco_artigo
    nome_artigo = StringVar()
    horas_disp = IntVar()
    preco_artigo = DoubleVar()
    tipo_artigo = StringVar()
    screen8.destroy()
    screen7 = Toplevel(screen)
    screen7.title("Adicionar Documentário")
    screen7.geometry("700x600")
    screen7.resizable(0, 0)
    screen7.propagate(0)
    
    tipo_artigo = 'Documentário'
    Label(screen, text="Insira o nome do documentário que pretende adicionar:").pack()
    Entry1 = Entry(screen, textvariable=nome_artigo)
    Entry1.pack()
    Label(screen, text="Insira o número de horas que pretende que o documentário esteja disponível:").pack()
    Entry2 = Entry(screen, textvariable=horas_disp)
    Entry2.pack()
    Label(screen, text="Insira o preço do documentário:").pack()
    Entry3 = Entry(screen, textvariable=preco_artigo)
    Entry3.pack()



def enviar_artigo():
    global screen
    tipo_info = tipo_artigo
    nome_info = nome_artigo
    horas_info = horas_disp.get()
    preco_info = preco_artigo.get()

    funcoes.addartigo(tipo_info, nome_info, horas_info, preco_info)


    Entry1.delete(0, END)
    Entry2.delete(0, END)
    Entry3.delete(0, END)

    if funcoes.addartigo(tipo_artigo, nome_artigo, horas_disp, preco_artigo) == 'confirma':
        Label(screen, text='Artigo adicionado!').pack()
    else:
        Label(screen, text='Erro').pack()





def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("500x300")
    Label(screen2, text="Insere os detalhes para Login").pack()
    Label(screen2, text="").pack()

    global email_verify
    global password_verify

    email_verify = StringVar()
    password_verify = StringVar()

    global email_entry1
    global password_entry1

    Label(screen2, text="Email : ").pack()
    email_entry1 = Entry(screen2, textvariable=email_verify)
    email_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password : ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify, show='*')
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", command=login_verify).pack()


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
    Button(text="Register", padx=4, activebackground='white', activeforeground='black', command=register).pack()
    # ignorar as seguintes linhas: apenas para espaço entre botoes e copyright
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
