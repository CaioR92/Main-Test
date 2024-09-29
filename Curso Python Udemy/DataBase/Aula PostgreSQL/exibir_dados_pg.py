from conexao_postgre import conn

cursor_obj = conn.cursor()

cursor_obj.execute('SELECT * FROM "Filmes"')

result = cursor_obj.fetchall()

print(result)