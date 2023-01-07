"""Создать не менее двух дескрипторов для атрибутов классов,
которые вы создали ранее в ДЗ"""

class Numberchecks:
    #класс валидации значения атрибута - число больше 0
    def __set__(self, instance, value):
        """валидация - происваевоемое значение должно быть больше ноля"""
        if value < 0:
            raise ValueError("Значение не может быть меньше нуля")
        else:
            instance.__dict__[self.my_atr] = value

    def __set_name__(self, owner, my_atr):
        self.my_atr = my_atr

class Textchecks:
    # класс валидации значения атрибута - вод только строки
    def __set__(self, instance, value):
        """проверка - происваевоемое значение должно быть больше ноля"""
        if type(value) != str:
            raise ValueError("Не может быть числом, введите текст")
        else:
            instance.__dict__[self.my_atr] = value

    def __set_name__(self, owner, my_atr):
        self.my_atr = my_atr

class Car:
    #Атрибуты которые делаеем дискрипторами
    speed = Numberchecks()
    name = Textchecks()
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        #метод вывода сообщения о начале движения
        return f' {self.name} Начал движение (поехал)'

    def stop(self):
        # метод вывода сообщения о остановке
        return f' {self.name} Прекратил движение (остановился)'

    def turn(self, direction):
        # метод вывода сообщения о изменении направления движения
        return f' {self.name} повернула в направлении {direction}'

    def show_speed(self):
        # метод вывода скорости
        return f'Автомобиль {self.name} движется со скоростью {self.speed}'

car_item = Car('Q5', 'синий', 50, False)
print(car_item.name)
print(car_item.speed)

class Cell:
    # Атрибуты которые делаеем дискрипторами
    quantity = Numberchecks()
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return str(self.quantity)

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity > other.quantity:
            return Cell(self.quantity - other.quantity)
        else:
            return 'Разница колличества ячеек первой и ' \
                   'второй клетки меньше нуля'

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cell(self.quantity // other.quantity)

    def make_order(self, row):
        result = []
        for _ in range(self.quantity // row):
            result.append('*' * row)
        if self.quantity % row != 0:
            result.append('*' * (self.quantity % row))
        return '\\n'.join(result)


print("Создаем объекты класса Cell - клетки")
cell_obj1 = Cell(20)
print(f'Клетка1 --> {cell_obj1}')
cell_obj2 = Cell(30)
print(f'Клетка2 --> {cell_obj2}')
cell_obj3 = Cell(25)
print(f'Клетка3 --> {cell_obj3}')
cell_obj4 = Cell(37)
print(f'Клетка4 --> {cell_obj4}')
