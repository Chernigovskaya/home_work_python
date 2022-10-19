# Задача 2. При работе с документацией менеджер допустил ошибку, названия товаров перемешались с ценами.
# Помогите восстановить документ. Порядковый номер товара совпадает с номером цены.

def error_find():
    data = open('text.txt', encoding='utf-8')
    text = data.readline()
    data.close()
    clothes = []
    prices = []
    text = text.split(' ')
    # print(text)
    for i in text:
        if i.isdigit():
            prices.append(i)
        else:
            clothes.append(i)
    # print(prices)
    # print(clothes)
    # text = zip(clothes, prices)
    # print(*text)
    for i in range(len(prices)):
        print(clothes[i], '-', prices[i])


error_find()