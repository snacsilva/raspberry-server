# -*- coding: utf-8 -*-
import socket
import _thread
import sqlite3

# Host como 0.0.0.0 pega o ip da máquina e fica ouvindo nele
HOST = '0.0.0.0'
PORT = 7374

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

print("Receiving from: %s" % option)

while True:

    #Recebe a informação com tamanho máximo definido e
    # recebe apenas a mensagem enviada pelo cliente
    info = option.recv(1024).decode()
    print(info[:4])
    print(info[5:])
    card_info = info[5:] #Pega a mensagem recebida da posição 5 até o final
    room_info = info[:4] #Pega a mensagem recebida do começo até a posição 4

    # Verificando se as informações existe na base
    cursor.execute('SELECT numero_cartao, description FROM card, room WHERE numero_cartao = ? and description = ?', (card_info, room_info))
    result = cursor.fetchall()

    print(result)

    if (result):

        option.send(b'OK\n')
        print(info)
        print("Done!")

    else:

        option.send(b'REJECT\n')
        print(info)
        print("Not this time! :(")


