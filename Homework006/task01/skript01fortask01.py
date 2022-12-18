

def sum_str_func01():
    """Функция подсчитываает сумму чисел в строке,
    раздеренных пробелом,"""
    list_num = '1 3 4 5 6 7 8 8'
    number_list = list_num.split()
    total_sum = 0
    for el in number_list:
        total_sum += int(el)

    return total_sum

sum_str_func01()

def sum_str_func02():
    """Функция подсчитываает сумму чисел в строке,
        раздеренных пробелом,"""
    list_num_str = '1 3 4 5 6 7 8 8'
    number_list = list_num_str.split()
    s = sum(int(el) for el in number_list)
    return s


sum_str_func02()

def sum_str_func03():
    """Функция подсчитываает сумму чисел в строке,
        раздеренных пробелом,"""
    num_srt = '1 3 4 5 6 7 8 8'
    list_str = num_srt.split(' ')
    list_num2 = [int(el) for el in list_str]
    return (f'sum = {sum(list_num2)}')

sum_str_func03()

def div_funk01():
    """
    Функция возвращает результат деления числа A на число B
    :param num_a: аргумет - делимое
    :param num_b: аргумент - делитель
    :return: результат деления
    """
    num_a = 157
    num_b = 9
    try:
        result = (int(num_a / num_b), num_a % num_b)
        return result
    except ZeroDivisionError:
        return print('Делить на 0 нельзя')
#print(div_funk01())

def div_func02():
    """ Функция возвращает результат деления числа A на число B
    и остаток от деления"""
    num_a = 157
    num_b = 9
    return divmod(num_a,num_b)
#print(div_func02())