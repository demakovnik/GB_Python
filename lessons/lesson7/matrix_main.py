
from lessons.lesson7.Matrix import Matrix

if __name__ == "__main__":
    matrix1 = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[1, 1], [1, 1]])
    matrix3 = matrix1.__add__(matrix2)
    print(matrix3)