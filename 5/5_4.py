# Вводится число, найти его максимальную цифру

try:
    number = int(input('N = '))
except ValueError:
    print('Вы ввели не число, попробуйте еще раз!')

max_digit = number % 10
number //= 10

while number > 0:
    if number % 10 > max_digit:
        max_digit = number % 10
    number //= 10
print('Максимальная цифра = ', max_digit)
