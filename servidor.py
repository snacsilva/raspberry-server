# -*- coding: utf-8 -*-
import socket
import _thread
import sqlite3
from datetime import time


# Host como 0.0.0.0 pega o ip da máquina e fica ouvindo nele
import datetime

HOST = '0.0.0.0'
PORT = 7444 #Erro possível de ocorrer: OSError: [Errno 98] Address already in use só mudar aqui! =D

# AF_INET = IP ; SOCK_STREAM = TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

banco = sqlite3.connect('smart.db')
cursor = banco.cursor()

#Fica ouvindo no IP e porta definidos anteriormente
servidor.bind((HOST, PORT))
#Escuta até 10 clientes
servidor.listen(10)
print("Listening on %s %s" % (HOST, PORT))

# Objeto, conexão = aceitando conexão
(opcao, cliente) = servidor.accept()

print("Receiving from: %s " % opcao)

while True:

    # Recebe a informação com tamanho máximo definido e
    # recebe apenas a mensagem enviada pelo cliente e formata a mensagen
    # deixando apenas a mensagem pura.
    info = opcao.recv(1024).decode()

    professor = info[5:-1] #Slice/fatia - Pega a mensagem recebida da posição 5 até o final -1
    sala = info[:4] #Slice/fatia - Pega a mensagem recebida do começo até a posição 4
    print(professor)
    print(sala)


    # Verificando se as informações existe na base
    cursor.execute('SELECT matricula, numero_cartao, sala, hora_inicio FROM professor, cartao, sala, horario '
                   'WHERE  (matricula = ? OR numero_cartao = ?) AND sala = ?', (professor, professor, sala))
    resultado = cursor.fetchall()

    print("Resultado: ")
    print(resultado)

    if (resultado):

        opcao.send(b'OK\n')
        print("'--------------------------------------------------------------------'")
        print("O professor(a) está autorizado(a) a acessar a sala.")
        print("'--------------------------------------------------------------------'")

    else:

        opcao.send(b'REJECT\n')
        print("'--------------------------------------------------------------------'")
        print("O professor(a) está autorizado(a) a acessar a sala.")
        print("O cartão ou a matrícula: " + professor + " não está salvo no nosso BD.")
        print("'--------------------------------------------------------------------'")
