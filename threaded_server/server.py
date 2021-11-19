#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import threading


def chat(client):
    while True:
        try:
            message = client.recv(1024)
            for j in clients:
                j.send(message)
            file = open('log.txt', mode='a')
            file.write(str(message))
            file.write('\n')
            file.close()
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            name = names[index]
            names.remove(nickname)
            for i in clients:
                i.send(f'{name} отключился!'.encode())

            break


clients = []
names = []
host = '127.0.0.1'
port = 2711
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

while True:
    client, address = server.accept()
    print(f"Подключение:  {str(address)}")
    client.send('wrt_nm'.encode())
    nickname = client.recv(1024).decode()
    names.append(nickname)
    clients.append(client)
    print(f"подключен {nickname}")
    for client in clients:
        client.send(f"{nickname} подключился".encode())
    client.send('Соединение установлено'.encode())

    thread = threading.Thread(target=chat, args=(client,))
    thread.start()
