# Код Морзе для представления цифр и букв использует тире и точки. Напишите
# функцию для кодирования текстового сообщения в соответствии с кодом Морзе.
# (словари в помощь)

morse = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
        }

# ШИФРОВАНИЕ
# мы извлекаем каждый символ (если не пробел) из слова по одному и сопоставляем его с соответствующим кодом Морзе
def encode_to_morse(message):
    result = ''
    for letter in message:
        if letter != ' ':
            result += morse[letter] + ' '
        else:
            result += ' '
    return result

print(encode_to_morse(message='HELLO PYTHON'))

# ДЕШИФРОВАНИЕ
def decode_from_morse(message):
    # Пробел - проверка на извлечение символов и начало их декодирования
    # Последний пробел в конце строки поможет нам идентифицировать последнюю последовательность символов
    message += ' '
    text = ''
    decipher = ''
    # Продолжаем извлекать символы из строки, пока у нас не останется свободного места.
    for letter in message:
        # Проверяет наличие свободного места
        if letter != ' ':
            # Cчетчик для отслеживания пространства
            count_of_spaces = 0
            # Cохранение азбуки Морзе из одного символа
            text += letter
        # В случае нехватки места
        else:
            # Новый символ
            count_of_spaces +=1

            # Новое слово
            if count_of_spaces == 2:
                # Добавление пробела к отдельным словам
                decipher += ' '
            else:
                # Доступ к ключам с использованием их значений
                decipher += list(morse.keys())[list(morse.values()).index(text)]
                text = ''
    return decipher

print(decode_from_morse(message='.... . .-.. .-.. ---'))
