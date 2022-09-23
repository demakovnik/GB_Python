"""
5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title = ""

    def draw(self):
        pass


class Pen(Stationery):
    def __init__(self):
        self.title = 'Pen'

    def draw(self):
        print("I'm a Pen. I draw like Pen")


class Pencil(Stationery):
    def __init__(self):
        self.title = 'Pencil'

    def draw(self):
        print("I'm a Pencil. I draw like Pencil")


class Handle(Stationery):
    def __init__(self):
        self.title = 'Handle'

    def draw(self):
        print("I'm a Handle. I draw like Handle")
