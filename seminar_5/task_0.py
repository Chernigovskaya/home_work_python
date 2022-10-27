'''
# Задача 0. С помощью анонимной функции найдите в списке на 15 элементов числа, кратные 5. Заполните список случайным образом числами от 1 до 100.

import random

num = [random.randint(1, 100) for i in range(15)]
print(num)

result = lambda x: x % 5 == 0
result = list(filter(result, num))

print(result)

'''

# Задача 1. На вход подаётся четырёхзначное число. Получите список, состоящий из цифр данного числа, увеличенных на 10.
num = list(input('Введите число: '))
print(num)
plus_ten = lambda i: int(i) + 10
res = list(map(plus_ten, num))
print(res)


