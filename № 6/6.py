# Определение функции f(x)
def f(x):
    return 3 / x - 2 * x


# Точка, в которой вычисляются производные
C = 2.34

# Вычисление первой производной
proizvod1 = (f(C + 1) - f(C - 1)) / ((C + 1) - (C - 1) * 2)

# Вычисление второй производной 
proizvod2 = (f(C + 1) - 2 * f(C) + f(C - 1)) / ((C + 1) - (C - 1) ** 2)

# Вывод результатов
print(f'Первая производная функции в точке {C} --> {proizvod1}')
print(f'Вторая производная функции в точке {C} --> {proizvod2}')
