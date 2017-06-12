# -*- coding: utf-8 -*-
import sqlite3

conexao = sqlite3.connect('smart.db')

print('Conexão com o banco realizada com sucesso!')

cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE `professor` ( 
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `rfid` INTEGER NOT NULL UNIQUE ,
    `matricula` TEXT NOT NULL UNIQUE );
    """)

cursor.execute("""

     CREATE TABLE `dia_semana` ( 
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
    `nome` TEXT NOT NULL UNIQUE ); 
""")

cursor.execute("""

     CREATE TABLE `sala` ( 
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
    `numero_sala` TEXT NOT NULL UNIQUE );
""")

cursor.execute("""

     CREATE TABLE `cartao` ( 
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
    `numero_cartao` TEXT NOT NULL UNIQUE );

""")

cursor.execute("""
   
     CREATE TABLE `hora_inicio` ( 
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
    `hora` TEXT NOT NULL UNIQUE
   );
    
""")

cursor.execute("""

     CREATE TABLE `hora_final` ( 
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
    `hora` TEXT NOT NULL UNIQUE
   );

""")

cursor.execute("""

     CREATE TABLE `check_informações` ( 
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
    `id_professor` REFERENCES professor NOT NULL, 
    `id_sala` REFERENCES sala NOT NULL, 
    `id_dia_semana` REFERENCES dia_semana NOT NULL,
    `hora_inicio` REFERENCES horario_inicio NOT NULL ,
    `hora_final` REFERENCES horario_final NOT NULL );
    
""")

print('Tabela criada com sucesso!')
