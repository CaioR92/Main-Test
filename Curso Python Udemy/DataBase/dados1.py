import sqlite3

def conectar_db():
    conexao = sqlite3.connect("Filmes.db")
    return conexao

def inserir_dados(nome, ano, nota):
    conexao = conectar_db()
    cursor = conexao.cursor()
    cursor.execute(
    """
    INSERT INTO Filmes(nome, ano, nota)
    VALUES (?, ?, ?)
               """, nome, ano, nota
    )
    conexao.commit()
    conexao.close()
    print("Dados inseridos na tabela")

# 3 - Listagem de dados
def obter_dados():
    conexao = conectar_db()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Filmes")
    dados = cursor.fetchall()
    cursor.close()
    return dados
    