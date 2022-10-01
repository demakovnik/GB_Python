"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных."""
from datetime import datetime


class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'{self.day}-{self.month}-{self.year}'

    @classmethod
    def set_date(cls, data):
        day, month, year = str(data).split('-')
        try:
            Date.validation(Date(day, month, year))
        except ValueError as error:
            return 'Wrong date'
        return cls(day, month, year)

    @staticmethod
    def validation(obj):
        get_date = lambda d: datetime.strptime(d, '%d-%m-%Y').date()
        return get_date(str(obj))


if __name__ == "__main__":
    d1 = Date.set_date('31-01-2022')
    print(d1)

    d2 = Date.set_date('33-09-2022')
    print(d2)


