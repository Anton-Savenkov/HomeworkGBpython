"""Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры памяти,
оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ,
что вы сделали и чего удалось добиться
Описания нужно делать в виде docstrings"""

from memory_profiler import profile

@profile()
def div_func02(num_a, num_b):
    """ Функция возвращает результат деления числа A на число B
    и остаток от деления"""
    return divmod(num_a, num_b)

print(div_func02(15, 3))

"""Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     8     18.1 MiB     18.1 MiB           1   @profile()
     9                                         def div_func02(num_a, num_b):
    10                                             Функция возвращает результат деления числа A на число B
    11                                             и остаток от деления
    12     18.1 MiB      0.0 MiB           1       return divmod(num_a, num_b)
    """

@profile()
def div_funk01(num_a, num_b):
    """
    Функция возвращает результат деления числа A на число B
    :param num_a: аргумет - делимое
    :param num_b: аргумент - делитель
    :return: результат деления / информация об ошибке
    """
    try:
        result = (int(num_a / num_b), num_a % num_b)
        return result
    except ZeroDivisionError:
        return print('Делить на 0 нельзя')

print(div_funk01(15231, 123))
"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    16     18.1 MiB     18.1 MiB           1   @profile()
    17                                         def div_funk01(num_a, num_b):
    18                                             
    19                                             Функция возвращает результат деления числа A на число B
    20                                             :param num_a: аргумет - делимое
    21                                             :param num_b: аргумент - делитель
    22                                             :return: результат деления / информация об ошибке
    23                                             
    24     18.1 MiB      0.0 MiB           1       try:
    25     18.1 MiB      0.0 MiB           1           result = (int(num_a / num_b), num_a % num_b)
    26     18.1 MiB      0.0 MiB           1           return result
    27                                             except ZeroDivisionError:
    28                                                 return print('Делить на 0 нельзя')
"""

original_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

@profile()
def my_func1(list_input):
    """
    Функция формирования массива из элементов входного списка,
    не имеющих повторений.
    :param list_input: исходный ссписок для выборки элементов
    :return: результирующий список
    """
    result_list = [el for el in list_input if list_input.count(el) < 2]
    return result_list

print(my_func1(original_list))

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    34     18.1 MiB     18.1 MiB           1   @profile()
    35                                         def my_func1(list_input):
    36                                             
    37                                             Функция формирования массива из элементов входного списка,
    38                                             не имеющих повторений.
    39                                             :param list_input: исходный ссписок для выборки элементов
    40                                             :return: результирующий список
    41                                             
    42     18.1 MiB      0.0 MiB          17       result_list = [el for el in list_input if list_input.count(el) < 2]
    43     18.1 MiB      0.0 MiB           1       return result_list
"""

@profile()
def my_func(list_input):
    """
    Функция формирования и вывода в консоль массива из элементов 
    входного списка, не имеющих повторений.
    :param list_input: исходный ссписок для выборки элементов
    :return: результирующий список 
    """
    result_list = []
    for el in list_input:
        if list_input.count(el) < 2:
            result_list.append(el)
    return print(result_list)

my_func(original_list)

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    47     18.1 MiB     18.1 MiB           1   @profile()
    48                                         def my_func(list_input):
    49                                             
    50                                             Функция формирования и вывода в консоль массива из элементов 
    51                                             входного списка, не имеющих повторений.
    52                                             :param list_input: исходный ссписок для выборки элементов
    53                                             :return: результирующий список 
    54                                             
    55     18.1 MiB      0.0 MiB           1       result_list = []
    56     18.1 MiB      0.0 MiB          15       for el in list_input:
    57     18.1 MiB      0.0 MiB          14           if list_input.count(el) < 2:
    58     18.1 MiB      0.0 MiB           6               result_list.append(el)
    59     18.1 MiB      0.0 MiB           1       return print(result_list)
"""

var = ("\n"
       "В результате выполнения замеров используемой памяти харакерных \n"
       "различий при использовании различных функций получить не удалось, \n"
       "ввиду слишко малого объема, так как \n"
       "для данных ввычеслеений достаточно изначально выделенной памяти")
print(var)