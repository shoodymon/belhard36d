# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)

users = {
    'id: 12312254253': {
        'Name': 'Petya', 'Surname': 'Vasilyev', 'Tel.': '750-26-26', 'Email': 'petvas78@gmail.com'
    },
    'id: 32849823948': {
        'Name': 'Maksim', 'Surname': 'Aliev', 'Tel.': '128-65-75', 'Email': 'alievm39@gmail.com'
    },
    'id: 84576894986': {
        'Name': 'Alik', 'Surname': 'Kireev', 'Tel.': '457-85-96', 'Email': 'kireev9797@gmail.com'
    },
    'id: 65748395894': {
        'Name': 'Artur', 'Surname': 'Bogomoltsev', 'Tel.': '421-65-74',
    },
    'id: 54898058348': {
        'Name': 'Alex', 'Surname': 'Miller', 'Tel.': '468-85-52', 'Email': ''
    }
}

def find_user():
    for user in users.values():
        if not user.get('Email'):
            print(user.get('Name'))

find_user()
