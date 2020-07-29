# 6.  Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки '{self.title}'.")


class Pen(Stationery):
    def draw(self):
        print(f"'{self.title}' отрисован ручкой.")


class Pencil(Stationery):
    def draw(self):
        print(f"'{self.title}' отрисован карандашом.")


class Handle(Stationery):
    def draw(self):
        print(f"'{self.title}' отрисован маркером.")


title = input('Введите название предмета или нажмите Enter для завершения: ')
while title:
    Stationery(title).draw()
    while True:
        print("1 - для отрисовки карандашом\n"
              "2 - для отрисовки ручкой\n"
              "3 - для отрисовки маркером")
        choice = input()
        if choice == '1':
            Pencil(title).draw()
            break
        elif choice == '2':
            Pen(title).draw()
            break
        elif choice == '3':
            Handle(title).draw()
            break
        else:
            print("Нужно выбрать один из трех вариантов меню. Попробуйте снова.")

    title = input('Введите название предмета или нажмите Enter для завершения: ')