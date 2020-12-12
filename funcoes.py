import psycopg2
import psycopg2.extras
from passlib.hash import sha256_crypt


def insere_novo_user(email_info, password_encriptada, nome_info):
    try:
        connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  port="5432",
                                  database="ProjetoBD2020")
        cursor = connection.cursor()
        cursor.execute(" INSERT INTO utilizador (email, password, nome, saldo) VALUES ('" +email_info +"', crypt('password', gen_salt('bf')),'" +nome_info +"', '20')")
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


def confirma_novo_user(email_info, password_encriptado):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020")
        cursor = connection.cursor()
        sql = " SELECT email, password FROM utilizador WHERE utilizador.email ='" +email_info +"' AND password = crypt('password', password)"
        print(sql)
        cursor.execute(sql)

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
                                      database="ProjetoBD2020")
        cursor = connection.cursor()

        cursor.execute("SELECT email, password FROM utilizador WHERE utilizador.email ='" +email_entry1 +"' AND password = crypt('password', password)")

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
                                      database="ProjetoBD2020")
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
                                      database="ProjetoBD2020")
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


def envia_mensagem(destinatario_info, assunto_info, mensagem_info, email1):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020")
        cursor = connection.cursor()
        cursor.execute("SELECT email FROM utilizador WHERE utilizador.email ='" +destinatario_info +"'")

        if cursor.rowcount == 1:
            cursor.execute("INSERT INTO mensagem (texto, assunto, utilizador_email, administrador_email) VALUES ('" +mensagem_info + "', '" +assunto_info + "', '" +destinatario_info + "', '"+email1+"')")
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



def envia_mensagem_todos(mensagem_todos_info, assunto_todos_info, email1):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020")
        cursor = connection.cursor()
        cursor.execute("SELECT email FROM utilizador")
        utilizadores=cursor.fetchall()

        for linha in utilizadores:
            sql ="INSERT INTO mensagem (texto, assunto, utilizador_email,administrador_email) VALUES('"+mensagem_todos_info +"','"+assunto_todos_info +"','"+linha[0]+"', '"+email1+"')"
            print(sql)
            cursor.execute(sql)
            connection.commit()
        return 'mensagem_aceite'

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
                                      database="ProjetoBD2020")
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
                                      database="ProjetoBD2020")
        cursor = connection.cursor()
   
        cursor.execute("SELECT utilizador_email, assunto, texto FROM mensagem")
        mensagem = cursor.fetchall()
        return mensagem

    except (Exception, psycopg2.Error) as error:
        print("Error", error)


def admin_ver_mensagens_recebidas(email1):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020")
        cursor = connection.cursor()

        cursor.execute("SELECT utilizador_email, assunto, texto FROM caixa_de_entrada_admin WHERE administrador_admin_email ='"+email1 +"'")
        mensagem = cursor.fetchall()
        return mensagem

    except (Exception, psycopg2.Error) as error:
        print("Error", error)


def utilizador_ver_todas_mensagens(email1):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020")
        cursor = connection.cursor()

        cursor.execute("SELECT assunto, texto FROM mensagem WHERE utilizador_email = '"+email1+"'")
        user_mensagens = cursor.fetchall()
        return user_mensagens

    except (Exception, psycopg2.Error) as error:
        print("Error", error)


def addartigo(tipo_info, nome_info, horas_info, preco_info, realizador_info, ator_info):
    try:
        connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  port="5432",
                                  database="ProjetoBD2020")
        cursor = connection.cursor()
        #cursor.execute(" INSERT INTO Artigo (tipo, nome, realizador, ator, tempo_disponivel, preco, id) VALUES ('" +tipo_info+ "','" +nome_info +"','" +realizador_info +"','"+ator_info +"', horas_info, preco_info, '7')")
        cursor.execute("INSERT INTO artigo (id, nome, tipo, realizador, ator, tempo_disponivel, preco,administrador_admin_email,administrador_admin_email1) VALUES (nextval('put_id'), %s, %s, %s, %s, %s, %s, '1', '1')", (nome_info, tipo_info, realizador_info, ator_info, horas_info, preco_info))  
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
                                      database="ProjetoBD2020")
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
                                      database="ProjetoBD2020")
        cursor = connection.cursor()
            
        cursor.execute("SELECT nome, id FROM artigo WHERE tipo = 'Filme'")
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
                                      database="ProjetoBD2020")
        cursor = connection.cursor()
            
        cursor.execute("SELECT nome, id FROM artigo WHERE tipo = 'Série'")
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
                                      database="ProjetoBD2020")
        cursor = connection.cursor()
            
        cursor.execute("SELECT nome, id FROM artigo WHERE tipo = 'Documentário'")
        documentario = cursor.fetchall()
        return documentario
       

    except (Exception, psycopg2.Error) as error:
        print("Error", error)



def ver_descricao_filmes(id_filme_info):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020")
        cursor = connection.cursor()

        cursor.execute("SELECT nome, tipo, realizador, ator, tempo_disponivel, preco FROM artigo WHERE artigo.tipo = 'Filme' AND artigo.id = %s", [id_filme_info])
        nomee = cursor.fetchall()
        return nomee
       

    except (Exception, psycopg2.Error) as error:
        print("Error", error)


def utilizador_enviar_mensagem(mensagem_utilizador_info, assunto_utilizador_info, email1):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020")
        cursor = connection.cursor()
        cursor.execute("SELECT admin_email FROM administrador")
        admins=cursor.fetchall()

        for linha in admins:
            sql ="INSERT INTO caixa_de_entrada_admin (texto, assunto, administrador_admin_email, utilizador_email) VALUES('"+mensagem_utilizador_info +"','"+assunto_utilizador_info +"','"+linha[0]+"', '"+email1 +"')"
            print(sql)
            cursor.execute(sql)
            connection.commit()
        return 'mensagem_aceite'

    except (Exception, psycopg2.Error) as error:
        print("Error", error)

    finally:
        # Closing database connection
        if connection:
            cursor.close()
            connection.close()



def ver_descricao_series(id_serie_info):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020")
        cursor = connection.cursor()

        cursor.execute("SELECT nome, tipo, realizador, ator, tempo_disponivel, preco FROM artigo WHERE tipo = 'Série' AND id = %s", [id_serie_info])
        seriee = cursor.fetchall()
        return seriee
       

    except (Exception, psycopg2.Error) as error:
        print("Error", error)


def ver_descricao_documentarios(id_documentario_info):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020")
        cursor = connection.cursor()

        cursor.execute("SELECT nome, tipo, realizador, ator, tempo_disponivel, preco FROM artigo WHERE tipo = 'Documentário' AND id = %s", [id_documentario_info])
        documentarioo = cursor.fetchall()
        return documentarioo
       

    except (Exception, psycopg2.Error) as error:
        print("Error", error)


def ver_filmes_admin():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020")
        cursor = connection.cursor()
            
        cursor.execute("SELECT nome, id, preco, tempo_disponivel FROM artigo WHERE tipo = 'Filme'")
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
                                      database="ProjetoBD2020")
        cursor = connection.cursor()
            
        cursor.execute("SELECT nome, id, preco, tempo_disponivel FROM artigo WHERE tipo = 'Série'")
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
                                      database="ProjetoBD2020")
        cursor = connection.cursor()
            
        cursor.execute("SELECT nome, id, preco, tempo_disponivel FROM artigo WHERE tipo = 'Documentário'")
        documentarios = cursor.fetchall()
        return documentarios
       

    except (Exception, psycopg2.Error) as error:
        print("Error", error)


def alterar_preco_admin(id_alterar_info, novo_preco_info):
    try:
        connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  port="5432",
                                  database="ProjetoBD2020")
        cursor = connection.cursor()
        cursor.execute("UPDATE artigo SET preco = %s WHERE id = %s", [novo_preco_info, id_alterar_info])
        print("Alterado com sucesso")
        connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Erro.")


def seleciona_clientes(mensagem_todos_info, assunto_todos_info, destinatario_info,email1):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020")
        cursor = connection.cursor()
        sql ="INSERT INTO mensagem (texto, assunto, utilizador_email, administrador_admin_email) VALUES('"+mensagem_todos_info +"','"+assunto_todos_info +"','"+destinatario_info+"', '"+email1 +"')"
        print(sql)
        cursor.execute(sql)
        connection.commit()
        return 'mensagem_aceite'

    except (Exception, psycopg2.Error) as error:
        print("Error", error)

    finally:
        # Closing database connection
        if connection:
            cursor.close()
            connection.close()


def remover_artigo_admin(id_remover_info):
    try:
        connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  port="5432",
                                  database="ProjetoBD2020")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM artigo WHERE id = %s", [id_remover_info])
        print("Removido com sucesso")
        connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Erro.")


def total_utilizadores():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020")
        cursor = connection.cursor()
        sql ="SELECT COUNT(*) FROM utilizador"
        print(sql)
        cursor.execute(sql)
        total_users = cursor.fetchall()
        return total_users

    except (Exception, psycopg2.Error) as error:
        print("Error", error)

    finally:
        # closing database connection
        if (connection):
            cursor.close()
            connection.close()


def total_artigos():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020")
        cursor = connection.cursor()
        sql ="SELECT COUNT(*) FROM artigo"
        print(sql)
        cursor.execute(sql)
        total_artigo= cursor.fetchall()
        return total_artigo

    except (Exception, psycopg2.Error) as error:
        print("Error", error)

    finally:
        # closing database connection
        if (connection):
            cursor.close()
            connection.close()


def return_clientes():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020")
        cursor = connection.cursor()

        sql = "SELECT (nome, email) FROM utilizador"
        print(sql)
        cursor.execute(sql)

        utilizadores = cursor.fetchall()
        return utilizadores

    except (Exception, psycopg2.Error) as error:
        print("Error", error)
    finally:
        # closing database connection
        if (connection):
            cursor.close()
            connection.close()


def return_artigos_total_preco():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020")
        cursor = connection.cursor()
        sql ="SELECT SUM(preco) FROM artigo"
        print(sql)
        cursor.execute(sql)
        total_artigo = cursor.fetchall()
        return total_artigo

    except (Exception, psycopg2.Error) as error:
        print("Error", error)

    finally:
        # closing database connection
        if (connection):
            cursor.close()
            connection.close()

def preco_antigo(id_alterar_info):
    try:
        connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  port="5432",
                                  database="ProjetoBD2020")
        cursor = connection.cursor()
        #cursor.execute("INSERT INTO hist_preco (id, precos) SELECT (id, preco) FROM artigos WHERE id = %s", [id_alterar_info])
        cursor.execute("SELECT id, preco FROM artigo WHERE id = %s", [id_alterar_info])
        filmes = cursor.fetchall()
        for linha in filmes:
            cursor.execute("INSERT INTO hist_preco (id_preco, id, precos, data) VALUES (nextval('put_id_preco'), %s, %s, CURRENT_TIMESTAMP)", [linha[0], linha[1]])
        
        connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Erro.")



def ver_precos(id_ver_preco_info):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020")
        cursor = connection.cursor()
            
        cursor.execute("SELECT precos, data FROM hist_preco WHERE id = %s", [id_ver_preco_info])
        precos_antigos = cursor.fetchall()
        return precos_antigos

    except (Exception, psycopg2.Error) as error:
        print("Error", error)




def alugar(id_alugar_info, email1):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020")
        cursor = connection.cursor()
        
        
        cursor.execute("SELECT preco FROM artigo WHERE id = %s", [id_alugar_info])       
        preco_now = cursor.fetchall()
        for linha in preco_now:
            cursor.execute("UPDATE utilizador SET saldo = (saldo - %s) WHERE utilizador.email = '"+ email1 +"'", [linha[0]])
            
            cursor.execute("SELECT saldo FROM utilizador WHERE email = '"+ email1 +"'")       
            saldo_now = cursor.fetchone()
            if(saldo_now[0] >= 0):
                cursor.execute("SELECT id, nome, tipo, tempo_disponivel FROM artigo WHERE id = %s", [id_alugar_info])     
                alug = cursor.fetchall()
                for linha in alug:
                    cursor.execute("INSERT INTO biblioteca (id_b, nome_b, tipo_b, data_alug, total_artigos, tempo_disp, email_ut, utilizador_email) VALUES (%s, %s, %s, CURRENT_TIMESTAMP, nextval('add_artigo'), %s,  '"+ email1 +"', '"+ email1 +"')", [linha[0], linha[1], linha[2], linha[3]])          
                print('Alugado com sucesso!')
            else:
                print('Não tem saldo suficiente.')
                cursor.execute("SELECT preco FROM artigo WHERE id = %s", [id_alugar_info])       
                preco_agora = cursor.fetchall()
                for linha in preco_agora:
                    cursor.execute("UPDATE utilizador SET saldo = (saldo + %s) WHERE utilizador.email = '"+ email1 +"'", [linha[0]])
            
        connection.commit()


    except (Exception, psycopg2.Error) as error:
        print("Error", error)

def ver_filmes_comprados(email1):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020")
        cursor = connection.cursor()
            
        cursor.execute("SELECT nome_b, tipo_b, data_alug, tempo_disp FROM biblioteca WHERE tipo_b = 'Filme' AND email_ut = '"+ email1 +"'")
        filmes_comprados = cursor.fetchall()
        return filmes_comprados
       

    except (Exception, psycopg2.Error) as error:
        print("Error", error)

def ver_series_compradas(email1):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020")
        cursor = connection.cursor()
            
        cursor.execute("SELECT nome_b, tipo_b, data_alug, tempo_disp FROM biblioteca WHERE tipo_b = 'Série' AND email_ut = '"+ email1 +"'")
        series_comprados = cursor.fetchall()
        return series_comprados
       

    except (Exception, psycopg2.Error) as error:
        print("Error", error)



def ver_documentarios_comprados(email1):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020")
        cursor = connection.cursor()
            
        cursor.execute("SELECT nome_b, tipo_b, data_alug, tempo_disp FROM biblioteca WHERE tipo_b = 'Documentário' AND email_ut = '"+ email1 +"'")
        documentarios_comprados = cursor.fetchall()
        return documentarios_comprados

    except (Exception, psycopg2.Error) as error:
        print("Error", error)


def pesquisar_titulo(titulo_pesquisa_info):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020")
        cursor = connection.cursor()

        sql = "SELECT nome, tipo, realizador, ator, tempo_disponivel, preco FROM artigo WHERE artigo.nome = '"+ titulo_pesquisa_info +"'"
        print(sql)
        cursor.execute(sql)
        titulos = cursor.fetchall()
        return titulos

    except (Exception, psycopg2.Error) as error:
        print("Error", error)


def pesquisar_ator(ator_pesquisa_info):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020")
        cursor = connection.cursor()

        sql = "SELECT nome FROM artigo WHERE artigo.ator = '"+ ator_pesquisa_info +"'"
        print(sql)
        cursor.execute(sql)
        ator1 = cursor.fetchall()
        return ator1

    except (Exception, psycopg2.Error) as error:
        print("Error", error)


def pesquisar_realizador(realizador_pesquisa_info):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020")
        cursor = connection.cursor()

        sql = "SELECT nome FROM artigo WHERE artigo.realizador = '"+ realizador_pesquisa_info +"'"
        print(sql)
        cursor.execute(sql)
        realizador1 = cursor.fetchall()
        return realizador1

    except (Exception, psycopg2.Error) as error:
        print("Error", error)


def pesquisar_preco(preco_pesquisa_info):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="ProjetoBD2020")
        cursor = connection.cursor()

        cursor.execute("SELECT nome, preco FROM artigo WHERE artigo.preco <= %s ", [preco_pesquisa_info])
        preco1 = cursor.fetchall()
        return preco1

    except (Exception, psycopg2.Error) as error:
        print("Error", error)
