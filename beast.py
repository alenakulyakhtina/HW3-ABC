import enum
import random
import string

from animal import Animal


class BeastEat(enum.Enum):
    """ Перечисляемый тип - вид питание зверя """
    """ Хищник """
    PREDATOR = 0
    """ Травоядное """
    HERBIVORE = 1
    """ Насекомоядное """
    INSECTIVORES = 2


class Beast(Animal):
    """ Класс описывающий зверей """

    def __init__(self, name: str, weight: int, type: BeastEat):
        """ type изменяется от 0 до 2: """
        """ Хищник - 0, Травоядное - 1, Насекомоядное - 2"""
        self.name = name
        self.weight = weight
        self.type = type

    @staticmethod
    def generate_random():
        """ Реализация заполнения случайными данными """
        name = ''.join([random.choice(string.ascii_lowercase) for i in range(random.randrange(3, 12))])
        weight = random.randint(1, 10000)
        type = BeastEat(random.randint(0, len(BeastEat) - 1))
        return Beast(name, weight, type)

    def function_for_sorting(self) -> float:
        """ Функция, возвращающая значение для сортировки """
        symbol_sum = 0
        for i in self.name:
            symbol_sum += ord(i)
        return symbol_sum / (self.weight + 0.0)

    def __str__(self):
        """ Построение строки для вывода в файл """
        return f'It is Beast: name - {self.name}, weight - {self.weight} grams, type of nutrition - {self.type.name}\n'
