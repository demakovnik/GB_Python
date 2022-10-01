"""7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса
(комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата."""

class Complex:

    def __init__(self, real, image):
        self.real = real
        self.image = image

    def __add__(self, other):
        return Complex(self.real + other.real, self.image + other.image)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.image - other.image)

    def __mul__(self, other):
        a1 = self.real
        a2 = other.real
        b1 = self.image
        b2 = other.image
        return Complex(a1 * a2 - b1*b2, a1*b2 + b1*a2)

    def __truediv__(self, other):
        a1 = self.real
        a2 = other.real
        b1 = self.image
        b2 = other.image
        return Complex(float((a1*a2+b1*b2) / (a2**2 + b2**2)), float((a2*b1-a1*b2) / (a2**2 + b2**2)))




    def __str__(self):
        return f'{self.real}{"{:+f}".format(self.image)}i'


if __name__ == "__main__":
    c1 = Complex(-2, 1)
    c2 = Complex(1, -1)

    print(c1+c2)

    print(c1 * c2)

    print(c1/c2)


