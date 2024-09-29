from conexao_postgre import conn

cursor_obj = conn.cursor()

sql = """
    DELETE FROM "Filmes"
    WHERE "Id" = %s
"""

cursor_obj.execute(sql, (3, ))
conn.commit()
print("Dados Excluídos com sucesso")
conn.close()