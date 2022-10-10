# Задача 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# from math import sqrt
#
# x_coord_A = float(input('Введите координату точки А по оси Х: '))
# y_coord_A = float(input('Введите координату точки А по оси Y: '))
# x_coord_B = float(input('Введите координату точки B по оси Х: '))
# y_coord_B = float(input('Введите координату точки B по оси Y: '))
#
# distance = round(sqrt((x_coord_B - x_coord_A) ** 2 + (y_coord_B - y_coord_A) ** 2), 2)
# print(distance)


def distance_2d(xa, ya, xb, yb):
    res = round(((xb - xa) ** 2 + (yb - ya) ** 2) ** 0.5, 2)
    print(res)


distance_2d(7, -5, 1, -1)
distance_2d(3, 6, 2, 1)
