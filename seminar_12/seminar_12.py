import random

import numpy as np
import matplotlib.pyplot as plt

# Проверьте, существует ли связь между данными, приведёнными в таблице.
# Выполните задание с помощью графика и библиотеки numpy.


def zadacha1():
    num_1 = [56, 37, 48, 45, 46, 43, 41, 45, 47, 48, 57, 63]
    num_2 = [66, 46, 46, 54, 57, 51, 52, 54, 57, 54, 68, 72]
    num_3 = [89, 67, 65, 77, 79, 68, 74, 75, 77, 77, 91, 96]
    matrix = [num_1, num_2, num_3]

    res = np.corrcoef(matrix)

    print(res)

    plt.plot(num_1, 'r')
    plt.plot(num_2, 'g')
    plt.plot(num_3, 'b')
    plt.show()

# Дан массив случайных чисел. Создайте его с помощью NumPy. Определите его среднее арифметическое.
# На ввод подаётся число. Определите ближайший по значению к нему элемент массива.
def zadacha2():
    num_list = np.random.randint(1, 100, 20) #+ np.random.random(6)
    print(num_list)
    mean = np.mean(num_list)
    print(mean)
    # difference1 = [num_list[i] - mean for i in range(len(num_list))]
    difference = [np.abs(i - mean) for i in num_list]

    print(difference)
    print(np.min(difference))
    print(np.argmin(difference))
    print(f"ближайший к {mean} жлемент равен {num_list[np.argmin(difference)]}. его позиция {np.argmin(difference) + 1}")

# Задайте квадратную матрицу, состоящую из случайных чисел. Найдите самый часто встречающийся элемент в этой матрице
def zadacha():
    random_list = np.random.randint(1, 10, (4, 4))
    print(random_list)
    uniq, count = np.unique(random_list, return_counts=True)
    print(uniq)
    print(count)
    max_count = np.max(count)
    ind_max_count = np.argmax(count)
    print(f'{uniq[ind_max_count]} наиболее часто встречается, оно встречается {max_count} раз')

# Задача 4. Дан двумерный массив. Определите есть ли в нём нулевые столбцы.

martix = np.random.randint(0, 2, (3, 7))
print(martix)
print(martix.any(axis=0))
martix = martix.any(axis=0)
martix = ~martix  # ~ обратная функция
# print(martix.any(axis=1))
print(martix)
print(martix.any())

