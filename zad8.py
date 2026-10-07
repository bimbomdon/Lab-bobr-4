# random — модуль для генерации случайных чисел
import random

numbers = [random.randint(1, 10) for _ in range(15)]
x = int(input("Какое число удалить? "))

print("До удаления:", numbers)

# Удаление элементов, равных x, со сдвигом
new_numbers = []
for num in numbers:
    if num != x:
        new_numbers.append(num)

print(f"Удалено элементов: {len(numbers) - len(new_numbers)}")
print("После удаления:", new_numbers)