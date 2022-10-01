"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В
базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры, уникальные
для каждого типа оргтехники."""

"""
5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу
в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру (например, словарь)."""


class StoreHouse:

    def __init__(self, length, width, height, year, *equipment):
        self.length = length
        self.width = width
        self.height = height
        self.year = year
        self.equipment = equipment


class OfficeEquipment:
    def __init__(self, model, serial_number, year):
        self.model = model
        self.serial_number = serial_number
        self.year = year


class Printer(OfficeEquipment):
    def __init__(self, model, serial_number, year, resolution, number_of_pages):
        super(Printer, self).__init__(model, serial_number, year)
        self.resolution = resolution
        self.number_of_pages = number_of_pages


class Scanner(OfficeEquipment):
    def __init__(self, model, serial_number, year, resolution):
        super(Scanner, self).__init__(model, serial_number, year)
        self.resolution = resolution


class Xerox(OfficeEquipment):
    def __init__(self, model, serial_number, year, resolution, type):
        super(Xerox, self).__init__(model, serial_number, year)
        self.resolution = resolution
        self.type = type
