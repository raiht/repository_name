# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_input = input('ввод IP-сети: ')
ip1, ip2, ip3, bufer = ip_input.split('.')
ip4, mask = bufer.split('/')

ip = ip_input.split('/')[0].split('.')
ip1, ip2, ip3, ip4 = [e.ljust(10) for e in ip]
ip1b, ip2b, ip3b, ip4b = [bin(int(e)).lstrip('0b').rjust(8, '0').ljust(10) for e in ip]
print('Network: ')
print(f'{ip1}{ip2}{ip3}{ip4}\n'
      f'{ip1b}{ip2b}{ip3b}{ip4b}')
print()

mask_row = int(mask) * '1' + (32 - int(mask)) * '0'
ms = [mask_row[i * 8: (i + 1) * 8] for i in range(4)]
ms1, ms2, ms3, ms4 = [str(int(e, 2)).ljust(10) for e in ms]  # [e.ljust(10) for e in ms]
ms1b, ms2b, ms2b, ms4b = [e.ljust(10) for e in ms]  # [bin(int(e)).lstrip('0b').rjust(8, '0').ljust(10) for e in ms]
print('Mask: ')
print('/' + str(mask))
print(f'{ms1}{ms2}{ms3}{ms4}\n'
      f'{ms1b}{ms2b}{ms2b}{ms4b}')
