# Задача 1. Постройте график функции𝑓(𝑥)=5𝑥^2+10𝑥−30
# По графику определите, при каких значения x значение функции отрицательно.

from matplotlib import pyplot as plt

x = list(x for x in range(-10, 10))
y = list(5 * a**2 + 10 * a - 30 for a in x)

print(x)
print(y)
x_lst = []
y_lst = []
for i in range(len(y)):
    if y[i] < 0:
        x_lst.append(x[i])
        y_lst.append(y[i])
print(x_lst)
print(y_lst)

plt.plot(x, y)
plt.plot(x_lst, y_lst)
plt.xlabel('X')
plt.ylabel('Y') 
plt.show()

