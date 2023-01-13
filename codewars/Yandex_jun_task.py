# TODO Удалить повторяющиеся элементы в сортированном списке
#  [0, 0, 0, 1, 1, 2, 2, 2, 3, 3]

numbers = [0, 0, 0, 1, 1, 2, 2, 2, 3, 3]
print(numbers)

def remove_dublicates(numbers: list[int]) -> list[int]:
    first_pointer = 0
    second_pointer = 0

    while second_pointer < len(numbers):
        while second_pointer < len(numbers) - 1 and numbers[second_pointer] == numbers[second_pointer + 1]:
            second_pointer += 1

        numbers[first_pointer] = numbers[second_pointer]
        first_pointer += 1
        second_pointer += 1

    return numbers[:first_pointer]

print(remove_dublicates(numbers))