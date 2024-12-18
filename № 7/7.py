import math


def f(x):
    return math.cos(x)


z = 0


a = float(input('Введите a : '))
b = float(input('Введите b : '))
n = int(input('Теперь введите n : '))

h = (b - a) / n


for i in range(n):
    z += f(a + h * i)
print(f'Методом левых пямоугольников --> {h * z}')

z = 0
for i in range(1, n + 1):
    z += f(a + h * i)
print(f'Методом правых пямоугольников --> {h * z}')

z = 0
for i in range(1, n):
    z += f(a + i * h)
print(f'Методом трапеции --> {h * (f(a) / 2 + f(b) / 2 + z)}')


#   : )
