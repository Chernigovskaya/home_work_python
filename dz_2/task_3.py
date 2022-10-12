# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки
# встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

def count_equality_el(str_1, str_2):
    for i in str_1:
        count = str_2.count(i)
        if count > 0:
            print(i, '-', count)


count_equality_el('one', 'onetwonine')



