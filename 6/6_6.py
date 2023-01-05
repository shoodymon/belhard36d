# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные

numbers = [1, 4, 5, 7, 10, 14, 53, 46, 76, 89, 91]
print(numbers)
def sort(numbers):
    numbers = list(filter(lambda x: not x % 2, numbers)) + list(filter(lambda x: x % 2, numbers))
    return numbers

print(sort(numbers))

elements = [1, 4, 5, 7, 10, 14, 53, 46, 76, 89, 91]
print(elements)

new_list = []
def second_sort(elements):
    for i in elements:
        if i % 2 == 0:
            new_list.insert(0, i)
        else:
            new_list.append(i)
    return new_list

print(second_sort(elements))
