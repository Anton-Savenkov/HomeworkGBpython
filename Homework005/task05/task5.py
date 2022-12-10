"""Создать (программно) текстовый файл, записать в него программно набор
чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

import random

# Создаем список рандомных значений для записи в файл
number_list = random.sample(range(0, 101), 15)
#print(number_list)

# запись рандомного набора чисел в файл
with open('file_task5.txt', 'w', encoding='utf-8') as new_obj:
    for el in number_list:
        new_obj.write(f'{str(el)} ')

# Подсчитываем сумму записанных в файл элементов
num_sum = 0
with open('file_task5.txt', 'r', encoding='utf-8') as new_obj2:
    for el in new_obj2:
        num_in_text = el.split()
        for i in num_in_text:
            num_sum += int(i)
# вывод результатов подсчета в консоль
print(f'Сумма записанных в файл элементов = {num_sum}')
