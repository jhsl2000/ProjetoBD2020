import psycopg2
import psycopg2.extras


def insere_novo_user(email_info, password_info, nome_info):
    try:
        connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  port="5432",
                                  database="ProjetoBD2020v3")
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
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020v3")
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
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020v3")
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
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020v3")
        cursor = connection.cursor()
        cursor.execute("Select email from utilizador where utilizador.email= '"+saldo_email_info +"'")

        if cursor.rowcount == 1:
            cursor.execute("update utilizador set saldo = (saldo + %s) where email = '"+ saldo_email_info +"'", [saldo_quantia_info])
            print("Saldo atualizado")
            print(saldo_quantia_info)
            connection.commit()
            return 'confirma'
        else:
            print("Email não existe")


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


def consulta_saldo(email1):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020v3")
        cursor = connection.cursor()
        cursor.execute("Select saldo  from utilizador where utilizador.email= '"+email1 +"'")

        saldo = cursor.fetchall()

        return saldo

    except (Exception, psycopg2.Error) as error:
        print("Error", error)

    finally:
        # Closing database connection
        if connection:
            cursor.close()
            connection.close()


def envia_mensagem(destinatario_info, assunto_info, mensagem_info):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020v3")
        cursor = connection.cursor()
        cursor.execute("SELECT email FROM UTILIZADOR WHERE email ='"+destinatario_info+"'")

        if cursor.rowcount == 1:
            cursor.execute("INSERT INTO mensagem (texto, assunto) VALUES ('"+mensagem_info+"', '"+assunto_info+"')")
            connection.commit()
            return "mensagem_aceite"

    except (Exception, psycopg2.Error) as error:
        print("Error", error)

    finally:
        # Closing database connection
        if connection:
            cursor.close()
            connection.close()
