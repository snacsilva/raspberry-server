# -*- coding: utf-8 -*-
import sqlite3

conexao = sqlite3.connect('smart.db')

print('Conexão com o banco realizada com sucesso!')

cursor = conexao.cursor()

cursor.execute("""
  INSERT INTO professor VALUES ('1','Silvio', 'DB12345')
        """)
cursor.execute("""
  INSERT INTO professor VALUES ('2','Rafael', 'DB55555')
        """)
cursor.execute("""
  INSERT INTO cartao VALUES ('1','5D84FDD8')
    """)
cursor.execute("""
  INSERT INTO cartao VALUES ('2','F5352C77')
        """)
cursor.execute("""
  INSERT INTO cartao_professor VALUES ('1','1','1', current_timestamp)
        """)
cursor.execute("""
  INSERT INTO cartao_professor VALUES ('2','2','2', current_timestamp)
            """)
cursor.execute("""
  INSERT INTO dia_semana VALUES ('1','Segunda-Feira')
            """)
cursor.execute("""
  INSERT INTO dia_semana VALUES ('2','Terça-Feira')
            """)
cursor.execute("""
  INSERT INTO dia_semana VALUES ('3','Quarta-Feira')
            """)
cursor.execute("""
  INSERT INTO dia_semana VALUES ('4','Quinta-Feira')
            """)
cursor.execute("""
  INSERT INTO dia_semana VALUES ('5','Sexta-Feira')
            """)
cursor.execute("""
  INSERT INTO dia_semana VALUES ('6','Sábado')
            """)
cursor.execute("""
  INSERT INTO dia_semana VALUES ('7','Domingo')
            """)
cursor.execute("""
  INSERT INTO sala VALUES ('1','LAB4')
        """)
cursor.execute("""
  INSERT INTO horario VALUES ('1','18:00:00','22:00:00')
        """)
cursor.execute("""
  INSERT INTO check_informacoes VALUES ('1','1','1','1','1','1')
        """)
cursor.execute("""
  INSERT INTO check_informacoes VALUES ('2','2','2','2','2','2')
        """)



# from datetime import date
# >>> hj = date.today()
# >>> dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
# >>> print "Hoje é", dias[hj.weekday()]
# Hoje é, Terça-feira


conexao.commit()

conexao.close()

print('Informações inseridas com sucesso!')