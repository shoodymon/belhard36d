# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя
# способами

sentence = input().replace(' ', '-')
print(sentence)

sentence = input()
separator = sentence.split()
new_sentence = '-'.join(separator)
print(new_sentence)