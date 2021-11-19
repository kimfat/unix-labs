#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import threading

HOST = '127.0.0.1'
PORT = 2711
BIND = (HOST, PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, 0))

name = input("Введите имя: ")
sock.sendto(f'\n{name} в чате!'.encode(), BIND)


def get():
    while True:
        data = sock.recv(1024)
        print(data.decode('UTF-8'))


trhread = threading.Thread(target=get)
trhread.start()
while True:
    msg = input("Вы сообщаете: ")
    sock.sendto(f'{name} сообщает: {msg}'.encode(), BIND)
