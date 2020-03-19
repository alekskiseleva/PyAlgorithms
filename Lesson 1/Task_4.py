# Задача 4
# Определить, является ли год, который ввел пользователь, високосным или не високосным.
# Блок-схема - https://drive.google.com/file/d/1IeVGgQunwZRxzvREg6KwC__F7kuJoIaK/view?usp=sharing
# тестовые значения - 1600(да), 1700(нет), 1978(нет), 1980(да), 2000(да)

year = int(input('Введите год в формате хххх: '))

if year % 4 != 0:
    print("Год не является високосным")

elif year % 100 == 0:

    if year % 400 == 0:
        print("Год является високосным")
    else:
        print("Год не является високосным")
else:
    print("Год является високосным")