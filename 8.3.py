#3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список только числами.
# Класс-исключение должен контролировать типы данных элементов списка.

class MyErr(Exception):
    def __init__(self, txt):
        self.txt = txt


def check_num(num):
    try:
        complex(num)
        return 0
    except ValueError:
        return 1


arr = []
print("Для выхода из программы необходимо ввести q в качестве элемента.")
while True:
    try:
        el = input("Введите элемент: ")
        if el == 'q':
            break
        elif not check_num(el):
            arr.append(el)
        else:
            raise MyErr("Элемент не является числом!")
    except MyErr as err:
        print(err)

print(arr)