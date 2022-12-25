"""4) Реализуйте базовый класс Car. У данного класса должны быть
следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних
классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:

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


class TownCar(Car):

    def __init__(self, name, color, speed, is_police, is_town_car):
        super().__init__(name, color, speed, is_police)
        self.is_town_car = is_town_car

    def show_speed(self):
        """метод вывводит сообщение о соответствии скорости заданной
        максимальной для данного типа авто"""
        if self.speed > 60:
            return f'Автомобиль {self.name} привысил допустимую скорость ' \
                   f'(маклимальная скорость для данного типа автомобиля 60км/ч'
        return f'Автмобиль {self.name} движется со скоростью {self.speed}'


class SportCar(Car):
    def __init__(self, name, color, speed, is_police, is_sport_car):
        super().__init__(name, color, speed, is_police)
        self.is_sport_car = is_sport_car


class WorkCar(Car):

    def __init__(self, name, color, speed, is_police, is_work_car):
        super().__init__(name, color, speed, is_police)
        self.is_work_car = is_work_car

    def show_speed(self):
        """метод вывводит сообщение о соответствии скорости заданной
                максимальной для данного типа авто"""
        if self.speed > 40:
            return f'Автомобиль {self.name} привысил допустимую скорость ' \
                   f'(маклимальная скорость для данного типа автомобиля 60км/ч'
        return f'Автмобиль {self.name} движется со скоростью {self.speed}'


class PoliceCar(Car):

    def duty_car(self, traffic_violation):
        """метод выввода сообщения о обнаружении нарушений ПДД"""
        if traffic_violation:
            return 'Выявлено нарушение ПДД'
        return 'Нарушения не обнаружены'


audi = TownCar('Audi Q5', 'серый', 62, False, True)
bmw_m1 = SportCar('BMW M1', 'красный', 210, False, True)
lexus = WorkCar('Lexus RX300', 'зеленый', 40, False, True)
bmw = PoliceCar('BMW 318', 'белый', 65, True)

print(f'Автомобиль {audi.name}, цвет - {audi.color}, движется со скоростью '
      f'{audi.speed}')
print(f'{bmw.name}, это полиция - {bmw.is_police}')
print(f'Автомобиль {bmw_m1.go()}  \n{lexus.show_speed()} '
      f'\nPolice: {bmw.duty_car(True)} ')
print(f'{audi.turn("на юг")} \n{lexus.stop()}')
