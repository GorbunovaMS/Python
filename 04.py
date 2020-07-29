#4.Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} начала двиение.")

    def stop(self):
        print(f"Машина {self.name} остановилась.")

    def turn(self, direction):
        print(f"Машина {self.name} повернула на{direction}")

    def show_speed(self):
        print(f"Текущая скорость автомобиля: {self.speed}км/ч.")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Скорость {self.speed}км/ч. Привышение! Убавьте скорость!")
        else:
            print(f"Скорочть автомобиля {self.speed} - в пределах нормы.")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Скорость {self.speed}км/ч. Привышение! Убавьте скорость!")
        else:
            print(f"Скорочть автомобиля {self.speed} - в пределах нормы.")


class PoliceCar(Car):
    pass


a = Car(60, 'green', 'Volvo', False)
a.go()
a.turn('право')
a.stop()
print('\n')

b = TownCar(80, 'black', 'BMW', False)
print(f"Машина {b.name}, цвета {b.color}")
b.go()
b.show_speed()
b.turn('лево')
print('\n')

c = WorkCar(50, 'white', 'Audi', False)
print(f"Машина {c.name}, цвета {c.color}")
c.go()
c.show_speed()
c.stop()
print('\n')
