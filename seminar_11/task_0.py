# Задача 1. Имеются данные о продаже компьютеров компаний «Ашечка» и «Бэшечка» за последние 6 лет.
# Спрогнозируйте, через сколько лет объёмыпродаж этих компаний сравняются.
from matplotlib import pyplot


first_conp = [1743, 1648, 1650, 1622, 1581, 1490]
second_conp = [743, 648, 711, 780, 805, 846]


def find_trend(comp):
    trend = []
    for i in range(len(comp) - 1):
        trend.append(comp[i+1] - comp[i])
    return trend


first_trend = find_trend(first_conp)
second_trend = find_trend(second_conp)
print(first_trend)
print(second_trend)

first_mean = 0
for el in first_trend:
    first_mean = first_mean + el
first_mean = first_mean / len(first_trend)
print(f'первая компания растет на {first_mean}')

second_mean = 0
for el in second_trend:
    second_mean = second_mean + el
second_mean = second_mean / len(second_trend)
print(f'вторая компания растет на {second_mean}')


def find_period(comp, mean):
    period = 10
    for i in range(period):
        comp.append(comp[-1] + mean)
    return comp


first_res = find_period(first_conp, first_mean)
#print(first_res)
second_res = find_period(second_conp, second_mean)
#print(second_res)

pyplot.plot(first_res)
pyplot.plot(second_res)
pyplot.show()
