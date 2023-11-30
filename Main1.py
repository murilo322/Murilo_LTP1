import sqlite3

#Conectar-se a um banco de dados existente ou criar um novo

connection = sqlite3.connect('novo_db.db')

cursor = connection.cursor()

#Criar uma tabela

cursor.execute(
    'CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER)'
)

# Inserir dados na tabela
cursor.execute(
    "INSERT INTO usuarios (nome, idade) VALUES ('Maria', 13)"
)

# Fazer uma consulta de dados

cursor.execute(
    'SELECT * FROM usuarios'
)
rows = cursor.fetchall()
for row in rows:
    print(row)

connection.commit()
connection.close()