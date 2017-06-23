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

     CREATE TABLE `card` ( 
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
    `numero_cartao` TEXT NOT NULL UNIQUE );
""")

cursor.execute("""

  CREATE TABLE `card_professor`(
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  `id_professor` INTEGER NOT NULL,
  `id_card` INTEGER NOT NULL,
  FOREIGN KEY (id_professor) REFERENCES professor(id),
  FOREIGN KEY (id_card) REFERENCES card(id)
  
  );


""")

cursor.execute("""

     CREATE TABLE `day_week` ( 
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
    `name_day` TEXT NOT NULL UNIQUE ); 
""")

cursor.execute("""

     CREATE TABLE `room` ( 
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
    `description` TEXT NOT NULL UNIQUE );
""")


cursor.execute("""
   
     CREATE TABLE `start_time` ( 
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
    `time` TEXT NOT NULL UNIQUE
   );
    
""")

cursor.execute("""

     CREATE TABLE `final_hour` ( 
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
    `time` TEXT NOT NULL UNIQUE
   );

""")

cursor.execute("""

    CREATE TABLE `check_informacoes` ( 
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
    `id_card_professor` INTEGER NOT NULL, 
    `id_room` INTERGER NOT NULL, 
    `id_day_week` INTEGER NOT NULL,
    `id_start_time` INTEGER NOT NULL ,
    `id_final_time` INTEGER NOT NULL,
    FOREIGN KEY(id_card_professor) REFERENCES card_professor(id),
    FOREIGN KEY(id_room) REFERENCES room(id),
    FOREIGN KEY(id_day_week) REFERENCES day_week(id),
    FOREIGN KEY(id_start_time) REFERENCES start_time(id),
    FOREIGN KEY(id_final_time) REFERENCES final_time(id)
    );
    
""")

conexao.close()

print('Tabelas criadas com sucesso!')
