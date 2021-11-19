#!/usr/bin/env python3
# -*- coding: utf-8 -*-

abc_en_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
abc_ru_up = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
abc_en_down = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
abc_ru_down = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
abc_num = '0123456789'


def shift_symbol(symbol, shift):
    if abc_en_up.find(symbol) != -1:
        index = abc_en_up.find(symbol)
        new_index = (((index + shift) % 28) + 28) % 28
        return abc_en_up[new_index]
    elif abc_en_down.find(symbol) != -1:
        index = abc_en_down.find(symbol)
        new_index = (((index + shift) % 28) + 28) % 28
        return abc_en_down[new_index]
    elif abc_ru_up.find(symbol) != -1:
        index = abc_ru_up.find(symbol)
        new_index = (((index + shift) % 33) + 33) % 33
        return abc_ru_up[new_index]
    elif abc_ru_down.find(symbol) != -1:
        index = abc_ru_down.find(symbol)
        new_index = (((index + shift) % 33) + 33) % 33
        return abc_ru_down[new_index]
    elif abc_num.find(symbol) != -1:
        index = abc_num.find(symbol)
        new_index = (((index + shift) % 10) + 10) % 10
        return abc_num[new_index]
    else:
        return symbol


def crypt_cesar(message, shift):
    result = ''
    for i in message:
        result += shift_symbol(i, shift)
    return result


def decrypt_cesar(message, shift):
    return crypt_cesar(message, -shift)


def all_decrypt_cesar(message):
    print('Все возможные расшифровки цезаря:')
    for i in range(1, 33):
        print(crypt_cesar(message, i))


def crypt_viginere(message, shift_message):
    result = ''
    for i in range(len(message)):
        shift = 0
        if isinstance(shift_message, str):
            shift = ord(shift_message[i % len(shift_message)])

        else:
            shift = shift_message[i % len(shift_message)]
        result += shift_symbol(message[i], shift)
    return result


def decrypt_viginere(message, shift_message):
    decrypt_shift_message = []
    for i in shift_message:
        decrypt_shift_message.append(-ord(i))
    return crypt_viginere(message, decrypt_shift_message)


if __name__ == "__main__":
    shift_cesar = int(input('Шаг шифровки цезаря: '))
    shift_viginere = input("строка шифровки вижинера: ")
    message = input("Сообщение для шифровки: ")

    # шифровка шифра цезаря
    crypt_message = crypt_cesar(message, shift_cesar)
    decrypt_message = decrypt_cesar(crypt_message, shift_cesar)
    print('Зашифрованное сообщение цезаря:', crypt_message)
    # all_decrypt_cesar(crypt_message)
    print('Расшифрованное сообщение цезаря:', decrypt_message)

    # шифровка шифра вижинера
    crypt_viginere_message = crypt_viginere(message, shift_viginere)
    print('Зашифрованное сообщение вижинера:', crypt_viginere_message)
    decrypt_viginere_message = decrypt_viginere(crypt_viginere_message, shift_viginere)
    print('Расшифрованное сообщение вижинера:', decrypt_viginere_message)
