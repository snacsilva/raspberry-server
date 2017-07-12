# -*- coding: utf-8 -*-
import socket
import sqlite3
from datetime import datetime, date

# Host como 0.0.0.0 pega o ip da máquina e fica ouvindo nele
HOST = '0.0.0.0'
PORT = 7426  # Erro possível de ocorrer: "OSError: [Errno 98] Address already in use" só mudar aqui! =D

# AF_INET = IP ; SOCK_STREAM = TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

banco = sqlite3.connect('smart.db')
cursor = banco.cursor()

# Fica ouvindo no IP e porta definidos anteriormente
servidor.bind((HOST, PORT))
# Escuta até 10 clientes
servidor.listen(10)
print("Ouvindo em: ", (HOST, PORT))

# Objeto, conexão = aceitando conexão
(opcao, cliente) = servidor.accept()
# Exibe o array das informações do cliente
print("Comunicando com: ", opcao)

while True:

    # Recebe a informação com tamanho máximo definido e 
    # recebe apenas a mensagem enviada pelo cliente e formata a mensagen
    # deixando apenas a mensagem pura.
    info = opcao.recv(1024).decode()

    professor = info[5:-1]  # Slice/fatia - Pega a mensagem recebida da posição 5 até o final -1
    sala = info[:4]  # Slice/fatia - Pega a mensagem recebida do começo até a posição 4
    hora = datetime.now()  #
    dia = date.today()  # 0=Domingo, 1=Segunda, 2=Terça, 3=Quarta, 4=Quinta, 5=Sexta, 6=Sábado.
    # Pra pegar o nome da semana que tá salvo no banco já, só fazer a pesquisa pelo campo nome_dia. ^-^

    # Impressões no terminal do servidor apenas para mostrar como tá saindo cada informação e como está indo para a query.
    print("'--------------------------------------------------------------------'")
    print('Id do professor: ', professor)
    print('Sala: ', sala)
    print('Hora não formatada: ', hora)
    print('Hora formatada: ', hora.strftime('%H:%M:%S'))
    print('Dia da semana: ', dia.isoweekday())
    print("'--------------------------------------------------------------------'")

    # Verificando se as informações existem na base
    cursor.execute(
        'SELECT matricula, numero_cartao, sala, hora_inicio, id_dia AS dia '
        'FROM professor, cartao, sala, horario, dia_semana '
        'WHERE numero_cartao = ? OR matricula = ? '
        'AND '
        'sala = ? '
        'AND '
        '? BETWEEN hora_inicio AND hora_final '
        'AND dia = ?',
        (professor, professor, sala, hora.strftime("%H:%M:%S"), dia.isoweekday()))
    resultado = cursor.fetchall()

    # Impressões no terminal do servidor apenas para mostrar como está vindo o array da pesquisa.
    print("'--------------------------------------------------------------------'")
    print("Resultado: ")
    print(resultado)
    print("'--------------------------------------------------------------------'")

    if (resultado):

        opcao.send(b'OK\n')
        print("'--------------------------------------------------------------------'")
        print("O professor(a) está autorizado(a) a acessar a sala.")
        print("'--------------------------------------------------------------------'")

    else:

        opcao.send(b'REJECT\n')
        print("'--------------------------------------------------------------------'")
        print("O professor(a) não está autorizado(a) a acessar a sala.")
        print("O cartão ou a matrícula: " + professor + " ou não está cadastrado ou não está no seu "
                                                        "horário e dia de entrada na sala: " + sala + ".")
        print("'--------------------------------------------------------------------'")
