import psycopg2
import psycopg2.extras

connection = psycopg2.connect("host=localhost dbname=testes user=postgres password=postgres")
cursor = connection.cursor()
cursor.execute(" INSERT INTO utilizador (nome, idade) VALUES ('antonio', 10)")
cursor.execute("SELECT * FROM utilizador;")

print("Registado com sucesso")

for linha in cursor.fetchall():
    nome, idade = linha
    print (linha)

connection.commit()
cursor.close()
connection.close()