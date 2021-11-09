import random
from enum import Enum
from fish import Fish, Place
from beast import Beast, BeastEat
from bird import Bird


class AnimalType(Enum):
    """ Перечисляемый тип - вид животного """
    """ Рыба """
    FISH = 0
    """ Птица """
    BIRD = 1
    """ Зверь """
    BEAST = 2


class Container:
    """ Класс описывающий работу контейнера (чтение, сортировка, запись) """
    def __init__(self):
        self._list = []

    def read_from_file(self, filename: str):
        """ Чтение данных из файла """

        with open(filename, 'r') as f:
            lines = f.readlines()

        for i_l, line in enumerate(lines):
            words = line.split()
            try:
                read_type = AnimalType(int(words[0]))
                if read_type == AnimalType.FISH:
                    self._list += [Fish(words[1], int(words[2]), Place(int(words[3])))]
                elif read_type == AnimalType.BIRD:
                    self._list += [Bird(words[1], int(words[2]), bool(words[3]))]
                elif read_type == AnimalType.BEAST:
                    self._list += [Beast(words[1], int(words[2]), BeastEat(int(words[3])))]
                else:
                    print("Unknown type of animal in line %d" % i_l)
            except:
                print("Could not parse data from line %d" % i_l)
                pass

    def generate_random(self, number_of_animals):
        """ Заполнение контейнера случайными животными """
        self._list = []
        for i_n in range(number_of_animals):
            type = AnimalType(random.randint(0, len(AnimalType) - 1))
            types = [Bird, Fish, Beast]
            self._list += [types[type.value].generate_random()]

    def straight_sort(self) -> None:
        """ Сортировка содержимого контейнера """
        for i in range(len(self)):
            animal = self._list[i]
            j = i - 1
            while j >= 0 and self._list[j].function_for_sorting() < animal.function_for_sorting():
                self._list[j + 1] = self._list[j]
                j -= 1
            self._list[j + 1] = animal


    def __str__(self):
        delim = ""
        for i in range(len(self._list)):
            delim += f"{i}) {self._list[i]}\n"
        return delim

    def __len__(self):
        return len(self._list)