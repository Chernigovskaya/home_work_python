# Задача 1. Дан файл, заполненный числами построчно.
# Считайте файл. Выведите все элементы, стоящие на чётных строках, а потом на нечётных

def read_text():
    data = open('number.txt', encoding='utf-8')
    lines = data.readlines()
    data.close()
    for i in range(0, len(lines), 2):
        print(lines[i], end='')
    print()
    for i in range(1, len(lines), 2):
        print(lines[i], end='')


read_text()
