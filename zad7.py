# random — модуль для генерации случайных чисел
import random

rows, cols = 4, 5
# Создаём матрицу 4×5 из чисел от 1 до 20
matrix = [[random.randint(1, 20) for _ in range(cols)] for _ in range(rows)]

print("Исходная матрица:")
for row in matrix:
    print(row)

# Поиск седловых точек
# Седловая точка: элемент является минимумом в своей строке И максимумом в своем столбце
found = False

for i in range(rows):
    # 1. Находим минимум в текущей строке i
    min_val = min(matrix[i])
    
    # 2. Ищем все индексы этого минимума в строке (на случай повторов)
    min_indices_in_row = [j for j in range(cols) if matrix[i][j] == min_val]
    
    # 3. Для каждого такого элемента проверяем, является ли он максимумом в своем столбце
    for j in min_indices_in_row:
        # Собираем весь столбец j
        column = [matrix[r][j] for r in range(rows)]
        max_in_col = max(column)
        
        # Если элемент равен максимуму столбца — это седловая точка
        if min_val == max_in_col:
            print(f"\nНайдена седловая точка: {min_val} (строка {i}, столбец {j})")
            found = True

if not found:
    print("\nСедловых точек нет.")