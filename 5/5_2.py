# сделать калькулятор: пользователь вводит число затеи действие и второе число

number1 = int(input('Введите первое число: '))
operation = input('+, -, *, /, **: ')
number2 = int(input('Введите второе число: '))

if operation == '+':
    result = number1 + number2

elif operation == '-':
    result = number1 - number2

elif operation == '*':
    result = number1 * number2

elif operation == '/':
    if number2 == 0:
        print('На ноль делить нельзя!')
    else:
        result = number1 / number2

elif operation == '**':
    result = number1 ** number2
else:
    print('Ошибка!')
print('Равно: ', result)
