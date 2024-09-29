import sqlite3

conexao = sqlite3.connect("Filmes.db")
cursor = conexao.cursor()

# 1 - Atualizando dados
id = 1
cursor.execute(
    """
    UPDATE Filmes SET nota = ?
    WHERE id = ?
    """,
    ("8.0", id)
               )

conexao.commit()
print("Dados atualizados com sucesso.")