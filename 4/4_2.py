# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

string = input()
data = {string[i]: string.count(string[i]) for i in range(len(string))}
print(data)
data2 = {i: string.count(i) for i in string}
print(data2)