# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def factorial_list(num):
    factorial = 1
    for i in range(1, num+1):
        factorial *= i
        print(factorial, end=', ')
    print()


factorial_list(4)
factorial_list(5)
