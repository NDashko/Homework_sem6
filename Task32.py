# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
list_1=[2, 4, 0, 17, -5, 3, 1, 25, 64, 18, 33, -10, 88]
min_number = int(input("Введите минимальное число "))
max_number = int(input("Введите максимальное число "))
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        print(i, end = ' ')
    