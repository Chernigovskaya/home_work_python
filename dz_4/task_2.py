#Задача 2. В первой строке файла находится информация об ассортименте мороженного,
# во второй - информация о том, какое мороженное есть на складе.
# Выведите названия того товара, который закончился.


with open('file.txt', 'w', encoding='utf-8') as data:
    data.writelines('«Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»' + '\n')
    data.writelines('«Сливочное», «Вафелька», «Сладкоежка»' + '\n')

with open('file.txt', 'r', encoding='utf-8') as data:
    exist = str(data.readlines(1))[2:-4].replace('«', '').replace('»', '').split(', ')
    exist = set(exist)
    stock = str(data.readlines(2))[2:-4].replace('«', '').replace('»', '').split(', ')
    stock = set(stock)

print(exist)
print(stock)

res = exist - stock

print(f'закончился товар - {res}')

