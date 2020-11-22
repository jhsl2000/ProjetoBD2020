import psycopg2
import psycopg2.extras

# Conexao a base de dados basica

import ui

def insere_novo_user(user_email, user_password, user_nome):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020")
        cursor = connection.cursor()

    except(Exception, psycopg2.Error):
        if (connection):
            print("Esse email ja tem conta criada! Insira outro email.")

    finally:
        # Closing database connection
        if(connection):
            cursor.close()
            connection.close()


def check_login(email_entry1, password_entry1):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020")
        cursor = connection.cursor()
        cursor.execute("SELECT utilizador.email, utlizador.password,"
                       "admin.utilizador_email FROM utilizador,"
                       "admin WHERE utilizador.email =%s AND utilizador.password = %s AND admin.utilizador_email = %s;",
                       (email_entry1, password_entry1, email_entry1))

        if cursor.rowcount == 1:
            return 'cliente' # codigo para cliente_login
        else:
            cursor.execute("SELECT utilizador.email, utlizador.password,"
                       "admin.utilizador_email FROM utilizador,"
                       "admin WHERE utilizador.email =%s AND utilizador.password = %s AND admin.utilizador_email = %s;",
                       (email_entry1, password_entry1, email_entry1))
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