# Задача 2_2
# Написать два алгоритма нахождения i-го по счёту простого числа.
# - Без использования Решета Эратосфена;
#  Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.
# Блок-схема -


n = 100
# n = int(input("Введите : "))
mssv = [i for i in range(1, n + 1)]

print('Исходный массив', mssv)
a = []
b = []
m = 0

for i in range(2, n - 1):

    m = 2 * i * j + i + j

    for j in range(i, n):




