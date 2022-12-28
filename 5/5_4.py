# Вводится число, найти его максимальную цифру

number = int(input('N = '))
max_digit = number % 10
number //= 10

while number > 0:
    if number % 10 > max_digit:
        max_digit = number % 10
    number //= 10
print('Максимальная цифра = ', max_digit)
