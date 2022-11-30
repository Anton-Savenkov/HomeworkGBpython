"""Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""

num_a = float(input("Введите число A: "))
num_b = float(input("Введите число B: "))
num_c = float(input("Введите число C: "))

def sum_func(arg_a, arg_b, arg_c):
    """Функция принимает три элемента и возвращает сумму двуух наибольших"""
    list_num = (arg_a, arg_b, arg_c)
    first_num = max(list_num)
    second_num = max(i for i in list_num if i != first_num)
    return first_num + second_num

print(f"Сумма двух наибольших аргументов = {sum_func(num_a, num_b, num_c)}")
