"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
завершиться с ошибкой."""

class DivisionZero(Exception):

    def __init__(self, txt):
        self.txt = txt


if __name__ == "__main__":

    a, b = input('Введите числа через пробел: ').split()
    try:
        a, b = float(a), float(b)
        if b == 0:
            raise DivisionZero('На ноль делить нельзя!')
        print(f'Частное чисел: {a} и {b} равно: {a / b}')
    except (DivisionZero, ValueError) as error:
        print(error)
