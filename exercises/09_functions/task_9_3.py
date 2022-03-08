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
        for line in f.readlines():
            if line.startswith('interface FastEthernet'):
                port_conf.append(line)
            elif ('access vlan' in line) or ('trunk allowed' in line):
                port_conf.append(line) 
    return(port_conf)


print(get_int_vlan_map('config_sw1.txt'))


"""
interface FastEthernet0/0
 switchport mode access
 switchport access vlan 10
 duplex auto
!
interface FastEthernet0/1
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100,200
 switchport mode trunk
 duplex auto

"""
