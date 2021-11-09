from abc import ABC, abstractmethod


class Animal(ABC):
    """ Класс описывающий общее животное"""

    def __init__(self, name: str, weight):
        self.name = name
        self.weight = weight

    @abstractmethod
    def generate_random(self):
        """ Генерация случайного животного """
        pass

    @abstractmethod
    def function_for_sorting(self):
        """ Сортировка животных """
        pass
