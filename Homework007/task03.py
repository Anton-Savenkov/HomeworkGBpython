"""3) Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса
Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров)."""


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
print(hr_item.get_full_name())
print(hr_item.get_total_income())
print(hr_item)
