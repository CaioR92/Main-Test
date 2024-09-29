import sqlite3

# 1- Conectando ao DB
conexao = sqlite3.connect("Banco.db")

# 2 - Criando Cursor
cursor = conexao.cursor()

# 3 - Leitura de dados
dados = cursor.execute("SELECT * FROM Filmes")
print(dados.fetchall())