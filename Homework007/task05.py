"""5) Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод
для каждого экземпляра.
"""


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):

    def draw(self):
        print(f'Отрисовывается: {self.title}')


class Pencil(Stationery):

    def draw(self):
        print(f'Выполнение отрисовки {self.title}а')


class Handle(Stationery):

    def draw(self):
        print(f'Запуск отрисовки предмета: {self.title}')


stationery_object = Pen('Шариковая ручка')
stationery_object2 = Pencil('Карандаш')
stationery_object3 = Handle('Перманентный маркер')

stationery_object2.draw()
stationery_object.draw()
stationery_object3.draw()
