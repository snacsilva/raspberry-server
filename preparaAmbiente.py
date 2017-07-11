# -*- coding: utf-8 -*-
import sqlite3
import datetime

conexao = sqlite3.connect('smart.db')

print('Conexão com o banco realizada com sucesso!')

cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE `professor` ( 
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `nome` TEXT NOT NULL,
    `matricula` TEXT NOT NULL UNIQUE );
    """)

cursor.execute("""

     CREATE TABLE `cartao` ( 
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
    `numero_cartao` TEXT NOT NULL UNIQUE );
""")

cursor.execute("""

  CREATE TABLE `cartao_professor`(
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  `id_professor` INTEGER NOT NULL,
  `id_cartao` INTEGER NOT NULL,
  `info_salvo` TIMESTAMP NOT NULL DEFAULT current_timestamp,
  FOREIGN KEY (id_professor) REFERENCES professor(id),
  FOREIGN KEY (id_cartao) REFERENCES cartao(id)
  
  );


""")

cursor.execute("""

     CREATE TABLE `dia_semana` ( 
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
    `nome_dia` TEXT NOT NULL UNIQUE ); 
""")

cursor.execute("""

     CREATE TABLE `sala` ( 
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
    `sala` TEXT NOT NULL UNIQUE );
""")


cursor.execute("""
   
     CREATE TABLE `horario` ( 
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
    `hora_inicio` TIMESTAMP NOT NULL ,
    `hora_final`  TIMESTAMP NOT NULL );
    
""")


cursor.execute("""

    CREATE TABLE `check_informacoes` ( 
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
    `id_cartao_professor` INTEGER NOT NULL, 
    `id_sala` INTERGER NOT NULL, 
    `id_dia_semana` INTEGER NOT NULL,
    `id_hora_inicio` INTEGER NOT NULL ,
    `id_hora_final` INTEGER NOT NULL,
    FOREIGN KEY(id_cartao_professor) REFERENCES cartao_professor(id),
    FOREIGN KEY(id_sala) REFERENCES sala(id),
    FOREIGN KEY(id_dia_semana) REFERENCES dia_semana(id),
    FOREIGN KEY(id_hora_inicio) REFERENCES horario(id),
    FOREIGN KEY(id_hora_final) REFERENCES hora(id)
    );
    
""")



conexao.close()

print('Tabelas criadas com sucesso!')

