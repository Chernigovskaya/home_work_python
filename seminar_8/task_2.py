# Дан двумерный массив. Определите
# номер строки и столбца, в котором находится
# максимальный элемент.
import numpy as np
numbers = np.random.randint(50, size=(10, 15))

print(numbers)

max_i = 0
max_j = 0

for i in range(numbers.shape[0]):
    for j in range(numbers.shape[1]):
        if numbers[i, j] > numbers[max_i, max_j]:
            max_i, max_j = i, j

print(max_i + 1, max_j + 1)
