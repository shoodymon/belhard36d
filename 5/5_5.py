# Подсчитать среднее арифметическое N чисел, вводимых с клавиатуры

try:
    count_of_numbers = int(input('Количество чисел: '))
except ValueError:
    print('Вы ввели не число, попробуйте еще раз!')

list_of_numbers = []
for i in range(count_of_numbers):
    print('Введите число: ', end= '')
    list_of_numbers.append(int(input()))

# Вывод введенных нами чисел с клавиатуры
# for i in range(count_of_numbers):
#     print(list_of_numbers[i], end= ' ')

sum_of_numbers = sum(list_of_numbers)
average_of_numbers = sum_of_numbers / count_of_numbers
print('Среднее арифметическое чисел = ', average_of_numbers)
