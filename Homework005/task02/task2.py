"""Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""

#Вывод текста файла
new_file = open('text_task2.txt', 'r', encoding='utf-8')
text_file = new_file.read()
print(f'Текст файла:\n{text_file}')
new_file.close()

#колличество строк через функцию len
new_file = open('text_task2.txt', 'r', encoding='utf-8')
line_text = new_file.readlines()
print(f'Колличество сток в файле {len(line_text)}')
print()
new_file.close()

#колличество строк и слов по строкам через цикл
new_file = open('text_task2.txt', 'r', encoding='utf-8')
line_text = new_file.readlines()
count_line = 0
for el in line_text:
    line = el.split()
    count_line +=1
    count_word = 0
    for i in line:
        count_word +=1
    print(f'Колличество слов в строке {count_line} = {count_word}')
print(f'Колличество строк в файле = {count_line}')
new_file.close()