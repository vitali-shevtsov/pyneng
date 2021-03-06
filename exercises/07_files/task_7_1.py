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

template = """{:22}{}
{:22}{}
{:22}{}
{:22}{}
{:22}{}"""

with open('ospf.txt') as f:
    for line in f:
        prefix = line.split()[1]
        metric = line.split()[2].strip('[]')
        nexthop= line.split()[4].strip(',')
        update = line.split()[5].strip(',')
        interf = line.split()[6]
        print(template.format('Prefix',prefix,'AD/Metric',metric,'Next-Hop', nexthop,'Last update',update, 'Outbound Interface', interf))
