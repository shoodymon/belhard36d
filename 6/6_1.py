# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int

# reminder(остаток) берем не как список, потому что придется извлекать и преобразовывать к строковому виду, собирать
# соединять, поэтому берем как строку, чтобы присоединять к строке каждый новый остаток
def decimal_to_binary(number, reminder = ''):
    while number > 0:
        reminder = str(number % 2) + reminder
        number //= 2
    return int(reminder)

print(decimal_to_binary(int(input())))

def binary_to_decimal(binary_number, decimal_number = 0):
    length_of_number = len(binary_number)
    for i in range(0, length_of_number):
        decimal_number = decimal_number + int(binary_number[i]) * (2 ** (length_of_number - i - 1))
    return decimal_number

print(binary_to_decimal(input()))