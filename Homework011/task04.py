"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

"""
import subprocess

new_list = ['разработка', 'администрирование', 'protocol', 'standard']
new_list_b = [b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1'
              b'\x82\xd0\xba\xd0\xb0',
              b'\xd0\xb0\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1'
              b'\x82\xd1\x80\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0'
              b'\xd0\xbd\xd0\xb8\xd0\xb5', b'protocol', b'standard']

print(f'{new_list}\n'
      f'преобразовыем из строкового представления в байтовое -->')
for el in new_list:
    el = el.encode('utf-8')
    print(el)

print(f'{new_list_b}\n'
      f'преобразовыем из байтового представления в строковое -->')
for el in new_list_b:
    el = el.decode('utf-8')
    print(el)

