# Дана квадратная матрица, заполненная случайными числами.
# Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.
import numpy as np
size = int(input('Введите размер матрицы: '))
numbers = np.random.randint(10, size=(size, size))
sum_diag = np.trace(numbers)
# print(sum_diag)
list_sum = []
for rows in numbers:
    res = sum(rows)
    list_sum.append(res)
# print(list_sum)
print(numbers)
for el in range(len(list_sum)):
    if list_sum[el] > sum_diag:
        print(f'сумма {el+1} строки больше суммы главной диагонали')


