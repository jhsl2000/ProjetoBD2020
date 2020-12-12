import psycopg2
import psycopg2.extras
from passlib.hash import sha256_crypt

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
    password_encriptada = sha256_crypt.hash(password_info)
    print(password_encriptada)
    nome_info = nome.get()
    funcoes.insere_novo_user(email_info, password_encriptada, nome_info)

    email_entry.delete(0, END)
    password_entry.delete(0, END)
    nome_entry.delete(0, END)

    if funcoes.confirma_novo_user(email_info, password_encriptada) == 'registado':
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
    Button(screen4, height=2, width=10, text="Documentários", command=documentarios).pack()
    Label(screen4, text="").pack()
    Label(screen4, text="").pack()
    Label(screen4, text="").pack()
    Button(screen4, height=2, width=10, text="Voltar", command=voltar).pack()





def filmes():
    Fonte = {'Verdana', 20}
    global screen5
    global id_filme
    screen5 = Toplevel(screen)
    screen5.title("Filmes")
    screen5.geometry("1280x720")
    screen5.resizable(0, 0)
    screen5.propagate(0)
    id_filme = DoubleVar()
    
    

    for linha in funcoes.ver_filmes():
        Label(screen5, text="").pack()
        Label(screen5, text="Nome: " + linha[0], font=Fonte).pack()
        Label(screen5, text="ID: ").pack()
        Label(screen5, text=linha[1]).pack()
        Label(screen5, text="").pack()
        Label(screen5, text="---------------").pack()
        
    Label(screen5, text="Qual o ID do filme que pretende visualizar os detalhes?").pack()
    Entry_filme = Entry(screen5, textvariable=id_filme)
    Entry_filme.pack()
    Button(screen5, height=2, width=10, text='Ver descrições', command=ver_descricao_filmes).pack()
    Button(screen5, height=2, width=10, text='Alugar', command=alugar_produto).pack()


def series():
    Fonte = {'Verdana', 20}
    global screen6
    global id_serie
    screen6 = Toplevel(screen)
    screen6.title("Séries")
    screen6.geometry("1280x720")
    screen6.resizable(0, 0)
    screen6.propagate(0)
    id_serie = DoubleVar()
    
    

    for linha in funcoes.ver_series():
        Label(screen6, text="").pack()
        Label(screen6, text="Nome: " + linha[0], font=Fonte).pack()
        Label(screen6, text="ID: ").pack()
        Label(screen6, text=linha[1]).pack()
        Label(screen6, text="").pack()
        Label(screen6, text="---------------").pack()
        
    Label(screen6, text="Qual o ID da série que pretende visualizar os detalhes?").pack()
    Entry_serie = Entry(screen6, textvariable=id_serie)
    Entry_serie.pack()
    Button(screen6, height=2, width=10, text='Ver descrições', command=ver_descricao_series).pack()
    Button(screen6, height=2, width=10, text='Alugar', command=alugar_produto).pack()


def documentarios():
    Fonte = {'Verdana', 20}
    global screen15
    global id_documentario
    screen15 = Toplevel(screen)
    screen15.title("Documentários")
    screen15.geometry("1280x720")
    screen15.resizable(0, 0)
    screen15.propagate(0)
    id_documentario = DoubleVar()
    
    

    for linha in funcoes.ver_documentarios():
        Label(screen15, text="").pack()
        Label(screen15, text="Nome: " + linha[0], font=Fonte).pack()
        Label(screen15, text="ID: ").pack()
        Label(screen15, text=linha[1]).pack()
        Label(screen15, text="").pack()
        Label(screen15, text="---------------").pack()
        
    Label(screen15, text="Qual o ID do documentário que pretende visualizar os detalhes?").pack()
    Entry_documentario = Entry(screen15, textvariable=id_documentario)
    Entry_documentario.pack()
    Button(screen15, height=2, width=10, text='Ver descrições', command=ver_descricao_documentarios).pack()
    Button(screen15, height=2, width=10, text='Alugar', command=alugar_produto).pack()



def alugar_produto():
    global screen55
    global id_alugar
    global Entry_produto_alugar
    screen55 = Toplevel(screen)
    screen55.title("Alugar")
    screen55.geometry("400x300")
    screen55.resizable(0, 0)
    screen55.propagate(0)
    id_alugar = DoubleVar()

    Label(screen55, text="Qual o ID do documentário que pretende alugar?").pack()
    Entry_produto_alugar = Entry(screen55, textvariable=id_alugar)
    Entry_produto_alugar.pack()
    Button(screen55, height=2, width=10, text='Alugar', command=produto_alugar).pack()




def produto_alugar():
    global screen  
    
    
    id_alugar_info = id_alugar.get()

    funcoes.alugar(id_alugar_info, email1)







def ver_descricao_filmes():
    Fonte = {'Verdana', 20}
    global screen71
    screen71 = Toplevel(screen)
    screen71.title("Descrição Filmes")
    screen71.geometry("500x600")
    screen71.resizable(0, 0)
    screen71.propagate(0)

    id_filme_info = id_filme.get()

    for linha in funcoes.ver_descricao_filmes(id_filme_info):
        Label(screen71, text="").pack()
        Label(screen71, text="").pack()
        Label(screen71, text="").pack()
        Label(screen71, text="").pack()
        Label(screen71, text="---------------").pack()
        Label(screen71, text="").pack()
        Label(screen71, text="").pack()
        Label(screen71, text=linha[0], font=Fonte).pack()
        Label(screen71, text="").pack()
        Label(screen71, text="Tipo: " + linha[1]).pack()
        Label(screen71, text="").pack()
        Label(screen71, text="Realizador: " + linha[2]).pack()
        Label(screen71, text="").pack()
        Label(screen71, text="Ator: " + linha[3]).pack()
        Label(screen71, text="").pack()
        Label(screen71, text="Tempo disponível: ").pack()
        Label(screen71, text=linha[4]).pack()
        Label(screen71, text="").pack()
        Label(screen71, text="Preço: ").pack()
        Label(screen71, text=linha[5]).pack()
        Label(screen71, text="").pack()
        Label(screen71, text="").pack()
        Label(screen71, text="---------------").pack()



def ver_descricao_series():
    Fonte = {'Verdana', 20}
    global screen20
    screen20 = Toplevel(screen)
    screen20.title("Descrição Séries")
    screen20.geometry("500x600")
    screen20.resizable(0, 0)
    screen20.propagate(0)

    id_serie_info = id_serie.get()
    

    for linha in funcoes.ver_descricao_series(id_serie_info):
        Label(screen20, text="").pack()
        Label(screen20, text="").pack()
        Label(screen20, text="").pack()
        Label(screen20, text="").pack()
        Label(screen20, text="---------------").pack()
        Label(screen20, text="").pack()
        Label(screen20, text="").pack()
        Label(screen20, text=linha[0], font=Fonte).pack()
        Label(screen20, text="").pack()
        Label(screen20, text="Tipo: " + linha[1]).pack()
        Label(screen20, text="").pack()
        Label(screen20, text="Realizador: " + linha[2]).pack()
        Label(screen20, text="").pack()
        Label(screen20, text="Ator: " + linha[3]).pack()
        Label(screen20, text="").pack()
        Label(screen20, text="Tempo disponível: ").pack()
        Label(screen20, text=linha[4]).pack()
        Label(screen20, text="").pack()
        Label(screen20, text="Preço: ").pack()
        Label(screen20, text=linha[5]).pack()
        Label(screen20, text="").pack()
        Label(screen20, text="").pack()
        Label(screen20, text="---------------").pack()





def ver_descricao_documentarios():
    Fonte = {'Verdana', 20}
    global screen72
    screen72 = Toplevel(screen)
    screen72.title("Descrição Documentários")
    screen72.geometry("500x600")
    screen72.resizable(0, 0)
    screen72.propagate(0)

    id_documentario_info = id_documentario.get()
    

    for linha in funcoes.ver_descricao_documentarios(id_documentario_info):
        Label(screen72, text="").pack()
        Label(screen72, text="").pack()
        Label(screen72, text="").pack()
        Label(screen72, text="").pack()
        Label(screen72, text="---------------").pack()
        Label(screen72, text="").pack()
        Label(screen72, text="").pack()
        Label(screen72, text=linha[0], font=Fonte).pack()
        Label(screen72, text="").pack()
        Label(screen72, text="Tipo: " + linha[1]).pack()
        Label(screen72, text="").pack()
        Label(screen72, text="Realizador: " + linha[2]).pack()
        Label(screen72, text="").pack()
        Label(screen72, text="Ator: " + linha[3]).pack()
        Label(screen72, text="").pack()
        Label(screen72, text="Tempo disponível: ").pack()
        Label(screen72, text=linha[4]).pack()
        Label(screen72, text="").pack()
        Label(screen72, text="Preço: ").pack()
        Label(screen72, text=linha[5]).pack()
        Label(screen72, text="").pack()
        Label(screen72, text="").pack()
        Label(screen72, text="---------------").pack()







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

    if funcoes.utilizador_enviar_mensagem(mensagem_utilizador_info, assunto_utilizador_info,email1) == 'mensagem_aceite':
        Label(screen18, text="Mensagem enviada").pack()
    else:
        Label(screen18, text="Erro no envio da mensagem").pack()


def utilizador_ver_mensagens():
    global screen22
    screen22 = Toplevel(screen)
    screen22.title("Mensagens")
    screen22.geometry("1280x720")
    screen22.resizable(0, 0)
    screen22.propagate(0)

    for linha in funcoes.utilizador_ver_todas_mensagens(email1):
        Label(screen22, text="Assunto:").pack()
        Label(screen22, text=linha[0]).pack()
        Label(screen22, text="Texto:").pack()
        Label(screen22, text=linha[1]).pack()
        Label(screen22, text="---------------").pack()


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
    
    if funcoes.envia_mensagem_todos(mensagem_todos_info, assunto_todos_info, email1) == 'mensagem_aceite':
        Label(screen16, text="Mensagem enviada").pack()
    else:
        Label(screen16, text="Erro no envio da mensagem").pack()


def enviar_mensagem():
    global screen8
    destinatario_info = destinatario.get()
    assunto_info = assunto.get()
    mensagem_info = mensagem.get()

    if funcoes.seleciona_clientes(mensagem_info, assunto_info, destinatario_info,email1) == 'mensagem_aceite':
        Label(screen8, text="Mensagem enviada").pack()
    else:
        Label(screen8, text="Erro no envio da mensagem").pack()


def admin_caixa_entrada_mensagens():
    global screen9
    screen9 = Toplevel(screen)
    screen9.title("Mensagens")
    screen9.geometry("400x300")
    screen9.resizable(0, 0)
    screen9.propagate(0)

    Label(screen9, text="").pack()
    Label(screen9, text="").pack()
    Button(screen9, height=2, width=35, text="Ver mensagens enviadas a 1 utilizador", command = admin_mensagens_utilizador).pack()
    Label(screen9, text="").pack()
    Label(screen9, text="").pack()
    Button(screen9, height=2, width=25,text="Ver todas as mensagens enviadas", command = admin_ver_todas_mensagens).pack()
    Label(screen9, text="").pack()
    Label(screen9, text="").pack()
    Button(screen9,height=2, width=25 , text="Ver todas as mensagens recebidas", command = admin_ver_todas_mensagens_recebidas).pack()
    
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

def admin_ver_todas_mensagens_recebidas():
    global screen40
    screen40 = Toplevel(screen)
    screen40.title("Mensagens")
    screen40.geometry("1280x720")
    screen40.resizable(0, 0)
    screen40.propagate(0)

    for linha in funcoes.admin_ver_mensagens_recebidas(email1):
        Label(screen40, text="De:  " + linha[0]).pack()
        Label(screen40, text="Assunto: " + linha[1]).pack()
        Label(screen40, text="Texto: " + linha[2]).pack()
        Label(screen40, text="-----------------").pack()



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
    Button(screen3, height=2, width=12, text="Pesquisar", command=pesquisa).pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Button(screen3, height=2, width=12, text="Biblioteca", command=biblioteca).pack()
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



def pesquisa():
    global screen36
    screen36 = Toplevel()
    screen36.title("Pesquisar")
    screen36.geometry("700x600")
    screen36.resizable(0, 0)
    screen36.propagate(0)

    Label(screen36, text="").pack()
    Button(screen36, height=2, width=15, text="Pesquisa por tipo", command=artigos).pack()
    Label(screen36, text="").pack()
    Button(screen36, height=2, width=15, text="Pesquisa por título", command=pesquisa_por_titulo).pack()
    Label(screen36, text="").pack()
    Button(screen36, height=2, width=15, text="Pesquisa por ator", command=pesquisa_por_ator).pack()
    Label(screen36, text="").pack()
    Button(screen36, height=2, width=15, text="Pesquisa por realizador", command=pesquisa_por_realizador).pack()
    Label(screen36, text="").pack()
    Button(screen36, height=2, width=20, text="Pesquisa por preço MAX", command=pesquisa_por_preco).pack()
    Label(screen36, text="").pack()



def pesquisa_por_titulo():
    global screen200
    screen200 = Toplevel()
    screen200.title("Pesquisar")
    screen200.geometry("700x600")
    screen200.resizable(0, 0)
    screen200.propagate(0)
    global Entry18
    global titulo_pesquisa

    titulo_pesquisa = StringVar()

    Label(screen200, text="").pack()
    Label(screen200, text="Qual o título do produto que pretende observar?").pack()
    Entry18 = Entry(screen200, textvariable=titulo_pesquisa)
    Entry18.pack()
    Button(screen200, height=2, width=15, text="Pesquisar", command=pesquisa_titulo).pack()


def pesquisa_titulo():

    global screen201
    screen201 = Toplevel()
    screen201.title("Pesquisar por Título")
    screen201.geometry("700x600")
    screen201.resizable(0, 0)
    screen201.propagate(0)

    titulo_pesquisa_info = titulo_pesquisa.get()

    for linha in funcoes.pesquisar_titulo(titulo_pesquisa_info):
        Label(screen201, text="---------------").pack()
        Label(screen201, text="").pack()
        Label(screen201, text="").pack()
        Label(screen201, text=linha[0]).pack()
        Label(screen201, text="").pack()
        Label(screen201, text="Tipo: " + linha[1]).pack()
        Label(screen201, text="").pack()
        Label(screen201, text="Realizador: " + linha[2]).pack()
        Label(screen201, text="").pack()
        Label(screen201, text="Ator: " + linha[3]).pack()
        Label(screen201, text="").pack()
        Label(screen201, text="Tempo disponível: ").pack()
        Label(screen201, text=linha[4]).pack()
        Label(screen201, text="").pack()
        Label(screen201, text="Preço: ").pack()
        Label(screen201, text=linha[5]).pack()
        Label(screen201, text="").pack()
        Label(screen201, text="").pack()
        Label(screen201, text="---------------").pack()
    

def pesquisa_por_ator():
    global screen201
    screen201 = Toplevel()
    screen201.title("Pesquisar")
    screen201.geometry("700x600")
    screen201.resizable(0, 0)
    screen201.propagate(0)
    global Entry22
    global ator_pesquisa

    ator_pesquisa = StringVar()


    Label(screen201, text="").pack()
    Label(screen201, text="Qual o ator que pretende observar?").pack()
    Entry22 = Entry(screen201, textvariable=ator_pesquisa)
    Entry22.pack()
    Button(screen201, height=2, width=15, text="Pesquisar", command=pesquisa_ator).pack()


def pesquisa_ator():
    global screen203
    screen203 = Toplevel()
    screen203.title("Pesquisar por Título")
    screen203.geometry("700x600")
    screen203.resizable(0, 0)
    screen203.propagate(0)

    ator_pesquisa_info = ator_pesquisa.get()
    Label(screen203, text="Este ator aparece em: ", fg="red")
    for linha in funcoes.pesquisar_ator(ator_pesquisa_info):
        Label(screen203, text="---------------").pack()
        Label(screen203, text=linha[0]).pack()


def pesquisa_por_realizador():
    global screen205
    screen205 = Toplevel()
    screen205.title("Pesquisar")
    screen205.geometry("700x600")
    screen205.resizable(0, 0)
    screen205.propagate(0)
    global Entry24
    global realizador_pesquisa

    realizador_pesquisa = StringVar()

    Label(screen205, text="").pack()
    Label(screen205, text="Qual o realizador que pretende observar?").pack()
    Entry25 = Entry(screen205, textvariable=realizador_pesquisa)
    Entry25.pack()
    Button(screen205, height=2, width=15, text="Pesquisar", command=pesquisa_realizador).pack()


def pesquisa_realizador():
    global screen206
    screen206 = Toplevel()
    screen206.title("Pesquisar por Título")
    screen206.geometry("700x600")
    screen206.resizable(0, 0)
    screen206.propagate(0)

    realizador_pesquisa_info = realizador_pesquisa.get()
    Label(screen206, text="Este realizador aparece em: ", fg="red")
    for linha in funcoes.pesquisar_realizador(realizador_pesquisa_info):
        Label(screen206, text="---------------").pack()
        Label(screen206, text=linha[0]).pack()


def pesquisa_por_preco():
    global screen207
    screen207 = Toplevel()
    screen207.title("Pesquisar")
    screen207.geometry("700x600")
    screen207.resizable(0, 0)
    screen207.propagate(0)
    global Entry32
    global preco_pesquisa

    preco_pesquisa = DoubleVar()

    Label(screen207, text="").pack()
    Label(screen207, text="Qual o preço máximo que pretende observar?").pack()
    Entry32 = Entry(screen207, textvariable=preco_pesquisa)
    Entry32.pack()
    Button(screen207, height=2, width=15, text="Pesquisar", command=pesquisa_preco).pack()

def pesquisa_preco():
    global screen208
    screen208 = Toplevel()
    screen208.title("Pesquisar por Título")
    screen208.geometry("700x600")
    screen208.resizable(0, 0)
    screen208.propagate(0)

    preco_pesquisa_info = preco_pesquisa.get()
    Label(screen208, text="Filmes com preço máximo introduzido: ", fg="red")
    for linha in funcoes.pesquisar_preco(preco_pesquisa_info):
        Label(screen208, text="---------------").pack()
        Label(screen208, text=linha[0]).pack()
        Label(screen208, text= linha[1]).pack()

def biblioteca():
    global screen30
    screen30 = Toplevel()
    screen30.title("Artigos alugados")
    screen30.geometry("700x600")
    screen30.resizable(0, 0)
    screen30.propagate(0)

    Label(screen30, text="").pack()
    Label(screen30, text="").pack()
    Label(screen30, text="").pack()
    Label(screen30, text="").pack()
    Label(screen30, text="").pack()
    Label(screen30, text="").pack()
    Button(screen30, height=2, width=10, text="Filmes", command=filmes_comprados).pack()
    Label(screen30, text="").pack()
    Label(screen30, text="").pack()
    Label(screen30, text="").pack()
    Button(screen30, height=2, width=10, text="Series", command=series_compradas).pack()
    Label(screen30, text="").pack()
    Label(screen30, text="").pack()
    Label(screen30, text="").pack()
    Button(screen30, height=2, width=10, text="Documentários", command=documentarios_comprados).pack()
    Label(screen30, text="").pack()
    Label(screen30, text="").pack()
    Label(screen30, text="").pack()


def filmes_comprados():
    global screen31
    screen31 = Toplevel(screen)
    screen31.title("Filmes Comprados")
    screen31.geometry("1280x720")
    screen31.resizable(0, 0)
    screen31.propagate(0)
    
    for linha in funcoes.ver_filmes_comprados(email1):
        Label(screen31, text="").pack()
        Label(screen31, text="").pack()
        Label(screen31, text=linha[0]).pack()
        Label(screen31, text="").pack()
        Label(screen31, text="Tipo: ").pack()
        Label(screen31, text=linha[1]).pack()
        Label(screen31, text="Data da compra: ").pack()
        Label(screen31, text=linha[2]).pack()
        Label(screen31, text="Tempo disponível: ").pack()
        Label(screen31, text=linha[3]).pack()




def series_compradas():
    global screen32 
    screen32 = Toplevel(screen)
    screen32.title("Séries Compradas")
    screen32.geometry("1280x720")
    screen32.resizable(0, 0)
    screen32.propagate(0)
    
    for linha in funcoes.ver_series_compradas(email1):
        Label(screen32, text="").pack()
        Label(screen32, text="").pack()
        Label(screen32, text=linha[0]).pack()
        Label(screen32, text="").pack()
        Label(screen32, text="Tipo: ").pack()
        Label(screen32, text=linha[1]).pack()
        Label(screen32, text="Data da compra: ").pack()
        Label(screen32, text=linha[2]).pack()
        Label(screen32, text="Tempo disponível: ").pack()
        Label(screen32, text=linha[3]).pack()




def documentarios_comprados():
    global screen33
    screen33 = Toplevel(screen)
    screen33.title("Documentários Comprados")
    screen33.geometry("1280x720")
    screen33.resizable(0, 0)
    screen33.propagate(0)
    
    for linha in funcoes.ver_documentarios_comprados(email1):
        Label(screen33, text="").pack()
        Label(screen33, text="").pack()
        Label(screen33, text=linha[0]).pack()
        Label(screen33, text="").pack()
        Label(screen33, text="Tipo: ").pack()
        Label(screen33, text=linha[1]).pack()
        Label(screen33, text="Data da compra: ").pack()
        Label(screen33, text=linha[2]).pack()
        Label(screen33, text="Tempo disponível: ").pack()
        Label(screen33, text=linha[3]).pack()




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
    Button(screen3, height=2, width=15, text="Visualizar Artigos", command=visualizar_artigos).pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Button(screen3, height=2, width=15, text="Adicionar Artigos", command=adicionar_artigos).pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Button(screen3, height=2, width=18, text="Ver histórico de preços", command=ver_historico).pack()
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


def ver_historico():
    global screen81
    screen81 = Toplevel(screen)
    screen81.title("Histórico de preços")
    screen81.geometry("500x600")
    screen81.resizable(0, 0)
    screen81.propagate(0)
    


    Label(screen81, text="").pack()
    Label(screen81, text="").pack()
    Label(screen81, text="").pack()
    Label(screen81, text="").pack()
    Label(screen81, text="").pack()
    Label(screen81, text="").pack()
    Button(screen81, height=2, width=10, text="Filmes", command=preco_filmes).pack()
    Label(screen81, text="").pack()
    Label(screen81, text="").pack()
    Label(screen81, text="").pack()
    Button(screen81, height=2, width=10, text="Series", command=series_admin).pack()
    Label(screen81, text="").pack()
    Label(screen81, text="").pack()
    Label(screen81, text="").pack()
    Button(screen81, height=2, width=10, text="Documentários", command=documentarios_admin).pack()
    Label(screen81, text="").pack()
    Label(screen81, text="").pack()
    Label(screen81, text="").pack()


def preco_filmes():

    global screen82
    global id_ver_preco
    global Entry10 
    screen82 = Toplevel(screen)
    screen82.title("Filmes")
    screen82.geometry("1280x720")
    screen82.resizable(0, 0)
    screen82.propagate(0)
    id_ver_preco = DoubleVar()
    
    

    for linha in funcoes.ver_filmes_admin():
        Label(screen82, text=linha[0]).pack()
        Label(screen82, text="").pack()
        Label(screen82, text="ID: ").pack()
        Label(screen82, text=linha[1]).pack()
        Label(screen82, text="Preço: ").pack()
        Label(screen82, text=linha[2]).pack()
        Label(screen82, text="---------------").pack()
    Label(screen82, text="Digite o ID do produto que pretende ver o histórico de preço:").pack()
    Entry10 = Entry(screen82, textvariable=id_ver_preco)
    Entry10.pack()
    Button(screen82, height=2, width=15, text="Visualizar preços", command=ver_preco_antigo).pack()


def preco_series():

    global screen84
    global id_ver_preco
    global Entry20 
    screen84 = Toplevel(screen)
    screen84.title("Séries")
    screen84.geometry("1280x720")
    screen84.resizable(0, 0)
    screen84.propagate(0)
    id_ver_preco = DoubleVar()
    
    

    for linha in funcoes.ver_filmes_admin():
        Label(screen84, text=linha[0]).pack()
        Label(screen84, text="").pack()
        Label(screen84, text="ID: ").pack()
        Label(screen84, text=linha[1]).pack()
        Label(screen84, text="Preço: ").pack()
        Label(screen84, text=linha[2]).pack()
        Label(screen84, text="---------------").pack()
    Label(screen84, text="Digite o ID do produto que pretende ver o histórico de preço:").pack()
    Entry20 = Entry(screen84, textvariable=id_ver_preco)
    Entry20.pack()
    Button(screen84, height=2, width=15, text="Visualizar preços", command=ver_preco_antigo).pack()



def preco_documentario():

    global screen83
    global id_ver_preco
    global Entry30
    screen83 = Toplevel(screen)
    screen83.title("Documentários")
    screen83.geometry("1280x720")
    screen83.resizable(0, 0)
    screen83.propagate(0)
    id_ver_preco = DoubleVar()
    
    

    for linha in funcoes.ver_documentarios_admin():
        Label(screen83, text=linha[0]).pack()
        Label(screen83, text="").pack()
        Label(screen83, text="ID: ").pack()
        Label(screen83, text=linha[1]).pack()
        Label(screen83, text="Preço: ").pack()
        Label(screen83, text=linha[2]).pack()
        Label(screen83, text="---------------").pack()
    Label(screen83, text="Digite o ID do produto que pretende ver o histórico de preço:").pack()
    Entry30 = Entry(screen83, textvariable=id_ver_preco)
    Entry30.pack()
    Button(screen83, height=2, width=15, text="Visualizar preços", command=ver_preco_antigo).pack()


def ver_preco_antigo():
    global screen85
    screen85 = Toplevel(screen)
    screen85.title("Preços antigos")
    screen85.geometry("1280x720")
    screen85.resizable(0, 0)
    screen85.propagate(0)

    id_ver_preco_info = id_ver_preco.get()
    for linha in funcoes.ver_precos(id_ver_preco_info):
        Label(screen85, text="").pack()
        Label(screen85, text="Preço antigo: ").pack()
        Label(screen85, text=linha[0]).pack()
        Label(screen85, text="Alterado na data: ").pack()
        Label(screen85, text=linha[1]).pack()




def ver_estatisticas():
    global screen23
    screen23 = Toplevel(screen)
    screen23.title("Estatísticas")
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
    for linha in funcoes.return_artigos_total_preco():
        Label(screen25, text="Valor total dos artigos adicionados").pack()
        Label(screen25, text=linha[0], fg='blue').pack()
    for linha in funcoes.contar_preco():
        Label(screen25, text="Valor total dos artigos alugados").pack()
        Label(screen25, text=linha[0], fg='blue').pack()

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
    screen10.title("Adicionar Série")
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
    
    tipo_artigo.set('Série')
    Label(screen10, text="").pack()
    Label(screen10, text="Insira o nome da série que pretende adicionar:").pack()
    nome_entrada = Entry(screen10, textvariable=nome_artigo)
    nome_entrada.pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="Insira o realizador da série:").pack()
    realizador_entrada = Entry(screen10, textvariable=realizador)
    realizador_entrada.pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="Insira o ator principal da série:").pack()
    ator_entrada = Entry(screen10, textvariable=ator)
    ator_entrada.pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="Insira o número de horas que pretende que a série esteja disponível:").pack()
    horas_entrada = Entry(screen10, textvariable=horas_disp)
    horas_entrada.pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="Insira o preço da série:").pack()
    preco_entrada = Entry(screen10, textvariable=preco_artigo)
    preco_entrada.pack()
    Label(screen10, text="").pack()
    Button(screen10, text="Enviar", command=enviar_artigo).pack()




def add_documentario():
    global screen10
    screen8.destroy()
    screen10 = Toplevel(screen)
    screen10.title("Adicionar Documentário")
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
    
    tipo_artigo.set('Documentário')
    Label(screen10, text="").pack()
    Label(screen10, text="Insira o nome do documentário que pretende adicionar:").pack()
    nome_entrada = Entry(screen10, textvariable=nome_artigo)
    nome_entrada.pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="Insira o realizador do documentário:").pack()
    realizador_entrada = Entry(screen10, textvariable=realizador)
    realizador_entrada.pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="Insira o ator principal do documentário:").pack()
    ator_entrada = Entry(screen10, textvariable=ator)
    ator_entrada.pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="Insira o número de horas que pretende que o documentário esteja disponível:").pack()
    horas_entrada = Entry(screen10, textvariable=horas_disp)
    horas_entrada.pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="Insira o preço do documentário:").pack()
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
        


def visualizar_artigos():
    global screen40
    screen40 = Toplevel()
    screen40.title("Artigos")
    screen40.geometry("700x600")
    screen40.resizable(0, 0)
    screen40.propagate(0)

    Label(screen40, text="").pack()
    Label(screen40, text="").pack()
    Label(screen40, text="").pack()
    Label(screen40, text="").pack()
    Label(screen40, text="").pack()
    Label(screen40, text="").pack()
    Button(screen40, height=2, width=10, text="Filmes", command=filmes_admin).pack()
    Label(screen40, text="").pack()
    Label(screen40, text="").pack()
    Label(screen40, text="").pack()
    Button(screen40, height=2, width=10, text="Series", command=series_admin).pack()
    Label(screen40, text="").pack()
    Label(screen40, text="").pack()
    Label(screen40, text="").pack()
    Button(screen40, height=2, width=10, text="Documentários", command=documentarios_admin).pack()
    Label(screen40, text="").pack()
    Label(screen40, text="").pack()
    Label(screen40, text="").pack()
    Button(screen40, height=2, width=10, text="Voltar", command=voltar).pack()


def filmes_admin():
    global screen50
    global novo_preco
    global id_alterar
    global id_remover
    global Entry11
    global Entry22
    global Entry33 
    screen50 = Toplevel(screen)
    screen50.title("Filmes")
    screen50.geometry("1280x720")
    screen50.resizable(0, 0)
    screen50.propagate(0)
    novo_preco = DoubleVar()
    id_alterar = DoubleVar()
    id_remover = DoubleVar()
    
    

    for linha in funcoes.ver_filmes_admin():
        Label(screen50, text=linha[0]).pack()
        Label(screen50, text="").pack()
        Label(screen50, text="ID: ").pack()
        Label(screen50, text=linha[1]).pack()
        Label(screen50, text="Preço: ").pack()
        Label(screen50, text=linha[2]).pack()
        Label(screen50, text="Tempo disponível: ").pack()
        Label(screen50, text=linha[3]).pack()
        Label(screen50, text="---------------").pack()
    Label(screen50, text="Digite o ID do produto que pretende alterar de preço:").pack()
    Entry11 = Entry(screen50, textvariable=id_alterar)
    Entry11.pack()
    Label(screen50, text="Digite o novo preço que deseja atribuir ao produto:").pack()
    Entry22 = Entry(screen50, textvariable=novo_preco)
    Entry22.pack()
    Button(screen50, height=2, width=15, text="Alterar preço", command=alterar_preco).pack()
    Label(screen50, text="Digite o ID do produto que pretende remover:").pack()
    Entry33 = Entry(screen50, textvariable=id_remover)
    Entry33.pack()
    Button(screen50, height=2, width=15, text="Remover artigo", command=remover_artigo).pack()


def series_admin():
    global screen60
    global novo_preco
    global id_alterar
    global id_remover
    global Entry11
    global Entry22
    global Entry33 
    screen60 = Toplevel(screen)
    screen60.title("Séries")
    screen60.geometry("1280x720")
    screen60.resizable(0, 0)
    screen60.propagate(0)
    novo_preco = DoubleVar()
    id_alterar = DoubleVar()
    id_remover = DoubleVar()
    
    

    for linha in funcoes.ver_series_admin():
        Label(screen60, text=linha[0]).pack()
        Label(screen60, text="").pack()
        Label(screen60, text="ID: ").pack()
        Label(screen60, text=linha[1]).pack()
        Label(screen60, text="Preço: ").pack()
        Label(screen60, text=linha[2]).pack()
        Label(screen60, text="Tempo disponível: ").pack()
        Label(screen60, text=linha[3]).pack()
        Label(screen60, text="---------------").pack()
    Label(screen60, text="Digite o ID do produto que pretende alterar de preço:").pack()
    Entry11 = Entry(screen60, textvariable=id_alterar)
    Entry11.pack()
    Label(screen60, text="Digite o novo preço que deseja atribuir ao produto:").pack()
    Entry22 = Entry(screen60, textvariable=novo_preco)
    Entry22.pack()
    Button(screen60, height=2, width=15, text="Alterar preço", command=alterar_preco).pack()
    Label(screen60, text="Digite o ID do produto que pretende remover:").pack()
    Entry33 = Entry(screen60, textvariable=id_remover)
    Entry33.pack()
    Button(screen60, height=2, width=15, text="Remover artigo", command=remover_artigo).pack()


def documentarios_admin():
    global screen105
    global novo_preco
    global id_alterar
    global id_remover
    global Entry11
    global Entry22
    global Entry33 
    screen105 = Toplevel(screen)
    screen105.title("Documentários")
    screen105.geometry("1280x720")
    screen105.resizable(0, 0)
    screen105.propagate(0)
    novo_preco = DoubleVar()
    id_alterar = DoubleVar()
    id_remover = DoubleVar()
    
    

    for linha in funcoes.ver_documentarios_admin():
        Label(screen105, text=linha[0]).pack()
        Label(screen105, text="").pack()
        Label(screen105, text="ID: ").pack()
        Label(screen105, text=linha[1]).pack()
        Label(screen105, text="Preço: ").pack()
        Label(screen105, text=linha[2]).pack()
        Label(screen105, text="Tempo disponível: ").pack()
        Label(screen105, text=linha[3]).pack()
        Label(screen105, text="---------------").pack()
    Label(screen105, text="Digite o ID do produto que pretende alterar de preço:").pack()
    Entry11 = Entry(screen105, textvariable=id_alterar)
    Entry11.pack()
    Label(screen105, text="Digite o novo preço que deseja atribuir ao produto:").pack()
    Entry22 = Entry(screen105, textvariable=novo_preco)
    Entry22.pack()
    Button(screen105, height=2, width=15, text="Alterar preço", command=alterar_preco).pack()
    Label(screen105, text="Digite o ID do produto que pretende remover:").pack()
    Entry33 = Entry(screen105, textvariable=id_remover)
    Entry33.pack()
    Button(screen105, height=2, width=15, text="Remover artigo", command=remover_artigo).pack()



def alterar_preco():
    global screen
    id_alterar_info = id_alterar.get()
    novo_preco_info = novo_preco.get()


    funcoes.preco_antigo(id_alterar_info)
    funcoes.alterar_preco_admin(id_alterar_info, novo_preco_info)

    Entry11.delete(0, END)
    Entry22.delete(0, END)

def remover_artigo():
    global screen
    id_remover_info = id_remover.get()

    funcoes.remover_artigo_admin(id_remover_info)

    Entry33.delete(0, END)
        


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






