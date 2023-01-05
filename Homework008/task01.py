"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы
в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д."""


class Matrix:

    def __init__(self, matrix_list, rows, colum):
        self.matrix_list = matrix_list
        self.rows = rows
        self.colum = colum

    def fill_arr(self):
        self.matrix_list = [list(map(int, input(f"Введите {self.colum} числа "
                                                f"через пробел : ")
                                     .split())) for el in range(self.rows)]

    def __str__(self):
        return str('\n'.join(['\t'.join([str(i) for i in el])
                              for el in self.matrix_list]))

    def __add__(self, other):
        result = [[0] * self.colum for el in range(self.rows)]
        for el in range(self.rows):
            for i in range(self.colum):
                if len(self.matrix_list) == len(other.matrix_list) and len(
                        self.matrix_list[el]) == len(other.matrix_list[el]):
                    result[el][i] = self.matrix_list[el][i] \
                                    + other.matrix_list[el][i]
                else:
                    return "Сложение матриц разного размера невозможно"
        return Matrix(result, self.rows, self.colum)

mobj_one = Matrix(list, 3, 3)
mobj_one.fill_arr()

mobj_two = Matrix(list, 3, 3)
mobj_two.fill_arr()

print(f'Первая матрица -->\n{mobj_one}')
print(f'Вторая матрица -->\n{mobj_two}')
print(f'Сумма первой и второй матрицы -->\n{mobj_one + mobj_two}')
