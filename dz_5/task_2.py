# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа,
# описывающие возрастающую последовательность. Порядок элементов менять нельзя.
import random
lst = [random.randint(1, 10) for i in range(6)]
print(lst)


def get_up(lst, el):
    res = []
    for i in range(el-1, len(lst)):
        if lst[i] == max(lst[:i+1]) and lst[i] not in res:
            res.append(lst[i])
    print(res)


get_up(lst, 1)
get_up(lst, 2)


