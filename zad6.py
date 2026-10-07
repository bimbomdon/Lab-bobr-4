# random — модуль для генерации случайных чисел
import random

rows, cols = 4, 6
# Создаём матрицу 4×6
matrix = [[random.randint(1, 20) for _ in range(cols)] for _ in range(rows)]

print("Исходная матрица:")
for row in matrix:
    print(row)

# Суммы столбцов
col_sums = []
for j in range(cols):
    s = 0
    for i in range(rows):
        s += matrix[i][j]
    col_sums.append(s)

print("\nСуммы по столбцам:", col_sums)

# Столбец с максимальной суммой
max_sum = max(col_sums)
max_col_index = col_sums.index(max_sum)

print(f"Максимальная сумма: {max_sum} (в столбце с индексом {max_col_index})")