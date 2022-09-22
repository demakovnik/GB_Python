"""
1. Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import itertools
import time


class TrafficLight:
    __color = ""

    def running(self):
        modes = ["red", "yellow", "green"]
        d_time = 0
        mode = itertools.cycle(modes)
        for el in mode:
            self.__color = el
            if el == modes[0]:
                d_time = 7
            elif el == modes[1]:
                d_time = 2
            elif el == modes[2]:
                d_time = 7
            print(self.__color)
            time.sleep(d_time)



