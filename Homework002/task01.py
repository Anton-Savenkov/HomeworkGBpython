"""Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе."""

new_list = ['tetxa', 'textb', 18, 22, 3.478, 56.4, None, 'new_text']

print(new_list)

for i in range(len(new_list)):
    print(
        f" {i + 1} - й элемент массива имеет тип данных - {type(new_list[i])}")