from conexao_postgre import conn

cursor_obj = conn.cursor()

sql = """
    UPDATE "Filmes"
    SET "Nome" = %s,
    "Ano" = %s
    WHERE "Id" = %s
"""
cursor_obj.execute(sql, ("Zona de Interesse", 2023, 1))
conn.commit()
print("Dados atualizados com sucesso")
conn.close()