# random — модуль для генерации случайных чисел
import random

numbers = [random.randint(1, 100) for _ in range(10)]
print("До сортировки:", numbers)

# Сортировка пузырьком
n = len(numbers)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("После сортировки:", numbers)