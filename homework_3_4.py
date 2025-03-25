'''Задача 4. Счетчик счастливых чисел Тома'''

# Решение 1
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

x = 0

for i in range(a, b + 1):
    if i // 77 == 0:
        continue
    if i % 77 == 0:
        x += 1
print(x)

# Решение 2
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

def lucky_numbers_in_range(a, b):
    numbers = 0
    for lucky_numbers in range(a, b + 1):
        if lucky_numbers % 77 == 0:
            numbers += 1
    return numbers

result = lucky_numbers_in_range(a, b)
print(result)





