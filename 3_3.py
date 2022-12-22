# Пользователь вводит Имя, Возраст и Город, сформировать
# приветственное сообщение путем форматирования 3-мя способами

name = input('Name: ')
age = input('Age: ')
town = input('Town: ')
sentence1 = 'Hello %s your age %s you are from %s' % (name, age, town)
sentence2 = 'Hello %(name)s your age %(age)s you are from %(town)s' % {'name': name, 'age': age, 'town': town}
sentence3 = 'Hello {} your age {} you are from {}'.format(name, age, town)
sentence4 = 'Hello {name} your age {age} you are from {town}'.format(name=name, age=age, town=town)
sentence5 = f'Hello {name} your age {age} you are from {town}'
print(sentence1)
print(sentence2)
print(sentence3)
print(sentence4)
print(sentence5)
# отработал все варианты для себя