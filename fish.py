import enum
import string
import random

from animal import Animal


class Place(enum.Enum):
    """ Перечисляемый тип - среда обитания рыбы"""
    """ Река """
    RIVER = 0
    """ Море """
    SEA = 1
    """ Озеро """
    LAKE = 2


class Fish(Animal):
    """ Класс описывающий рыб """

    def __init__(self, name: str, weight: int, place: Place):
        """ place измняется от 0 до 2: """
        """ Река - 0, Море - 1, Озеро - 2 """
        self.name = name
        self.weight = weight
        self.place = place

    @staticmethod
    def generate_random():
        """ Реализация заполнения случайными данными """
        name = ''.join([random.choice(string.ascii_lowercase) for i in range(random.randrange(3, 12))])
        weight = random.randint(1, 10000)
        place = Place(random.randint(0, len(Place) - 1))

        return Fish(name, weight, place)

    def function_for_sorting(self) -> float:
        """ Функция, возвращающая значение для сортировки """
        symbol_sum = 0
        for i in self.name:
            symbol_sum += ord(i)
        return symbol_sum/(self.weight+0.0)

    def __str__(self):
        """ Построение строки для вывода в файл """
        return f'It is Fish: name - {self.name}, weight - {self.weight} grams; habitat - {self.place.name}\n'

