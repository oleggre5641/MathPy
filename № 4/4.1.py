import numpy as np

# Определяем матрицу коэффициентов A и вектор свободных членов b
A = np.array([[4, -3, 2],
              [2, 5, -3],
              [5, 6, -2]])

b = np.array([3, 7, 8])

# Вычисляем определитель основной матрицы
det_A = np.linalg.det(A)

# Проверяем, что определитель не равен нулю
if det_A == 0:
    print("Система не имеет единственного решения.")
else:
    # Вычисляем определители для каждой переменной
    det_x = np.linalg.det(np.column_stack((b, A[:, 1], A[:, 2])))
    det_y = np.linalg.det(np.column_stack((A[:, 0], b, A[:, 2])))
    det_z = np.linalg.det(np.column_stack((A[:, 0], A[:, 1], b)))

    # Находим решение по формуле Крамера
    x = det_x / det_A
    y = det_y / det_A
    z = det_z / det_A

    print(f"Решение системы: x = {x}, y = {y}, z = {z}")

#    : )
