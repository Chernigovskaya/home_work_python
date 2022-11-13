# . Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.
from math import gcd


def find_fractions(n):
    res = []
    for i in range(2, n + 1):
        for j in range(1, i):
            if gcd(i, j) == 1:
                res.append(f'{j}/{i}')
    return res


print(find_fractions(11))
