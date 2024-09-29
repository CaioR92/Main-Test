import sqlite3

# 2- Conectando ao DB
conexao = sqlite3.connect("Filmes.db")

# 2 - Criando Cursor
cursor = conexao.cursor()

# 3 - Criar tabela
cursor.execute(
    """
    CREATE TABLE Filmes(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        ano INTEGER NOT NULL,
        nota REAL NOT NULL
    );
               """)

# 4- Fecha conexão
conexao.close()
print("Tabela foi criada.")