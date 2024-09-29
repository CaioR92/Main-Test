import sqlite3

conexao = sqlite3.connect("Filmes.db")
cursor = conexao.cursor()

# 2 - Exclusão de dados
id = (1, 2)
cursor.execute(
    """
    DELETE FROM Filmes
    WHERE ID in (?, ?)
    """,
    id
)
conexao.commit()

print("Dados excluídos com sucesso")