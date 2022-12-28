# **Вывести четные числа от 2 до N по 5 в строку

try:
    number_n = int(input('N = '))
except ValueError:
    print('Вы ввели не число, попробуйте еще раз!')

for number_per_line in range (2, number_n, 10):
    for number_in_column in range(number_per_line, number_per_line+9, 2):
        if number_in_column <= number_n:
            print(number_in_column, end=' ')
        else:
            break
    print()
