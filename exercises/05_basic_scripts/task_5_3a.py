# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

interface_mode = input('Введите режим работы интерфейса (access/trunk): ')
interface_number = input('Введите тип и номер интерфейса: ')
if interface_mode == 'access':
	vlan_list = input('Введите номер VLAN:')
else:
	vlan_list = input('Введите разрешенные VLANы:')
print()

print(f'interface {interface_number}')
if interface_mode == 'access':
	for e in access_template:
		if e == "switchport access vlan {}":
			print(e.format(vlan_list))
		else:
			print(e)
elif interface_mode == 'trunk':
	for e in trunk_template:
		if e == 'switchport trunk allowed vlan {}':
			print(e.format(vlan_list))
		else:
			print(e)
