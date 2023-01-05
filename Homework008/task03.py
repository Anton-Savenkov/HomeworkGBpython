"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
"""

from sys import exit

class Division_by_zero(Exception):
    def __init__(self, text):
        self.text = text
        exit('Делить на ноль нельзя')

user_num = input('Введите число не равное нулю: ')

try:
    user_num = int(user_num)
    if user_num == 0:
        raise Division_by_zero('Вы ввели ноль')
except ValueError:
    print('Вы ввели не число')
except Division_by_zero as err:
    print(err)
else:
    print(f'Деление воозможно, вы ввели число {user_num}')