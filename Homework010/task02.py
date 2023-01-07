"""Создать метакласс для паттерна Синглтон"""

class MetaClassSingleton(type):
    #метакласс создающий единственный объект ккласса
    instance = None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls, *args, **kwargs)

        return cls.instance


class Test(metaclass=MetaClassSingleton):
#метакласс позволяет всем новым объектам экземплярам клаасса
#ссылаться на один объет

    def __init__(self, name, age ):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}, возраст - {self.age}'

a = Test('Robin', '732')
b = Test('a', '7')

print(a)