# Задача 3. Выведите число π с заданной точностью. Точность вводится пользователем в виде натурального числа

from math import pi

num = int(input('Укажите, с какой точностью определить число Пи: '))


def round_pi(num):
    res = round(pi, num)
    return res


print(round_pi(num))
