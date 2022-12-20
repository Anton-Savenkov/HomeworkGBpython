"""2) Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина). Значения данных атрибутов должны передаваться
при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего
дорожного полотна. Использовать формулу: длинаширинамасса асфальта
для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т"""


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
        res = int(
            self._length * self._width * Road.weight * Road.web_thickness)
        print(f'Asphalt concrete mass for pavement with parameters = {res} kg')


road_calc = Road(20, 5000)
road_calc.material_mass_calculation()
