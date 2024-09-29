import sqlite3

conexao = sqlite3.connect("Filmes.db")
cursor = conexao.cursor()

# 2 - Leitura de dados
dados = cursor.execute("SELECT * FROM Filmes")
print(dados.fetchall())