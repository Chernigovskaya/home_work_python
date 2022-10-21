# Задача 0. Создайте файл random.txt. Запишите в него 10 случайных чисел

import random
# num = []
# for i in range(10):
#     num.append(random.randint(1, 10))
# print(num)
#
# with open('random.txt', 'w') as data:
#     data.writelines(str(num))


# Задача 1. Создайте кортеж, заполненный случайными числами. Напишите метод, который заменяет элемент в кортеже по заданному индексу.

size = random.randint(5, 12)
num = tuple(random.randint(1, 100) for i in range(size))
print(size)
print(num)

index = int(input('Введите индекс элемента, который ходите изменить: '))


def change_ind(number, index):

    new = list(number)
    new[index - 1] = random.randint(1, 100)
    return tuple(new)


res = change_ind(num, index)
print(res)
