import numpy as np

# Определяем матрицу коэффициентов A и вектор свободных членов b
A = np.array([[4, -3, 2],
              [2, 5, -3],
              [5, 6, -2]], dtype=float)

b = np.array([3, 7, 8], dtype=float)


# Функция для приведения матрицы к верхнетреугольному виду (прямой ход)
def gaussian_elimination(A, b):
    n = len(A)
    for i in range(n):
        # Поиск максимального элемента в столбце
        max_row = np.argmax(np.abs(A[i:, i])) + i
        # Перестановка строк
        A[[i, max_row]] = A[[max_row, i]]
        b[[i, max_row]] = b[[max_row, i]]

        # Обнуление столбца под текущей строкой
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]

    return A, b


# Функция для обратного хода (нахождения решения)
def back_substitution(A, b):
    n = len(A)
    x = np.zeros(n, dtype=float)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]
    return x


# Применяем метод Гаусса
A_upper, b_upper = gaussian_elimination(A.copy(), b.copy())

# Находим решение
solution = back_substitution(A_upper, b_upper)
print(f"Решение системы: x = {solution[0]}, y = {solution[1]}, z = {solution[2]}")

#    : )
