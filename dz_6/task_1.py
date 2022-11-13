# Задача 1. Дано натуральное число N. Найдите значение выражения:N + NN + NNN
# N может быть любой длины.
# N = 132:132 + 132132 + 132132132 = 132264396


def result():
    number = int(input('Введите натуральное число: '))
    num = str(number)
    res_1 = num + num
    res_2 = num + num + num
    res = number + + int(res_1) + int(res_2)
    print(res)


result()
