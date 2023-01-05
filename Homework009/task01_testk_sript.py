
import unittest
from task01_test_func import *


class Test_func_one(unittest.TestCase):
    """Первый testCase для нескоольких небольших функций"""
    #тест проверки результаа функции деления
    def test_div_numbers(self):
        self.assertEqual(div_numbers(10, 2), 5)

    # тест проверки обработки исключения функции деления
    def test_div_numbers_except(self):
        self.failureException(div_numbers(10, 0), 'Делить на 0 нельзя')

    # тест проверки результаа функции сумы наибольших элементов списка
    def test_sum_func_one(self):
        self.assertEqual(sum_func(1, 2, 3), 5)

    # тест проверки результаа функции сумы наибольших элементов списка
    def test_sum_func_two(self):
        self.assertNotEqual(sum_func(1, 2, 3), 7)

    # тест проверки результаа функции замены стройной буквы на заглавную
    def test_sub_capital_list(self):
        self.assertEqual(sub_capital_list('te'), ['T', 'E'])


class Test_func_two(unittest.TestCase):
    """Второй testCase для тестов классов их экземпляров и методов """

    def setUp(self):
        #Создание ннеобходимых объектов классов
        self.road_calc = Road(20, 5000)
        self.hr_item = Position('Василиса', 'Васечкина', 'слесарь',
                                12000, 43029)

    #Проверка ссылаются ли два экземпляра класса на один обьект
    def test_class_obj(self):
        self.assertIsNot(Road(10, 20), Road(10, 20))

    #Проверка результатов работы метода material_mass_calculation класса Road
    def test_metod_class01(self):
        self.assertEqual(self.road_calc.material_mass_calculation(), 125000)

    # Проверка соответствия словаря атрибута класса заданному
    def test_metod_class02(self):
        self.assertDictEqual(self.hr_item.income,
                             {"Salary": 12000, "Bonus": 43029})

    # Проверка ссылаются ли два экземпляра класса на один обьект
    def test_metod_class03(self):
        self.assertIsNot(Worker('Ли','Кунь', '', 4, 5),
                         Worker('Ли','Кунь', '', 4, 5))

    # Проверка обьекта класса на пренадлежноость клаассу Road
    def test_metod_class04(self):
        self.assertIsInstance(self.road_calc, Road)