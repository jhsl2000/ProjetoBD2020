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
    global email1
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
    global screen7
    saldo_email_info = saldo_email.get()
    saldo_quantia_info = saldo_quantia.get()
    if funcoes.add_saldo(saldo_email_info, saldo_quantia_info) == 'confirma':
        Label(screen7, text='Saldo atualizado!').pack()
    else:
        Label(screen7, text='Erro').pack()

    Entry1.delete(0, END)
    Entry2.delete(0, END)


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


def mensagens():
    global screen15
    screen15 = Toplevel(screen)
    screen15.title("Mensagens")
    screen15.geometry("400x300")
    screen15.resizable(0, 0)
    screen15.propagate(0)

    Label(screen15, text="").pack()
    Label(screen15, text="Pretende enviar para:").pack()
    Label(screen15, text="").pack()
    Button(screen15, text="Utilizador especifico", command=mensagens_para_um_utilizador).pack()
    Label(screen15, text="").pack()
    Label(screen15, text="").pack()
    Button(screen15, text="Todos os utilizadores", command=mensagens_para_todos).pack()

def mensagens_utilizador():
    global screen20
    screen20=Toplevel(screen)
    screen20.title("Caixa de entrada de mensagens")
    screen20.geometry("400x300")
    screen20.resizable(0, 0)
    screen20.propagate(0)

    Label(screen20, text="").pack()
    Label(screen20, text="").pack()
    Label(screen20, text="Pretende...").pack()
    Label(screen20, text="").pack()
    Button(screen20,height=2, width=18, text="Ver mensagens recebidas", command=utilizador_ver_mensagens).pack()
    Label(screen20, text="").pack()
    Button(screen20,height=2, width=18, text="Escrever mensagem", command=utilizador_escrever_mensagem).pack()

def utilizador_escrever_mensagem():
    global screen18
    screen18 = Toplevel(screen)
    screen18.title("Mensagens")
    screen18.geometry("1280x720")
    screen18.resizable(0, 0)
    screen18.propagate(0)

    global mensagem_utilizador
    global assunto_utilizador
    assunto_utilizador = StringVar()
    mensagem_utilizador = StringVar()

    Label(screen18, text="").pack()
    Label(screen18, text="").pack()
    Label(screen18, text="Irá enviar uma mensagem para os administradores", fg="red").pack()
    Label(screen18, text="Insira o assunto:").pack()
    Label(screen18, text="").pack()
    Entry2 = Entry(screen18, textvariable=assunto_utilizador)
    Entry2.pack()
    Label(screen18, text="").pack()
    Label(screen18, text="Insira a mensagem").pack()
    Entry3 = Entry(screen18, textvariable=mensagem_utilizador)
    Entry3.pack(padx=50, pady=25, ipadx=50, ipady=50)
    Button(screen18, text="Enviar", command=utilizador_enviar_mensagem).pack()

def utilizador_enviar_mensagem():
    global screen18

    assunto_utilizador_info = assunto_utilizador.get()
    mensagem_utilizador_info = mensagem_utilizador.get()

def utilizador_ver_mensagens():
    global screen22
    screen22 = Toplevel(screen)
    screen22.title("Mensagens")
    screen22.geometry("1280x720")
    screen22.resizable(0, 0)
    screen22.propagate(0)

    for linha in funcoes.utilizador_ver_todas_mensagens(email1):
        Label(screen13, text="Destinatario:").pack()
        Label(screen13, text=linha[0]).pack()
        Label(screen13, text="Assunto:").pack()
        Label(screen13, text=linha[1]).pack()
        Label(screen13, text="Texto:").pack()
        Label(screen13, text=linha[2]).pack()
        Label(screen13, text="").pack()
        Label(screen13, text="---------------").pack()


def mensagens_para_um_utilizador():

    global screen8
    screen8 = Toplevel(screen)
    screen8.title("Mensagens")
    screen8.geometry("1280x720")
    screen8.resizable(0, 0)
    screen8.propagate(0)
    global destinatario
    global mensagem
    global assunto
    destinatario = StringVar()
    assunto = StringVar()
    mensagem = StringVar()
   
    Label(screen8, text="").pack()
    Label(screen8, text="").pack()
    Label(screen8, text="Destinatario:").pack()
    Label(screen8, text="").pack()
    Entry1 = Entry(screen8, textvariable=destinatario)
    Entry1.pack()   
    Label(screen8, text="").pack()
    Label(screen8, text="Insira o assunto:").pack()
    Label(screen8, text="").pack()
    Entry2 = Entry(screen8, textvariable=assunto)
    Entry2.pack()
    Label(screen8, text="").pack()
    Label(screen8, text="Insira a mensagem").pack()
    Entry3 =Entry(screen8, textvariable=mensagem)
    Entry3.pack(padx=50, pady = 25, ipadx = 50, ipady= 50)
    Button(screen8, text="Enviar", command = enviar_mensagem).pack()


def mensagens_para_todos():
    global screen16
    screen16 = Toplevel(screen)
    screen16.title("Mensagens")
    screen16.geometry("1280x720")
    screen16.resizable(0, 0)
    screen16.propagate(0)

    global mensagem_todos
    global assunto_todos
    mensagem_todos = StringVar()
    assunto_todos = StringVar()

    Label(screen16, text="").pack()
    Label(screen16, text="").pack()
    Label(screen16, text="Insira o assunto:").pack()
    Label(screen16, text="").pack()
    Entry2 = Entry(screen16, textvariable=assunto_todos)
    Entry2.pack()
    Label(screen16, text="").pack()
    Label(screen16, text="Insira a mensagem").pack()
    Entry3 =Entry(screen16, textvariable=mensagem_todos)
    Entry3.pack(padx=50, pady = 25, ipadx = 50, ipady= 50)
    Button(screen16, text="Enviar", command = enviar_mensagem_todos).pack()


def enviar_mensagem_todos():
    global screen16

    mensagem_todos_info = mensagem_todos.get()
    assunto_todos_info = assunto_todos.get()
    
    if funcoes.envia_mensagem_todos(mensagem_todos_info, assunto_todos_info) == 'mensagem_aceite':
        Label(screen16, text="Mensagem enviada").pack()
    else:
        Label(screen16, text="Erro no envio da mensagem").pack()


def enviar_mensagem():
    global screen8
    destinatario_info = destinatario.get()
    assunto_info = assunto.get()
    mensagem_info = mensagem.get()

    if funcoes.seleciona_clientes(destinatario_info, assunto_info, mensagem_info) == 'mensagem_aceite':
        Label(screen8, text="Mensagem enviada").pack()
    else:
        Label(screen8, text="Erro no envio da mensagem").pack()


def admin_caixa_entrada_mensagens():
    global screen9
    screen9 = Toplevel(screen)
    screen9.title("Mensagens")
    screen9.geometry("600x500")
    screen9.resizable(0, 0)
    screen9.propagate(0)

    Label(screen9, text="").pack()
    Label(screen9, text="").pack()
    Button(screen9, text="Pesquisar por utilizador", command = admin_mensagens_utilizador).pack()
    Label(screen9, text="").pack()
    Label(screen9, text="").pack()
    Button(screen9, text="Ver todas as mensagens enviadas", command = admin_ver_todas_mensagens).pack()

    
def admin_mensagens_utilizador():
    global screen11
    screen11 = Toplevel(screen)
    screen11.title("Mensagens")
    screen11.geometry("400x300")
    screen11.resizable(0, 0)
    screen11.propagate(0)

    global nome_utilizador
    nome_utilizador = StringVar()

    Label(screen11, text="").pack()
    Label(screen11, text="").pack()
    Label(screen11, text="Insira o nome do utilizador:").pack()
    Label(screen11, text="").pack()
    Entry(screen11, textvariable = nome_utilizador).pack()
    Button(screen11, text="Pesquisar", command=admin_ver_mensagens_utilizador).pack()

def admin_ver_mensagens_utilizador():
    global screen12
    screen12 = Toplevel(screen)
    screen12.title("Mensagens")
    screen12.geometry("1280x720")
    screen12.resizable(0, 0)
    screen12.propagate(0)

    nome_utilizador_info = nome_utilizador.get()

    for linha in funcoes.admin_ver_mensagens_utilizador(nome_utilizador_info):
        Label(screen12, text=linha[0]).pack()
        Label(screen12, text=linha[1]).pack()
        Label(screen12, text="").pack()
        Label(screen12, text="").pack()

  


def admin_ver_todas_mensagens():
    global screen13
    screen13 = Toplevel(screen)
    screen13.title("Mensagens")
    screen13.geometry("1280x720")
    screen13.resizable(0, 0)
    screen13.propagate(0)

    for linha in funcoes.admin_ver_todas_mensagens():
        Label(screen13, text="-------------------------------------").pack()
        Label(screen13, text="Destinatario:  " + linha[0] + " Assunto:  " + linha[1] + " Texto:  " + linha[2]).pack()




#def utilizador_enviar_mensagem():


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

    Label(screen3, text="Saldo:").pack()
    Label(screen3, text=funcoes.consulta_saldo(email1), font= {'Arial', 25 }).pack()
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
    Button(screen3, height=2, width=12, text="Biblioteca").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Button(screen3, height=2, width=15, text="Caixa de mensagens", command=mensagens_utilizador).pack()
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
    Button(screen3, height=2, width=15, text="Adicionar Artigos", command=adicionar_artigos).pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Button(screen3, height=2, width=15, text="Alterar preco artigo").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Button(screen3, height=2, width=15, text="Adicionar saldo", command=saldo).pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Button(screen3, height=2, width=15, text="Enviar mensagens", command=mensagens).pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Button(screen3, height=2, width=25, text="Caixa de entrada de Mensagens", command=admin_caixa_entrada_mensagens).pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Button(screen3, height=2, width=25, text="Ver estatisticas", command=ver_estatisticas).pack()

def ver_estatisticas():
    global screen23
    screen23 = Toplevel(screen)
    screen23.title("Mensagens")
    screen23.geometry("400x200")
    screen23.resizable(0, 0)
    screen23.propagate(0)

    Label(screen23, text="Qual a estatistica que pretende ver:", fg="blue").pack()
    Button(screen23,height=2, width=15, text="Total de clientes", command=total_clientes).pack()
    Label(screen23, text="").pack()
    Button(screen23,height=2, width=15, text="Total de artigos", command=estatisticas_artigos).pack()

def total_clientes():
    global screen24
    screen24 = Toplevel(screen)
    screen24.title("Total de clientes")
    screen24.geometry("400x700")
    screen24.resizable(0, 0)
    screen24.propagate(0)

    Label(screen24, text="Total de clientes").pack()
    Label(screen24, text=funcoes.total_utilizadores(), fg= 'green').pack()
    Label(screen24, text="").pack()
    for linha in funcoes.return_clientes():
        Label(screen24, text="-------------------------------------").pack()
        Label(screen24, text="Nome,Email:  " + linha[0] ).pack()

def estatisticas_artigos():
    global screen25
    screen25 = Toplevel(screen)
    screen25.title("Total de clientes")
    screen25.geometry("1280x720")
    screen25.resizable(0, 0)
    screen25.propagate(0)

    Label(screen25, text="Total de artigos").pack()
    Label(screen25, text=funcoes.total_artigos(), fg= 'green').pack()
    Label(screen25, text="").pack()


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
    global screen25
    screen25 = Toplevel(screen)
    screen25.title("Estatistica de Artigos ")
    screen25.geometry("400x700")
    screen25.resizable(0, 0)
    screen25.propagate(0)


def add_filme():
    global screen10
    screen8.destroy()
    screen10 = Toplevel(screen)
    screen10.title("Adicionar Filme")
    screen10.geometry("1280x720")
    screen10.resizable(0, 0)
    screen10.propagate(0)
    global tipo_artigo
    global nome_artigo
    global realizador
    global ator
    global horas_disp
    global preco_artigo
    global nome_entrada
    global realizador_entrada
    global ator_entrada
    global horas_entrada
    global preco_entrada
    nome_artigo = StringVar()
    tipo_artigo = StringVar()
    realizador = StringVar()
    ator = StringVar()
    horas_disp = DoubleVar()
    preco_artigo = DoubleVar()
    
    tipo_artigo.set('Filme')
    Label(screen10, text="").pack()
    Label(screen10, text="Insira o nome do filme que pretende adicionar:").pack()
    nome_entrada = Entry(screen10, textvariable=nome_artigo)
    nome_entrada.pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="Insira o realizador do filme:").pack()
    realizador_entrada = Entry(screen10, textvariable=realizador)
    realizador_entrada.pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="Insira o ator principal do filme:").pack()
    ator_entrada = Entry(screen10, textvariable=ator)
    ator_entrada.pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="Insira o número de horas que pretende que o filme esteja disponível:").pack()
    horas_entrada = Entry(screen10, textvariable=horas_disp)
    horas_entrada.pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="Insira o preço do filme:").pack()
    preco_entrada = Entry(screen10, textvariable=preco_artigo)
    preco_entrada.pack()
    Label(screen10, text="").pack()
    Button(screen10, text="Enviar", command=enviar_artigo).pack()

    
def add_serie():
    global screen10
    screen8.destroy()
    screen10 = Toplevel(screen)
    screen10.title("Adicionar Filme")
    screen10.geometry("1280x720")
    screen10.resizable(0, 0)
    screen10.propagate(0)
    global tipo_artigo
    global nome_artigo
    global realizador
    global ator
    global horas_disp
    global preco_artigo
    global nome_entrada
    global realizador_entrada
    global ator_entrada
    global horas_entrada
    global preco_entrada
    nome_artigo = StringVar()
    tipo_artigo = StringVar()
    realizador = StringVar()
    ator = StringVar()
    horas_disp = DoubleVar()
    preco_artigo = DoubleVar()
    
    tipo_artigo.set('Filme')
    Label(screen10, text="").pack()
    Label(screen10, text="Insira o nome do filme que pretende adicionar:").pack()
    nome_entrada = Entry(screen10, textvariable=nome_artigo)
    nome_entrada.pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="Insira o realizador do filme:").pack()
    realizador_entrada = Entry(screen10, textvariable=realizador)
    realizador_entrada.pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="Insira o ator principal do filme:").pack()
    ator_entrada = Entry(screen10, textvariable=ator)
    ator_entrada.pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="Insira o número de horas que pretende que o filme esteja disponível:").pack()
    horas_entrada = Entry(screen10, textvariable=horas_disp)
    horas_entrada.pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="Insira o preço do filme:").pack()
    preco_entrada = Entry(screen10, textvariable=preco_artigo)
    preco_entrada.pack()
    Label(screen10, text="").pack()
    Button(screen10, text="Enviar", command=enviar_artigo).pack()




def add_documentario():
    global screen10
    screen8.destroy()
    screen10 = Toplevel(screen)
    screen10.title("Adicionar Filme")
    screen10.geometry("1280x720")
    screen10.resizable(0, 0)
    screen10.propagate(0)
    global tipo_artigo
    global nome_artigo
    global realizador
    global ator
    global horas_disp
    global preco_artigo
    global nome_entrada
    global realizador_entrada
    global ator_entrada
    global horas_entrada
    global preco_entrada
    nome_artigo = StringVar()
    tipo_artigo = StringVar()
    realizador = StringVar()
    ator = StringVar()
    horas_disp = DoubleVar()
    preco_artigo = DoubleVar()
    
    tipo_artigo.set('Filme')
    Label(screen10, text="").pack()
    Label(screen10, text="Insira o nome do filme que pretende adicionar:").pack()
    nome_entrada = Entry(screen10, textvariable=nome_artigo)
    nome_entrada.pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="Insira o realizador do filme:").pack()
    realizador_entrada = Entry(screen10, textvariable=realizador)
    realizador_entrada.pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="Insira o ator principal do filme:").pack()
    ator_entrada = Entry(screen10, textvariable=ator)
    ator_entrada.pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="Insira o número de horas que pretende que o filme esteja disponível:").pack()
    horas_entrada = Entry(screen10, textvariable=horas_disp)
    horas_entrada.pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="Insira o preço do filme:").pack()
    preco_entrada = Entry(screen10, textvariable=preco_artigo)
    preco_entrada.pack()
    Label(screen10, text="").pack()
    Button(screen10, text="Enviar", command=enviar_artigo).pack()



def enviar_artigo():
    global screen
    tipo_info = tipo_artigo.get()
    nome_info = nome_artigo.get()
    realizador_info = realizador.get()
    ator_info = ator.get()
    horas_info = horas_disp.get()
    preco_info = preco_artigo.get()

    funcoes.addartigo(tipo_info, nome_info, horas_info, preco_info, realizador_info, ator_info)


    nome_entrada.delete(0, END)
    horas_entrada.delete(0, END)
    preco_entrada.delete(0, END)
    realizador_entrada.delete(0, END)
    ator_entrada.delete(0, END)

    if funcoes.confirma_novo_artigo(nome_info, realizador_info) == 'confirma':
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
