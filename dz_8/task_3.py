# В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год. Каждому месяцу соответствует своя строка.
# Определите самый жаркий и самый холодный 7-дневный промежуток этого периода. Выведите его даты.

import numpy as np
import random
may = [round(random.random() * 20, 1) for i in range(31)]
june = [round(random.random() * 30, 1) for i in range(30)]
july = [round(random.random() * 40, 1) for i in range(31)]
august = [round(random.random() * 30, 1) for i in range(31)]
september = [round(random.random() * 20, 1) for i in range(30)]
mons = [may, june, july, august, september]
mons = sum(mons, [])
res = []
for j in range(len(mons)):
    sum_j = round(sum(mons[j:j+7])/7, 2)

    res.append(sum_j)

max_el = max(res)
max_in = res.index(max_el)
min_el = min(res[:-6])
min_in = res.index(min_el)
if max_in < 31:
    print(f'самая жаркая неделя была с {max_in+1} по {max_in +1 + 7} мая, Tcp = {max_el}')
elif 31 < max_in < 62:
    print(f'самая жаркая неделя была с {max_in-30} по {max_in -30 + 7} июня, Tcp = {max_el}')
elif 61 < max_in < 93:
    print(f'самая жаркая неделя была с {max_in-60} по {max_in -60 + 7} июля, Tcp = {max_el}')
elif 92 < max_in < 124:
    print(f'самая жаркая неделя была с {max_in-91} по {max_in -91 + 7} августа, Tcp = {max_el}')
elif max_in > 123:
    print(f'самая жаркая неделя была с {max_in-122} по {max_in -122 + 7} сентября, Tcp = {max_el}')


if min_in < 31:
    print(f'самая холодная неделя была с {min_in+1} по {min_in +1 + 7} мая, Tcp = {min_el}')
elif 31 < min_in < 62:
    print(f'самая холодная неделя была с {min_in-30} по {min_in-30 + 7} июня, Tcp = {min_el}')
elif 61 < min_in < 93:
    print(f'самая холодная неделя была с {min_in-60} по {min_in-60 + 7} июля, Tcp = {min_el}')
elif 92 < min_in < 124:
    print(f'самая холодная неделя была с {min_in-91} по {min_in-91 + 7} августа, Tcp = {min_el}')
elif min_in > 123:
    print(f'самая холодная неделя была с {min_in-122} по {min_in-122 + 7} сентября, Tcp = {min_el}')
# print(min_in)
# print(max_in)
# print(res)





