# Сгенерируйте список случайных чисел от 1 до 20, состоящий из 10 элементов. Удалите из списка дубликаты уже имеющихся элементов.
import random
# my_list = []
# len_l = 10
#
# for i in range(len_l):
#     my_list.append(random.randint(1, 20))
# print(my_list)
# print(set(my_list))


def get_numbers():
    with open('list.txt', 'a', encoding='utf-8') as data:
        num = [random.randint(1, 20) for i in range(0, 10)]
        data.write((str(num)))
        return num


def find_numbers(my_list):
    with open('list.txt', 'a', encoding='utf-8') as data:
        # num = data.readline()[1:-1].split(',')
        # print(num)
        # num = [int(i) for i in num]
        # print(num)
        # num = set(num)
        # print(num)
        my_list = set(my_list)
        data.write('\n' + (str(my_list)))


find_numbers(get_numbers())
