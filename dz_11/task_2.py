# Задача 2. Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000 рублей.
# Предоставьте ему графические данные о стоимости квадратного метра каждого дома и список подходящих ему домов, отсортированных по площади.
# Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров, цены от 3 до 20 млн.
import random
import matplotlib.pyplot as plt


count = 15
number = [i for i in range(1, count+1)]
square = list(random.randint(100, 300) for i in range(count))
price = list(random.randint(3000000, 20000000) for i in range(count))
min_price = 50000
line = [min_price for i in range(count)]
price_metr = []
for i in range(len(square)):
    res = price[i] / square[i]
    price_metr.append(res)


houses = dict(zip(number, price_metr))

# print(square)
# print(price)
# print(price_metr)
# print(houses)

res_number = []
res_square = []
res_metr = []
res_price = []

for i in range(count):
    if price_metr[i] < min_price:
        res_number.append(number[i])
        res_price.append(price[i])
        res_square.append(square[i])
        res_metr.append(price_metr[i])

print(f'Дома стоимостью за квадратный метр менее {min_price}: ')
for i in range(len(res_number)):
    print(f'дом № {res_number[i]}, площадью {res_square[i]} м2, стоимостью {res_price[i]} руб (стоимоcть за квадратный метр {round(res_metr[i])} руб/м2)')


# for key, val in houses.items():
#     if val < min_price:
#         print(f'дом № {key}, стоимость за квадратный метр составляет {round(val)} рублей')



fig, ax = plt.subplots()

ax.bar(number, price_metr)
plt.plot(number, line, 'r')
ax.set_facecolor('seashell')
fig.set_facecolor('floralwhite')
plt.ylabel('Стоимость')
plt.xlabel('№ дома')

# plt.plot(number, price_metr, 'o')
plt.show()


