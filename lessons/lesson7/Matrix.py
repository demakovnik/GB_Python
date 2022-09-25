"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, data):
        self.__data = list(data)

    def __add__(self, other):
        result_data = list()
        rows = len(self.__data)
        if rows != len(other.__data):
            print('Error: rows mismatch')
            return
        cols = len(self.__data[0])
        for i in range(0, rows):
            li = list()
            if len(self.__data[i]) != cols or len(other.__data[i]) != cols:
                print('Error: rows mismatch')
                return
            for j in range(0, cols):
                li.append(self.__data[i][j] + other.__data[i][j])
            result_data.append(li)
        return Matrix(result_data)

    def __str__(self):
        s = ""
        for line in self.__data:
            s += '  '.join(map(str, line)) + '\n'
        return s
