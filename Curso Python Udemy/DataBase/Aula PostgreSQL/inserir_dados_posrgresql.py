from conexao_postgre import conn

cursor_obj = conn.cursor()

filmes = [('A Pele que Habito', 2020, 9.0),
          ('Kaibutsu', 2023, 9.5),
          ('Anatomia de uma Queda', 2023, 10.0),
          ('La Chimera', 2023, 9.0)]

for filme in filmes:
    cursor_obj.execute(
        """
        INSERT INTO "Filmes"("Nome", "Ano", "Nota")
        VALUES (%s, %s, %s)
    """, filme
    )
    
conn.commit()
print("Dados inseridos com sucesso!")
conn.close()