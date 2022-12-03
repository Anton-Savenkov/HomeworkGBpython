"""Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия. Для выполнения расчета для
конкретных значений необходимо запускать скрипт с параметрами."""

from sys import argv

script_name, worked_hours, hour_price, prem = argv

try:
    a = float(worked_hours)
    b = float(hour_price)
    c = float(prem)
    payroll = a * b + c
except ValueError:
    print('Введены неверные значения')

print("Имя скрипта: ", script_name)
print("Колличество отработанных часов: ", worked_hours)
print("Стооимость одногго часа рабочей смены: $ ", hour_price)
print("Размер премии: $ ", prem)
print(" Размеер заработной платы сотрудника: $ ", payroll)
