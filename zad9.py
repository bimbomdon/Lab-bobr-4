# random — модуль для генерации случайных чисел
import random

numbers = [random.randint(1, 50) for _ in range(15)]
print("Исходный массив:", numbers)

# Разделение на чётные и нечётные
evens = []   # для чётных (делятся на 2 без остатка)
odds = []    # для нечётных

for num in numbers:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

# Сортировка каждого списка по возрастанию
evens.sort()
odds.sort()

print("\nЧётные (отсортированы):", evens)
print("Нечётные (отсортированы):", odds)