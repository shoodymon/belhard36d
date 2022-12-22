# Пользователь вводит 3 числа, сказать сколько из них положительных
# и сколько отрицательных

# Вариант решения задачи через условный оператор if
number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
number3 = int(input('Введите третье число: '))
count_of_positive_numbers = 0
count_of_negative_numbers = 0
if number1 > 0:
    count_of_positive_numbers += 1
else:
    count_of_negative_numbers += 1
if number2 > 0:
    count_of_positive_numbers += 1
else:
    count_of_negative_numbers += 1
if number3 > 0:
    count_of_positive_numbers += 1
else:
    count_of_negative_numbers += 1
print('Положительных чисел: ', count_of_positive_numbers)
print('Отрицательных чисел: ', count_of_negative_numbers)

# Решение задачи, где учтем, что при сложении типа bool ответ приведет его в int
number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
number_3 = int(input('Введите третье число: '))
check = (number_1 > 0) + (number_2 > 0) + (number_3 > 0)
print(f"Кол-во положительных чисел: {check}. Кол-во отрицательных чисел: {3 - check}")