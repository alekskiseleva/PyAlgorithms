# Задача 6
# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
# Блок-схема - https://drive.google.com/file/d/12CsYJTtRDX6x2_PTF3OTRJ2VzsGhR0zL/view?usp=sharing

from random import randint

my_mssv = [randint(-100, 100) for i in range(10)]
print('Исходный массив:', my_mssv)

mssv = []
sum_el = 0
mx = 0
mn = 0
max_el = my_mssv[0]
min_el = my_mssv[0]

for i in my_mssv:

    if i > max_el:
        max_el = i
        mx = my_mssv.index(i)

    if i < min_el:
        min_el = i
        mn = my_mssv.index(i)

print('max -', max_el, '\nmin -', min_el)

if mx > mn:
    print('Массив элементов между min и max', my_mssv[mn+1:mx])
    for i in my_mssv[mn+1:mx]:
        mssv.append(i)

else:
    print('Массив элементов между max и min', my_mssv[mx+1:mn])
    for i in my_mssv[mx+1:mn]:
        mssv.append(i)

for i in mssv:
    sum_el = sum_el + i

print('Сумма элементов между min и max, не включающая их =', sum_el)
