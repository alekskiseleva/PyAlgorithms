# Задача 2_2
# Написать два алгоритма нахождения i-го по счёту простого числа.
# Использовать алгоритм решето Эратосфена
# Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.
# Блок-схема -


def resheto_eratosfena(n):
    c = 0  # количество делителей

    for i in range(2, n + 1):

        for j in range(2, i):

            if i % j == 0:
                c = c + 1

        if c == 0:
            a.append(i)
        else:
            c = 0
    return a


m = int(input('Введите номер простого числа: '))
n = 10000
mssv = [i for i in range(1, n)]

a = []
b = []

resheto_eratosfena(n)

print(a)

for i in range(0, len(a)):

    if i == m:
        print(f'Выводим {m}-ное простое число {a[i]}')