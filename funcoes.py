import psycopg2
import psycopg2.extras

# Conexao a base de dados basica


def insere_novo_user(email_info, password_info, nome_info):
    try:
        connection = psycopg2.connect(user="postgres",
                                  password="rodmen27",
                                  host="localhost",
                                  port="5432",
                                  database="ProjetoBD2020v2")
        cursor = connection.cursor()
        cursor.execute(" INSERT INTO utilizador (email, password, nome, saldo) VALUES ('" +email_info +"','" +password_info +"','" +nome_info +"', '20')")
        print("Registado com sucesso")
        connection.commit()
    except (Exception, psycopg2.Error):
        if connection:
            print("Esse email ja tem conta criada! Insira outro email.")

    finally:
        # Closing database connection
        if connection:
            cursor.close()
            connection.close()


def confirma_novo_user(email_info, password_info):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="rodmen27",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020v2")
        cursor = connection.cursor()

        cursor.execute(" SELECT email, password FROM utilizador WHERE utilizador.email ='" +email_info +"' AND password ='" +password_info +"'")

        if cursor.rowcount == 1:
            return 'registado' # codigo para cliente_login

        else:
            return 0


    except (Exception, psycopg2.Error) as error:
        print("Error", error)
    finally:
        # closing database connection
        if(connection):
            cursor.close()
            connection.close()


def check_login(email_entry1, password_entry1):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="rodmen27",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020v2")
        cursor = connection.cursor()

        cursor.execute("SELECT email, password FROM utilizador WHERE utilizador.email ='" +email_entry1 +"' AND password ='" +password_entry1 +"'")

        if cursor.rowcount == 1:
            return 'cliente' # codigo para cliente_login

        else:
            cursor.execute("SELECT admin_email, pass FROM administrador WHERE administrador.admin_email ='" +email_entry1 +"' AND pass ='" +password_entry1 +"'")

            if cursor.rowcount == 1:
                return 'admin' # codigo para admin_login

            else:
                return 0

    except (Exception, psycopg2.Error) as error:
        print("Error", error)
    finally:
        # closing database connection
        if(connection):
            cursor.close()
            connection.close()


def add_saldo(saldo_email_info, saldo_quantia_info):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="rodmen27",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020v2")
        cursor = connection.cursor()

        cursor.execute("SELECT email FROM utilizador WHERE utilizador.email= '"+saldo_email_info +"'")

        if cursor.rowcount == 1:
            cursor.execute("UPDATE utilizador SET saldo = utilizador.saldo + %s WHERE email = '"+ saldo_email_info +"'", (saldo_quantia_info))
            print("Saldo atualizado")

        else:
            print("Email não existe")
            return 0

    except (Exception, psycopg2.Error) as error:
        print("Error", error)
        '''
        if connection:
            print("erro")
            print(saldo_email_info)
            print(saldo_quantia_info)
        '''
    finally:
        # Closing database connection
        if connection:
            cursor.close()
            connection.close()


def addartigo(tipo_info, nome_info, horas_info, preco_info, realizador_info, ator_info):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="rodmen27",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020v2")
        cursor = connection.cursor()

        cursor.execute(" INSERT INTO Artigo (tipo, nome, realizador, ator, tempo_disponivel, preco, id) VALUES ('" +tipo_info+ "','" +nome_info +"','" +realizador_info +"','"+ator_info +"', %f, %f, '7')", (horas_info, preco_info))
        print("Adicionado com sucesso")
        connection.commit()

    except (Exception, psycopg2.Error) as error:
        print(tipo_info)
        print(nome_info)
        print(horas_info)
        print(preco_info)
        print(realizador_info)
        print(ator_info)
        print("Esse artigo já existe.")

    finally:
        # Closing database connection
        if connection:
            cursor.close()
            connection.close()




def confirma_novo_artigo(nome_info, realizador_info):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="rodmen27",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020v2")
        cursor = connection.cursor()

        cursor.execute(" SELECT nome, realizador FROM artigo WHERE artigo.nome ='" +nome_info +"' AND artigo.realizador ='" +realizador_info +"'")

        if cursor.rowcount == 1:
            return 'confirma' # codigo para cliente_login

        else:
            return 0
            
    except (Exception, psycopg2.Error) as error:
        print("Error", error)
    finally:
        # closing database connection
        if(connection):
            cursor.close()
            connection.close()
