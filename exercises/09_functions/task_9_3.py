# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename):
    access = {}
    trunk = {}
    port_conf = []
    with open(config_filename, 'r') as f:
        array = f.readlines()
        for i in range(len(array)):
            if 'access vlan' in array[i]:
                access[array[i-2].split()[1]] = int(array[i].split()[-1])
            elif 'trunk allowed' in array[i]:
                trunk[array[i-2].split()[1]] = [int(i) for i in array[i].split()[-1].split(',')]
    return(access, trunk)

#print(get_int_vlan_map('config_sw1.txt'))
