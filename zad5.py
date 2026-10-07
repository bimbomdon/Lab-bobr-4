# random — модуль для генерации случайных чисел
import random

# Создаём матрицу 5×5 из случайных чисел от 1 до 9
matrix = [[random.randint(1, 9) for _ in range(5)] for _ in range(5)]

print("Исходная матрица:")
for row in matrix:
    print(row)

# Суммы диагоналей
main_diag = sum(matrix[i][i] for i in range(5))              # главная: i == j
side_diag = sum(matrix[i][4 - i] for i in range(5))          # побочная: i + j == 4

print(f"\nСумма главной диагонали: {main_diag}")
print(f"Сумма побочной диагонали: {side_diag}")

# Транспонирование (строки ↔ столбцы)
transposed = [[matrix[j][i] for j in range(5)] for i in range(5)]

print("\nПосле транспонирования:")
for row in transposed:
    print(row)