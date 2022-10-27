# Задача 3. Имеется информация о том, телефонами каких компаний сейчас торгуют магазины.
# Определите те компании, чьи телефоны присутствуют в каждом магазине.

with open('tel.txt', 'r', encoding='utf_8') as data:
    tel = data.readlines()

    shop_1 = set(tel[1].replace('\n', '').split(', '))
    shop_2 = set(tel[3].replace('\n', '').split(', '))
    shop_3 = set(tel[5].replace('\n', '').split(', '))
    print(shop_1.intersection(shop_2).intersection(shop_3))
   
