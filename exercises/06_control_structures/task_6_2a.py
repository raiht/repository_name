# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_adress = input('ввод IP-адреса: ')
try:
    ip_adress_list = [int(e) for e in ip_adress.split('.')]

    if (all([e in ['.', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] for e in ip_adress]) and len(ip_adress_list) == 4 and all([0 <= e <= 255 for e in ip_adress_list])):
        if 1 <= ip_adress_list[0] <= 223:
            print('unicast')
        elif 224 <= ip_adress_list[0] <= 239:
            print('multicast')
        elif ip_adress == '255.255.255.255':
            print('local broadcast')
        elif ip_adress == '0.0.0.0':
            print('unassigned')
        else:
            print('unused')
    else:
        print('Неправильный IP-адрес')
except Exception:
    print('Неправильный IP-адрес')
