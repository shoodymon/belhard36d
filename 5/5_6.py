# "Угадай число"
# from random import randint
# a = randint(1, 100)
# Данная функция генерирует случайное число в заданном диапазоне,
# необходимо написать игру "угадай число" и сказать сколько попыток ушло на
# это у пользователя

from random import randint
hidden_number = randint(1, 100)
print(hidden_number)

number = int(input('Пробую угадать число: '))

attempt = 1
while number != hidden_number:
    print('Ваша', attempt+1, 'попытка: ', end=' ')
    number = int(input())
    attempt += 1
    if number > hidden_number:
        print('Загаданное число меньше того, что я загадал')

    if number < hidden_number:
        print('Загаданное число больше того, что я загадал')

    if number == hidden_number:
        break

print('Попыток: ', attempt)