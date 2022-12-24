# Вводится с клавиатуры десятичная дробь (пример "10/3") необходимо вычислить значение данной дроби (3.333)

string = input()
new_string = string.split('/')
answer = int(new_string[0]) / int(new_string[1])
print(answer)