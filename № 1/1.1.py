import math

# Точные значения наших чисел
exact_1 = math.sqrt(83)
exact_2 = 6 / 11

# Приближенные значения наших чисел
primerno_1 = 9.11
primerno_2 = 0.545

# Вычисление абсолютных погрешностей чисел
absolut_1 = abs(exact_1 - primerno_1)
absolut_2 = abs(exact_2 - primerno_2)

# Вычисляем отношение абсолютной погрешности к точному значению
otnos_1 = absolut_1 / exact_1
otnos_2 = absolut_2 / exact_2

# Сравнениваем относительные погрешности и выводим что является более точным
if otnos_1 < otnos_2:
    print("Равенство √83 = 9.11 является более точным.")
else:
    print("Равенство 6 / 11 = 0.545 является более точным.")

# Вывод результатов и погрешностей до 5 знаков после запятой
print(f"Относительная погрешность для √83 = 9.11: {otnos_1 * 100:.5f}%")
print(f"Относительная погрешность для 6 / 11 = 0.545: {otnos_2 * 100:.5f}%")

#    : )
