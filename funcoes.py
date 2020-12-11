import psycopg2
import psycopg2.extras


def insere_novo_user(email_info, password_info, nome_info):
    try:
        connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  port="5432",
                                  database="ProjetoBD2020v1")
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
                                      database="ProjetoBD2020v1")
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
                                      database="ProjetoBD2020v1")
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
                                      database="ProjetoBD2020v1")
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
                                      database="ProjetoBD2020v1")
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
                                      database="ProjetoBD2020v1")
        cursor = connection.cursor()
        cursor.execute("SELECT email FROM utilizador WHERE utilizador.email ='" +destinatario_info +"'")

        if cursor.rowcount == 1:
            cursor.execute("INSERT INTO mensagem (texto, assunto, utilizador_email) VALUES ('" +mensagem_info + "', '" +assunto_info + "', '" +destinatario_info + "')")
            connection.commit()
            print("Mensagem enviada")
            return 'mensagem_aceite'
        else:
            return 'erro'
    
    except (Exception, psycopg2.Error) as error:
        print("Error", error)
 
    finally:
        # Closing database connection
        if connection:
            cursor.close()
            connection.close()


def admin_ver_mensagens_utilizador(nome_utilizador_info):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020v1")
        cursor = connection.cursor()
        cursor.execute("SELECT email FROM utilizador WHERE email = '"+nome_utilizador_info +"' ")

        if cursor.rowcount == 1:
            cursor.execute("SELECT texto, assunto FROM mensagem where mensagem.utilizador_email = '"+nome_utilizador_info +"'")
            mensagem = cursor.fetchall()
            return mensagem
        else:
            return 0

    except (Exception, psycopg2.Error) as error:
        print("Error", error)


def admin_ver_todas_mensagens():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020v1")
        cursor = connection.cursor()
   
        cursor.execute("SELECT utilizador_email, assunto, texto FROM mensagem")
        mensagem = cursor.fetchall()
        return mensagem

    except (Exception, psycopg2.Error) as error:
        print("Error", error)


def addartigo(tipo_info, nome_info, horas_info, preco_info, realizador_info, ator_info):
    try:
        connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  port="5432",
                                  database="ProjetoBD2020v1")
        cursor = connection.cursor()
        #cursor.execute(" INSERT INTO Artigo (tipo, nome, realizador, ator, tempo_disponivel, preco, id) VALUES ('" +tipo_info+ "','" +nome_info +"','" +realizador_info +"','"+ator_info +"', horas_info, preco_info, '7')")
        cursor.execute("INSERT INTO artigo (id, nome, tipo, realizador, ator, tempo_disponivel, preco) VALUES (nextval('put_id'), %s, %s, %s, %s, %s, %s)", (nome_info, tipo_info, realizador_info, ator_info, horas_info, preco_info))    
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
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020v1")
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




def ver_filmes():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020v1")
        cursor = connection.cursor()
            
        cursor.execute("SELECT nome FROM artigo WHERE tipo = 'Filme'")
        filme = cursor.fetchall()
        return filme
       

    except (Exception, psycopg2.Error) as error:
        print("Error", error)



def ver_series():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020v1")
        cursor = connection.cursor()
            
        cursor.execute("SELECT nome FROM artigo WHERE tipo = 'Série'")
        serie = cursor.fetchall()
        return serie
       

    except (Exception, psycopg2.Error) as error:
        print("Error", error)




def ver_documentarios():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020v1")
        cursor = connection.cursor()
            
        cursor.execute("SELECT nome FROM artigo WHERE tipo = 'Documentário'")
        documentario = cursor.fetchall()
        return documentario
       

    except (Exception, psycopg2.Error) as error:
        print("Error", error)



def ver_descricao():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020v1")
        cursor = connection.cursor()

        cursor.execute("SELECT nome, tipo, realizador, ator, tempo_disponivel, preco FROM artigo WHERE nome = 'oo'")
        nomee = cursor.fetchall()
        return nomee
       

    except (Exception, psycopg2.Error) as error:
        print("Error", error)







def ver_filmes_admin():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020v1")
        cursor = connection.cursor()
            
        cursor.execute("SELECT nome, preco, tempo_disponivel FROM artigo WHERE tipo = 'Filme'")
        filmes = cursor.fetchall()
        return filmes
       

    except (Exception, psycopg2.Error) as error:
        print("Error", error)


def ver_series_admin():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020v1")
        cursor = connection.cursor()
            
        cursor.execute("SELECT nome, preco, tempo_disponivel FROM artigo WHERE tipo = 'Série'")
        series = cursor.fetchall()
        return series
       

    except (Exception, psycopg2.Error) as error:
        print("Error", error)


def ver_documentarios_admin():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020v1")
        cursor = connection.cursor()
            
        cursor.execute("SELECT nome, preco, tempo_disponivel FROM artigo WHERE tipo = 'Documentário'")
        documentarios = cursor.fetchall()
        return documentarios
       

    except (Exception, psycopg2.Error) as error:
        print("Error", error)

