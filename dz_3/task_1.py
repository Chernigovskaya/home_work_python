# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8

data = open('res_fibo.txt', 'w', encoding='utf-8')
nums = int(input('Введите число: '))


def fibonacci(n):
    num_1 = 0
    num_2 = 1
    data.write(f' {n} первых элементов последовательности Фибоначчи:\n')

    for i in range(n+1):
        (num_1, num_2) = (num_2, num_1 + num_2)
        data.writelines(str(num_1) + ' ')


fibonacci(nums)







