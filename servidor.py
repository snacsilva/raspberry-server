# -*- coding: utf-8 -*-
import socket
import _thread
import sqlite3

# Host como 0.0.0.0 pega o ip da máquina e fica ouvindo nele
HOST = '0.0.0.0'
PORT = 7685

# AF_INET = IP ; SOCK_STREAM = TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

banco = sqlite3.connect('smart.db')
cursor = banco.cursor()

#Fica ouvindo no IP e porta definidos anteriormente
server.bind((HOST, PORT))
#Escuta até 10 clientes
server.listen(10)
print("Listening on %s %s" % (HOST, PORT))

# Objeto, conexão = aceitando conexão
(option, client) = server.accept()

print("Receiving from: %s " % option)

while True:

    # Recebe a informação com tamanho máximo definido e
    # recebe apenas a mensagem enviada pelo cliente
    info = option.recv(1024).decode()
    print(info[:4])
    print(info[5:])
    card_info = info[5:] #Slice/fatia - Pega a mensagem recebida da posição 5 até o final
    room_info = info[:4] #Slice/fatia - Pega a mensagem recebida do começo até a posição 4


    # print(room_info + "room_info")
    # print("card_info" + card_info )

    if (info != "\n"):

        # Verificando se as informações existe na base
        cursor.execute('SELECT numero_cartao, description FROM card, room WHERE numero_cartao = ? AND description = ?',
                       (card_info, room_info))
        result = cursor.fetchall()

        print(result)

        if (result):

            option.send(b'OK\n')
            print(info + "if")
            print("Done!")

        else:

            option.send(b'REJECT\n')
            print(info + "ELSE")
            print("Not this time! :(")


    else:
        option.send(b'Enviando dados vazios. \n Conexao encerrada.\n')
        option.close()
