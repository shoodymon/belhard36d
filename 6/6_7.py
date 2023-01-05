# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка

numbers = [1, 4, 5, 7, 10, 14, 53, 46, 76, 89, 91]
print(numbers)

def sum_of_numbers(numbers):
    result = []
    for i in range(len(numbers)):
        if i < len(numbers) - 1:
            result.append(numbers[i-1] + numbers[i+1])
        else:
            result.append(numbers[i-1] + numbers[0])
    return result

print(sum_of_numbers(numbers))
