# Даны два файла, в каждом из которых находится запись многочлена. Найдите сумму данных многочленов.

with open('file_1.txt', 'w', encoding='utf-8') as data_1:
    data_1.write('5x + 3x')
with open('file_2.txt', 'w', encoding='utf-8') as data_2:
    data_2.writelines('3x^2 + x + 8 + 6')

with open('file_1.txt', 'r', encoding='utf-8') as data_1:
    text_1 = data_1.read().split()
    print(text_1)

with open('file_2.txt', 'r', encoding='utf-8') as data_2:
    text_2 = data_2.read().split()
    # text_2 = set(text_2)
    print(text_2)

res = text_2 + text_1
for i in res:
    if i.isdigit():
        print(i)

print(res)
