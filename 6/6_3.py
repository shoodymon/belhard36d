# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]

def foo(number):
    list_of_elements = [1, 2, 3, 4, 5, 6, 7]
    for i in range(number):
        deleted_element = list_of_elements.pop()
        list_of_elements.insert(0,deleted_element)
    return list_of_elements

print(foo(3))

