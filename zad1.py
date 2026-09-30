numbers = []  # Создаем пустой список

print("Введите 10 чисел по очереди:")

# Цикл повторяется ровно 10 раз (от 0 до 9)
for i in range(10):
    while True:  # Бесконечный цикл, пока не введут правильное число
        try:
            # input() считывает текст, float() превращает его в число
            num = float(input(f"Число {i + 1}: "))
            numbers.append(num)  # .append() добавляет число в конец списка
            break  # Если всё ок, выходим из внутреннего цикла while
        except ValueError:
            print("Ошибка! Введите именно число.")

total_sum = sum(numbers)
average = total_sum / len(numbers)
min_val = min(numbers)
min_index = numbers.index(min_val)
max_val = max(numbers)
max_index = numbers.index(max_val)

print("-" * 30)
print(f"Ваш массив: {numbers}")
print(f"Сумма:    {total_sum}")
print(f"Среднее:  {average}")
print(f"Минимум:  {min_val} (индекс {min_index})")
print(f"Максимум: {max_val} (индекс {max_index})")