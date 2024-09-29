import psycopg2
from psycopg2 import OperationalError

try:
    conn = psycopg2.connect(
        database = 'postgres',
        user = 'caioricardosilva',
        password = 'Vitoria8814.',
        host = 'localhost',
        port = '5432'
        )
    print("Conexão estabelecidade com sucesso")
except OperationalError as e:
        print(f'Erro: {e}')