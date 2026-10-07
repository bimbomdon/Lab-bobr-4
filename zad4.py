# random — модуль для генерации случайных чисел
import random

numbers = [random.randint(1, 100) for _ in range(10)]
k = int(input("На сколько позиций сдвинуть вправо? "))

print("До сдвига:", numbers)

# Циклический сдвиг вправо на k позиций
n = len(numbers)
k = k % n  # если k больше длины массива, берём остаток
numbers = numbers[-k:] + numbers[:-k]

print("После сдвига:", numbers)