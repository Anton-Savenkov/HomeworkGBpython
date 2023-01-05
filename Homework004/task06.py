"""Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении
числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено."""

from itertools import count
from itertools import cycle

start_num_generate = int(input('Введите целое число,'
                               ' с которого начнется генерация чисел: '))

finish_num_generate = int(input('Введите целое число, до которого '
                                'будеет происхоодить процесс генерации: '))


def num_generate(start_num, finish_num):
    """Функция генерирующая целые числа, начиная с указанного и до
    указанного """
    for el in count(start_num):
        if el <= finish_num:
            print(el)
        else:
            break


num_generate(start_num_generate, finish_num_generate)

count_repeat = int(input('Введите колличество повторов, '
                         'для выхода из цикла: '))

day_week_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
                 'Friday', 'Saturday']


def generate_replace(input_list, count_var):
    """Функция повторяющий элементы пеередоваемого в нее списка,
    указанное коллество раз, определенного заранее и переданного в функцию
    в качестве аргумента."""
    i = 1
    for el in cycle(input_list):
        if i <= count_var:
            print(el)
            i += 1
        else:
            break


generate_replace(day_week_list, count_repeat)
