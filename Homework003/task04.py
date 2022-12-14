"""Программа принимает действительное положительное число x
и целое отрицательное число y. Необходимо выполнить возведение числа x
в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения
числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **,
предусматривающая использование цикла."""

number_x = float(input('Введите действительное положительное число X: '))
number_y = int(input('Введите целое отрицательное число Y: '))


def expo_lite_func(arg_x, arg_y):
    """ Функция возведения в степень с помошью оператоора *"""
    return arg_x ** arg_y


print(f'Первый результат возведения числа X = {number_x} '
      f'в степень Y = {number_y} равен '
      f'{expo_lite_func(number_x, number_y): .5f}')


def de_exponent_func(arg_x, arg_y):
    """ Функция на вход принимает два аргумента и возвращает результат
    возведения первого аргумента в степень равную второму аргументу"""

    result = arg_x

    if arg_y > 0:
        count = arg_y
    elif arg_y == 0:
        result = 1
        return result
    else:
        count = - arg_y

    while count != 1:
        result *= arg_x
        count -= 1

    if arg_y > 0:
        return result
    else:
        return 1 / result


print(f"Второй результат возведения числа X = {number_x} "
      f"в степень Y = {number_y} равен "
      f"{de_exponent_func(number_x, number_y): .5f}")
