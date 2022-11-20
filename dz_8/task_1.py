#  В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки заносятся в таблицу.
#  Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.

import random


def print_matrix(numbers):
    for row in numbers:
        print(row)


def matrix_rand():
    count_student = random.randint(20, 30)
    count_grop = 5
    numbers = [0] * count_grop
    res = []
    for i in range(len(numbers)):
        numbers[i] = list(random.randint(2, 5) for i in range(count_student))
        medium = sum(numbers[i]) / count_student
        res.append(medium)
    # print(res)
    for _ in res:
        result = res.index(max(res))
    print(f'{result + 1} группа имеет наилучшую успеваемость')
    return numbers


matrix_rand()
# numbers = matrix_rand()
# print_matrix(numbers)

