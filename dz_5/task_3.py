# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают.Список уникальных элементов
# [1, 4, 2, 3, 6, 7]
import random


lst = [random.randint(1, 10) for i in range(10)]
print(lst)


def count_repeat(nums):
    res = {i: nums.count(i) for i in nums if nums.count(i) > 1}
    total = sum(res.values())
    print(f'совпадающих элементов есть в списке: {total}')
    print(res)


def del_repeat(nums):
    nums = set(nums)
    nums = list(nums)
    print(f'Список уникальных элементов: {nums}')


count_repeat(lst)
del_repeat(lst)
