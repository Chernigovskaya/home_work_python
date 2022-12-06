# Задача 2. Тренер секции по стрельбе получил результаты выступления своих спортсменов, где каждое очко означает поражённый сектор.
# Помогите ему сымитировать по имеющимся данным поражённые мишени

from matplotlib import pyplot

n = [4, 6, 10, 4, 2, 8, 10, 7, 1, 5]
a = [3, 3, 10, 5, 10, 10, 4, 3, 6, 1]
p = [2, 2, 1, 1, 3, 7, 9, 9, 2, 8]

max_val = 10
n = list(max_val - i for i in n)
a = list(max_val - i for i in a)
p = list(max_val - i for i in p)

ax = pyplot.subplot(131, projection='polar')
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_ticks([0, 2, 4, 6, 8, 10])
ax.get_yaxis().set_ticklabels(['10', '8', '6', '4', '2', '0'])
pyplot.plot(n, 'ro')

ax = pyplot.subplot(132, projection='polar')
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_ticks([0, 2, 4, 6, 8, 10])
ax.get_yaxis().set_ticklabels(['10', '8', '6', '4', '2', '0'])
pyplot.plot(a, 'ro')

ax = pyplot.subplot(133, projection='polar')
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_ticks([0, 2, 4, 6, 8, 10])
ax.get_yaxis().set_ticklabels(['10', '8', '6', '4', '2', '0'])
pyplot.plot(p, 'ro')

pyplot.show()