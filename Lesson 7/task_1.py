# Задача 1
# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными
# числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
#
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

from random import randint, random


def sort_to_bubble(mssv):
    n = len(mssv)
    for i in range(n):

        for j in range(n - i - 1):
            a, b = mssv[j], mssv[j + 1]

            if a < b:
                mssv[j], mssv[j + 1] = b, a

    return


# m = int(input('Введите размерность массива '))
z = int(random()*100)
mssv = [randint(-100, z) for i in range(10)]
print(mssv)
sort_to_bubble(mssv)
print(mssv)
