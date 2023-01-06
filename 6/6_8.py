# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны

data = {'Belarus': ['Minsk', 'Grodno', 'Brest'],
        'Poland': ['Gdansk', 'Belostok', 'Warsaw'],
        'Ukraine': ['Lviv', 'Kiev', 'Rovno']
        }

city = input('Enter the city: ')

def finding_country(city):
        global data
        for country, cities in data.items():
                if city in cities:
                        return country
        return 'No'

print(finding_country(city))
