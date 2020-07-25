import random as rm

my_list = [rm.randint(0, 100) for i in range(10)]
summa = 0
with open('04.txt', 'w', encoding='utf-8') as new_file:
    for el in my_list:
        summa += el
        new_file.write(str(el) + ' ')
print(f'Список {my_list} записан в файл 04.txt\nСумма элементов ровна {summa}')