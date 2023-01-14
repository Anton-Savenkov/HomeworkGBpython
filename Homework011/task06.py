"""
Задание 6.

Создать  НЕ программно (вручную) текстовый файл test_file.txt, заполнить его тремя строками:

Принудительно программно открыть файл в формате Unicode и вывести его содержимое.
Что это значит? Это значит, что при чтении файла вы должны явно указать кодировку utf-8
и файл должен открыться у ЛЮБОГО!!! человека при запуске вашего скрипта.

"""
from chardet import detect

file_name = 'test_file.txt'


def encoding_files(f_name):
    """
    Функция открвает файл в формате Unicode
    :param f_name: имя файла
    :return: возвращает файл в кодировке 'utf-8'
    """
    with open(f_name, 'rb') as new_obj:
        content_bytes = new_obj.read()
    # print(content_bytes) #вывод контента в представлении bytes
    detected = detect(content_bytes)
    encoding = detected['encoding']
    # print(encoding) #вывод исходной кодировки
    content_text = content_bytes.decode(encoding)
    with open(f_name, 'w', encoding='utf-8') as new_obj:
        new_obj.write(content_text)
    # print(content_text)


encoding_files(file_name)

with open('test_file.txt', 'r', encoding='utf-8') as new_obj:
    print(new_obj.read())
