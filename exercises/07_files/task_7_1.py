# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ospf_file = open('ospf.txt', 'r')
ospf_source = ospf_file.read()
ospf_file.close()
ospf_transformed = [line.split()[1:] for line in ospf_source.split('\n')][:-1]

output_template = '''
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}'''

for line in ospf_transformed:
    # print(line)
    prefix = line[0]
    ad_metric = line[1][1:-1]
    next_hop = line[3][:-1]
    last_update = line[4][:-1]
    outbound_interface = line[5]
    print(output_template.format(prefix, ad_metric, next_hop, last_update, outbound_interface))
