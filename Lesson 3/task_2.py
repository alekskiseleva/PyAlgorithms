# Задача 2
# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5,
# (индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
# Блок-схема - https://drive.google.com/file/d/1QYBPAOgWooxXLu_-IhTI9qV1bElCwiFo/view?usp=sharing

from random import randint

my_mssv = [randint(0, 100) for i in range(10)]
# my_mssv = [8, 3, 15, 6, 4, 2] - [0, 3, 4, 5]

mssv_2 = []

print('Массив:', my_mssv)

for i in my_mssv:

    if i % 2 == 0:
        mssv_2.append(my_mssv.index(i))

print("Индексы четных элементов первого массива:", mssv_2)
