"""Создать метакласс для паттерна Синглтон"""

class MetaclassSingleton(type):
    """Метакласс создающий единственный экземпляр класса"""

    instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__call__( *args, **kwargs)
            return cls.instance
        return cls.instance

class MyClassTest(metaclass=MetaclassSingleton):
    #тестовый класс один для тестирования метода метакласса MetaclassSingleton
    pass

obj_test1 = MyClassTest()
obj_test2 = MyClassTest()

print(obj_test1 is obj_test2)

class MyClassTest1(metaclass=MetaclassSingleton):
    #тестовый класс два для тестирования метода метакласса MetaclassSingleton
    def __init__(self, x, y):
        self.x = x
        self.y = y
w = MyClassTest1(4,5)
z = MyClassTest1(5,3)

print(w == z)
