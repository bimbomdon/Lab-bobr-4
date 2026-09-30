# random — модуль для генерации случайных чисел
import random

numbers = [random.randint(-20, 20) for _ in range(10)]
print("Исходный:", numbers)

# Подсчёт
positive = sum(1 for n in numbers if n > 0)
negative = sum(1 for n in numbers if n < 0)
zeros = numbers.count(0)

# Обмен min ↔ max
min_idx = numbers.index(min(numbers))
max_idx = numbers.index(max(numbers))
numbers[min_idx], numbers[max_idx] = numbers[max_idx], numbers[min_idx]

# Вывод
print(f"Положительных: {positive}, отрицательных: {negative}, нулей: {zeros}")
print(f"Min: {min(numbers)} (индекс {min_idx})")
print(f"Max: {max(numbers)} (индекс {max_idx})")
print("После обмена:", numbers)
