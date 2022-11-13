# Задача 0. Дан список случайных элементов. Проверьте, что все его элементы уникальны.
import random

#
# def zadacha_0():
#     number = [random.randint(1, 10) for i in range(5)]
#     print(number)
#     if len(number) == len(set(number)):
#         print('уникальные')
#     else:
#         print('Есть повторения')
#
#
# zadacha_0()
# Задача 1. Даны два случайных пятизначных числа. Определить, состоят ли они из одних и тех же цифр.

'''    
def zadacha_1(num_1, num_2):
    if check_num(num_1) and check_num(num_2):

        if count_el(num_1) == count_el(num_2):
            print('числа совпадают')
        else:
            print('не совпадают')
    else:
        print('Числа не удовлетворяют условию')


def check_num(num):
    return 10000 <= num <= 99999


def count_el(num):
    num = str(num)
    num = set((i, num.count(i)) for i in set(num))
    print(num)
    return num


num_1 = 23554
num_2 = 45532
zadacha_1(num_1, num_2)

'''


