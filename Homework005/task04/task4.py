"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение
и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

num_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
translate_text = []
#print(num_dict.keys())

with open('text_task4.txt', 'r', encoding='utf-8') as new_obj:
    for el in new_obj:
        el = el.split(' ', 1)
        translate_text.append(f'{num_dict[el[0]]} {el[1]}')
    # print(translate_text)

with open('new_text_task4.txt', 'w', encoding='utf-8') as new_obj2:
    new_obj2.writelines(translate_text)
