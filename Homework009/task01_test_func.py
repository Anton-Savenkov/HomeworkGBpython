"""В данном файле сгруппированы функции для тестирования"""

#Homework003/task01
def div_numbers(num_a, num_b):
    """
    Функция принемает два числа введенных пользоваателем,
    возвращает результат деления числа A на число B
    :param num_a: аргумет - делимое
    :param num_b: аргумент - делитель
    :return: результат деления
    """
    try:
        return num_a / num_b
    except ZeroDivisionError:
        return print('Делить на 0 нельзя')

#Homework003/task03
def sum_func(arg_a, arg_b, arg_c):
    """Функция принимает три элемента и возвращает сумму двуух наибольших"""
    list_num = (arg_a, arg_b, arg_c)
    first_num = max(list_num)
    second_num = max(i for i in list_num if i != first_num)
    return first_num + second_num

#Homework003/task06
sub_capital_word = lambda word: word.capitalize()

def sub_capital_list(list_input):
    """Функция принимает сстроку из слов латинскими бууквами,
     возвращает список слов с заглавными буквами
    :param list_input: строка латинских слов
    :return : строка слов с заглавными буквааим
    """
    sub_list = []
    for el in list_input:
        sub_list.append(sub_capital_word(el))
    return sub_list

#Homework007/task02
class Road:
    weight = 25  # масса покрытия одного кв метра дороги (кг)
    web_thickness = 0.05  # толщина полотна (м)

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def material_mass_calculation(self):
        """ Расчет колличества асфальта для покрытия
        орожного полотна с введенными длинной и шириной
        """
        return int(
            self._length * self._width * Road.weight * Road.web_thickness)

#Homework007/task03
class Worker:

    def __init__(self, name, surname, position, salary, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"Salary": salary, "Bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, salary, bonus):
        super().__init__(name, surname, position, salary, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self.income["Salary"] + self.income["Bonus"]

    def __str__(self):
        return f'Сотрудник: {self.name} {self.surname}, доход включая ' \
               f'премию и оклад: {self.get_total_income()}'


hr_item = Position('Василиса', 'Васечкина', 'слесарь', 12000, 43029)