def round_number_with_pogreshn(number, delta, is_relative=False):
    if is_relative:
        # Если погрешность относительная, вычисляем абсолютную погрешность
        delta_a = number * delta
    else:
        # Иначе используем заданную абсолютную погрешность
        delta_a = delta

    # Определяем количество знаков после запятой
    if delta_a < 0.0005:
        rounded_number = round(number, 4)
    elif delta_a < 0.005:
        rounded_number = round(number, 3)
    elif delta_a < 0.05:
        rounded_number = round(number, 2)
    elif delta_a < 0.5:
        rounded_number = round(number, 1)
    else:
        rounded_number = round(number)

    # Вычисляем округленную погрешность
    delta_rounded = abs(rounded_number - number)

    # Обновляем предельную абсолютную погрешность
    delta_a_rounded = delta_a + delta_rounded

    # Проверяем, является ли полученная погрешность верной в широком или узком смысле
    if delta_a_rounded < 0.0005:
        return rounded_number, delta_a_rounded, "верные в узком смысле"
    elif delta_a_rounded < 0.005:
        return rounded_number, delta_a_rounded, "верные в широком смысле"
    elif delta_a_rounded < 0.05:
        return rounded_number, delta_a_rounded, "верные в широком смысле"
    elif delta_a_rounded < 0.5:
        return rounded_number, delta_a_rounded, "верные в широком смысле"
    else:
        return rounded_number, delta_a_rounded, "верные в широком смысле"

# Задача А
number_a = 8.24163
delta_a = 0.002  # Это как 0,2%
result_a = round_number_with_pogreshn(number_a, delta_a, is_relative=True)
print(f"Задача a): {result_a[0]} с погрешностью {result_a[1]:.7f} - {result_a[2]}")

# Задача Б
number_b = 0.12356
delta_b = 0.00036
result_b = round_number_with_pogreshn(number_b, delta_b)
print(f"Задача б): {result_b[0]} с погрешностью {result_b[1]:.7f} - {result_b[2]}")

#    : )
