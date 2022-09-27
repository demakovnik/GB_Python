"""
3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть
реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
деление (__truediv__()). Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
и целочисленное (с округлением до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.
Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.
Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод
позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернёт строку:
*****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернёт строку:
*****\n*****\n*****.
"""


class Cell:

    def __init__(self, cells):
        self.__cells = cells

    def __add__(self, other):
        return Cell(self.__cells + other.__cells)

    def __sub__(self, other):
        try:
            if self.__cells - other.__cells < 0:
                raise ValueError('Value less than zero')
            return Cell(self.__cells - other.__cells)
        except ValueError as e:
            return e

    def __mul__(self, other):
        return Cell(self.__cells * other.__cells)

    def __truediv__(self, other):
        try:
            return Cell(int(self.__cells / other.__cells))
        except ZeroDivisionError as e:
            return e

    def __str__(self):
        return str(self.__cells)

    def make_order(self, number):
        full_strings = int(self.__cells / number)
        remainder = self.__cells % number
        s = ""
        for i in range(0, full_strings):
            s += '*' * number + '\n'
        s += remainder * '*'

        return s
