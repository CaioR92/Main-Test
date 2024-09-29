import sqlite3

# 1- Criando DB
conexao = sqlite3.connect("Banco.db")

# 2- Conectando ao DB
conexao = sqlite3.connect("Banco.db")

# 2 - Criando Cursor
cursor = conexao.cursor()

# 3 - Criar tabela
cursor.execute(
    """
    CREATE TABLE Cliente(
        id INTEGER NOT NULL PRIMARY KEY,
        nome TEXT NOT NULL,
        cpf UNIQUE NOT NULL,
        data_nascimento DATE NOT NULL,
        endereco TEXT NOT NULL 
    );
               """)

cursor.execute(
    """
    CREATE TABLE Conta(
        id INTEGER NOT NULL PRIMARY KEY,
        cliente_id INTEGER NOT NULL,
        nro_conta TEXT NOT NULL,
        agencia INTEGER NOT NULL,
        saldo REAL DEFAULT 0,
        tipo_conta TEXT NOT NULL,
        data_criacao DATE NOT NULL,
        FOREIGN KEY (cliente_id) REFERENCES Cliente (id)
    );
               """)

cursor.execute(
    """
    CREATE TABLE ContaCorrente(
        conta_id INTEGER NOT NULL PRIMARY KEY,
        limite_diario INTEGER DEFAULT 0,
        limite_saque REAL DEFAULT 0,
        FOREIGN KEY (conta_id) REFERENCES Conta(id)
    );
               """)

cursor.execute(
    """
    CREATE TABLE Transacoes(
        id INTEGER NOT NULL PRIMARY KEY,
        conta_id INTEGER NOT NULL,
        tipo_transacao TEXT NOT NULL,
        valor REAL NOT NULL,
        data_tran DATE NOT NULL,
        FOREIGN KEY (conta_id) REFERENCES Conta(id)
    );
               """)

cursor.execute(
    """
    CREATE TABLE HistoricoTransacoes(
        id INTEGER NOT NULL PRIMARY KEY,
        conta_id INTEGER NOT NULL,
        transacao_id INTEGER NOT NULL,
        FOREIGN KEY (conta_id) REFERENCES Conta(id),
        FOREIGN KEY (transacao_id) REFERENCES Transacoes(id)
    );
               """)

# 4- Fecha conexão
conexao.close()
print("Tabela foi criada.")