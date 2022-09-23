"""
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите
методы и покажите результат.
"""


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("I'm Go")

    def stop(self):
        print("I'm don't go")

    def turn(self, direction):
        print(f"I turn to {direction}")

    def show_speed(self):
        print(f"{self.speed} km/h")


class TownCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)

    def go(self):
        print("I'm TownCar")
        super().go()

    def stop(self):
        print("I'm TownCar")
        print("I'm don't go")

    def turn(self, direction):
        print("I'm TownCar")
        print(f"I turn to {direction}")

    def show_speed(self):
        if self.speed > 60:
            print(f"Speed is very high! {self.speed} km/h")
            return
        print(f"{self.speed} km/h")


class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)

    def go(self):
        print("I'm SportCar")
        super().go()

    def stop(self):
        print("I'm SportCar")
        print("I'm don't go")

    def turn(self, direction):
        print("I'm SportCar")
        print(f"I turn to {direction}")


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)

    def go(self):
        print("I'm WorkCar")
        super().go()

    def stop(self):
        print("I'm WorkCar")
        print("I'm don't go")

    def turn(self, direction):
        print("I'm WorkCar")
        print(f"I turn to {direction}")

    def show_speed(self):
        if self.speed > 40:
            print(f"Speed is very high! {self.speed} km/h")
            return
        print(f"{self.speed} km/h")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)

    def go(self):
        print("I'm PoliceCar")
        super().go()

    def stop(self):
        print("I'm PoliceCar")
        print("I'm don't go")

    def turn(self, direction):
        print("I'm PoliceCar")
        print(f"I turn to {direction}")
