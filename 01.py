#1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep


class TrafficLight:
    __color = ["red", "yellow", "green"]
    timer = {__color[0]: 7, __color[1]: 2, __color[2]: 2}

    if __color == ["red", "yellow", "green"]: #B
        def running(self):
            print(self.__color[0])
            sleep(self.timer[self.__color[0]])
            print(self.__color[1])
            sleep(self.timer[self.__color[1]])
            print(self.__color[2])
            sleep(self.timer[self.__color[2]])
            print("finish")
    else:
        print("Вы изменили приватный параметр")

newTrafficLight = TrafficLight().running()