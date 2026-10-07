# random — модуль для генерации случайных чисел
import random

rows, cols = 3, 4
# Создаём матрицу 3×4
matrix = [[random.randint(1, 50) for _ in range(cols)] for _ in range(rows)]

print("Исходная матрица:")
for row in matrix:
    print(row)

#  Максимум в каждой строке
print("\nМаксимумы в строках:")
for i in range(rows):
    max_in_row = max(matrix[i])
    print(f"Строка {i}: {max_in_row}")

#  Минимум в каждом столбце
print("\nМинимумы в столбцах:")
for j in range(cols):
    # Собираем элементы j-го столбца в список
    column = [matrix[i][j] for i in range(rows)]
    min_in_col = min(column)
    print(f"Столбец {j}: {min_in_col}")