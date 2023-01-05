# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно

collection = [1, 2, 3, 'hello', 21.42, False, 'python', 1, 3, 'world', 1, 3, 'pycharm']
print(collection)

def foo(collection):
    for elements in collection:
        flag = isinstance(elements, str)
        if flag:
            print(elements, end= ' ')

foo(collection)

collection = list(filter(lambda elements: isinstance(elements, str), collection))
print(collection)
