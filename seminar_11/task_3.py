# Задача 3. Данные торговых точек говорят, что годовая зависимость спроса на кофе определяется формулой:
# 𝑦=𝑎^2 𝑥+3000
# где:
# y – спрос на кофе
# x – объём стаканчика
# a – количество сахара
# Сколько, примерно, сахара нужно добавлять, чтобыкофе объёмом 120 мл покупали 5500 человек,
# а объёмом 205 мл – 6500 человек в год?

from matplotlib import pyplot

x = [120, 205]

for i in x:
    people = [i * a * a + 3000 for a in range(0, 10)]
    pyplot.plot(people)


pyplot.title('Зависимость спроса от сахара')
ax = pyplot.subplot(211)
plot1 = [5500 for a in range(0, 20)]
line, = pyplot.plot(plot1)
line.set_label('требуемый спрос')

people = [x[0] * a * a + 3000 for a in range(0, 10)]
line, = pyplot.plot(people)
line.set_label('спрос от сахара')
ax.legend()

ax = pyplot.subplot(212)
plot1 = [6500 for a in range(0, 20)]
line, = pyplot.plot(plot1)
line.set_label('требуемый спрос')

people = [x[1] * a *a + 3000 for a in range(0, 10)]
line, = pyplot.plot(people)
line.set_label('спрос от сахара')
ax.legend()

# pyplot.title('Зависимость спроса от сахара')
pyplot.xlabel('сахар')
pyplot.ylabel('спрос')

pyplot.show()