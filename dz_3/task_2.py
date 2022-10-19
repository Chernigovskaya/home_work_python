#Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.

data = open('fruits.txt', 'r', encoding='utf-8')

text = data.read().split()

data.close()
# print(text)


def find_fruits(letter):
    for i in text:
        if i.lower()[0] == letter:
            print(i, end=', ')
    print()


find_fruits('а')
find_fruits('о')
