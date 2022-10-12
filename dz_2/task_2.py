# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.
def task_2():
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                res = not(x and y) or z
                print(x, y, z, int(res))


task_2()
