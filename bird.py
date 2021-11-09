import random
import string

from animal import Animal


class Bird(Animal):
    """ Класс описывающий птиц """

    def __init__(self, name: str, weight: int, migration: bool):
        """ migration: перелетная - true, зимующая - false"""
        self.migration: bool = migration
        self.name = name
        self.weight = weight

    @staticmethod
    def generate_random():
        """ Реализация заполнения случайными данными """
        name = ''.join([random.choice(string.ascii_lowercase) for i in range(random.randrange(3, 12))])
        weight = random.randint(1, 10000)
        migration = random.choice([True, False])
        return Bird(name, weight, migration)

    def function_for_sorting(self) -> float:
        """ Функция, возвращающая значение для сортировки """
        symbol_sum = 0
        for i in self.name:
            symbol_sum += ord(i)
        return symbol_sum/(self.weight+0.0)

    def __str__(self):
        """ Построение строки для вывода в файл """
        if bool(self.migration):
            winter = "it is a migratory bird"
        else:
            winter = "this bird stays for the winter"
        return f'It is Bird: name - {self.name}, weight - {self.weight} grams, wintering - {winter}\n'

