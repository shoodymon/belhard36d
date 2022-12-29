# Реализовать бинарный поиск по упорядоченному списку,
# суть бинарного поиска заключается в дроблении списка на половину

from random import randint

list_of_elements = []

for i in range(12):
    list_of_elements.append(randint(1, 100))

list_of_elements.sort()
print(list_of_elements)

value = int(input())

position_of_low_number = 0
position_of_middle_number = len(list_of_elements) // 2
position_of_high_number = len(list_of_elements) - 1

while list_of_elements[position_of_middle_number] != value and position_of_low_number <= position_of_high_number:
    if value < list_of_elements[position_of_middle_number]:
        position_of_high_number = position_of_middle_number - 1
    else:
        position_of_low_number = position_of_middle_number + 1
    position_of_middle_number = (position_of_low_number + position_of_high_number) // 2

if position_of_low_number < position_of_high_number:
    print('Ваше число имеет позицию: ', position_of_middle_number)
else:
    print('Такого числа нет в списке!')
