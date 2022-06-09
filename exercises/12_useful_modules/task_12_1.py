# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

import subprocess

#result = subprocess.run(['ping', '-c', '3', '-n', '8.8.8.8'], stdout=subprocess.PIPE)
#result = subprocess.run(['ping', '-c', '3', '-n', '8.8.8.8'], stdout=subprocess.DEVNULL)
#print(result.stdout.decode('utf-8'))
#print(result.stdout)
#print(result.returncode)

def ping_ip_addresses(ip_addr_list):
    available_ip = []
    unavailable_ip = []
    for i in ip_addr_list:
        result = subprocess.run(['ping', '-c', '3', '-n', i], stdout=subprocess.DEVNULL)
        if result.returncode == 0:
            available_ip.append(i)
        else:
            unavailable_ip.append(i)
    return(available_ip, unavailable_ip)

print(ping_ip_addresses(['8.8.8.8','77.88.8.8','93.125.15.1']))
