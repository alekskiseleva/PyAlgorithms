# Задача 1
# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Блок-схема - https://drive.google.com/file/d/14Mh0xFzySgdbO_mhgPGDmI2h3KJGsVF2/view?usp=sharing


for i in range(2, 10):

    c = 0

    for j in range(2, 100):

        if j % i == 0:
            c = c + 1
    print(f'Числу {i} кратно {c} чисел')


