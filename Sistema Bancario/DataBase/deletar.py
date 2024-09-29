import sqlite3

# 1- Conectando ao DB
conexao = sqlite3.connect("Banco.db")

# 2 - Criando Cursor
cursor = conexao.cursor()

# 3 - Exclusão de dados
id = (x, x)
cursor.execute(
    """
    DELETE FROM Banco
    WHERE ID in (?, ?)
    """,
    id
)
conexao.commit()

print("Dados excluídos com sucesso")