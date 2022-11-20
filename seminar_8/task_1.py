import random
import numpy


def print_matrix(numbers):
    for row in numbers:
        print(row)


def matrix_rand():
    rows = 4
    columns = 5
    numbers = [0] * rows
    used = []
    for i in range(len(numbers)):
        numbers[i] = list(None for _ in range(columns))

    for i in range(rows):
        for j in range(columns):
            current_number = random.randint(0, 300)
            while current_number in used:
                current_number = random.randint(0, 300)
            numbers[i][j] = current_number
            used.append(current_number)
    return numbers

    # print(numbers[0][3])


def zadacha_2():
    numbers = matrix_rand()
    print_matrix(numbers)
    result = []
    for rows in numbers:
        for el in rows:
            result.append(el)
    result = list(set(result))
    result.sort()
    print(f'{result[-2]}-{result[1]} = {result[-2] - result[1]}')


# zadacha_2()
def zadacha_3():
    seats = numpy.random.randint(2, size=(25, 36))
    print(seats)
    M = int(input('How many people: '))
    K = int(input('The closest row: '))
    N = int(input('The farthest row: '))
    found = False

    for i in range(K, N + 1):
        for j in range(36 - M + 1):
            if 1 not in seats[i, j: j + M + 1]:
                print(seats[i, j: j + M])
                print(i + 1, j + 1)
                found = True
        if found:
            break
        if found:
            break
    else:
        print('No seats')


# zadacha_3()


def zadacha_4():
    numbers = matrix_rand()
    print_matrix(numbers)
    result = []
    for rows in numbers:
        for el in rows:
            result.append(el)
    print(result)
    max_el = max(result)
    print(max_el)
    max_in = result.index(max_el)
    print(max_in)
    row = len(numbers)
    cols = len(numbers[0])
    print(max_in // cols + 1, max_in % cols + 1)


zadacha_4()
