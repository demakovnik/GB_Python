from abc import ABC, abstractmethod

"""
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
"""


class Clothing(ABC):

    @abstractmethod
    def consumption(self):
        pass


class Costume(Clothing, ABC):

    def __init__(self, H):
        self.__H = H

    def consumption(self):
        return 2 * self.__H + 0.3

    @property
    def height(self):
        return self.__H

    @height.setter
    def height(self, H):
        self.__H = H



class Coat(Clothing, ABC):

    def __init__(self, V):
        self.__V = V

    def consumption(self):
        return self.__V / 6.5 + 0.5

    @property
    def volume(self):
        return self.__V

    @volume.setter
    def volume(self, H):
        self.__H = H
