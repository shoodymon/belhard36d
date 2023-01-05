# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза

numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers)

def foo(numbers):
    for element in range(len(numbers) // 2):
        position_of_exchangeable_element = len(numbers) - element - 1
        temp = numbers[element]
        numbers[element] = numbers[position_of_exchangeable_element]
        numbers[position_of_exchangeable_element] = temp
        # numbers[element], numbers[position_of_exchangeable_element] = numbers[position_of_exchangeable_element], numbers[element]
    return numbers

print(foo(numbers))
