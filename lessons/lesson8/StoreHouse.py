"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В
базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры, уникальные
для каждого типа оргтехники."""

"""
5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу
в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру (например, словарь)."""

from abc import ABC

from collections import Counter


class StoreHouse:

    def __init__(self, length, width, height, year, *equipment):
        self.length = length
        self.width = width
        self.height = height
        self.year = year
        self.equipment = list(equipment)

    def accept(self, equip):
        equip.set_owner(None)
        self.equipment.append(equip)

    def transfer(self, equipment, department):
        self.equipment.remove(equipment)
        equipment.set_owner(department)

    def get_possessions(self):
        return Counter(map(lambda arg: str(type(arg)).replace("<class '__main__.", "")
                           .replace("'>", ""), self.equipment)).items()



class OfficeEquipment(ABC):
    def __init__(self, model, serial_number, year, owner):
        self.model = model
        self.serial_number = serial_number
        self.year = year
        self.owner = owner

    def set_owner(self, owner):
        self.owner = owner

    def __str__(self):
        return f'Model: {self.model}, Serial Number: {self.serial_number}, Year: {self.year}, Owner: {self.owner}'



class Printer(OfficeEquipment):
    def __init__(self, model, serial_number, year, owner, resolution, number_of_pages):
        super(Printer, self).__init__(model, serial_number, year, owner)
        self.resolution = resolution
        self.number_of_pages = number_of_pages


class Scanner(OfficeEquipment):
    def __init__(self, model, serial_number, year, owner, resolution):
        super(Scanner, self).__init__(model, serial_number, year, owner)
        self.resolution = resolution


class Xerox(OfficeEquipment):
    def __init__(self, model, serial_number, year, owner, resolution, tp):
        super(Xerox, self).__init__(model, serial_number, year, owner)
        self.resolution = resolution
        self.tp = tp


if __name__ == "__main__":
    xerox = Xerox('xerox 456', 'ABCDEF123', 2019, None, '300px', 'color')
    xerox2 = Xerox('xerox 456', 'ABCDEF123', 2019, None, '300px', 'color')
    scanner = Scanner('Samsung 123', 'DEFGH456', 2018, None, '600px')
    printer = Printer('Kyocera 456', 'ABCD456456546', 2019, None, '1000px', 20000)

    storehouse = StoreHouse(100, 100, 10, 2021)

    storehouse.accept(xerox)
    storehouse.accept(scanner)
    storehouse.accept(printer)
    storehouse.accept(xerox2)

    print(storehouse.get_possessions())
    storehouse.transfer(xerox2, 'IT')
    print(xerox2)
    print(storehouse.get_possessions())

