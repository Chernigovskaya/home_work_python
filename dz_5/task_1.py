# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.
import random
lst = [random.randint(1, 10) for i in range(10)]
more_five = lambda x: x > 5
result = list(filter(more_five, lst))
print(lst)
print(result)
