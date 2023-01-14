"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet

# добавлен аргумент "-c" для MacOS
args_yand = ['ping', 'yanddex.ru', '-c', '5']
args_yout = ['ping', 'youtube.com', '-c', '5']


def PingWebRes(input_args):
    """
    Вункция вывода пингаа веб-ресурсов
    :param input_args: веб-ресурс
    :return: вывод в консоль
    """
    resurse_ping = subprocess.Popen(input_args, stdout=subprocess.PIPE)
    for line in resurse_ping.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        print(end=line.decode('utf-8'))


print(f'Выполняем пинг веб-ресурса {args_yand[1]}')
PingWebRes(args_yand)
print(f'\nВыполняем пинг веб-ресурса {args_yout[1]}')
PingWebRes(args_yout)
