# Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


number = int(input("Введите число: "))


def multipliers(num):
    i = 2
    lst = []
    while i <= num:
        if num % i == 0:
            lst.append(i)
            num = num // i

        else:
            i += 1
    print(lst)


multipliers(number)
