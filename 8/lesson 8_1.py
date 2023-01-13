class Person:

    # Атрибут чертежа, а не объекта
    city = 'Minsk'
    all = []

    # 1 - Создание объекта
    def __new__(cls, *args, **kwargs):
        return cls()

    def __str__(self):
        return f'User: name={self.name} email={self.email}'

    def __len__(self):
        return len(self.name)

    def __getitem__(self, item):
        return self.__getattribute__('name')

    def __gt__(self, other):
        if isinstance(other, Person):
            return self.age > other.age
        elif isinstance(other, (int, float)):
            return self.age > other
        else:
            raise TypeError

    def __add__(self, other):
        if isinstance(other, Person):
            return self.age + other.age
        elif isinstance(other, int):
            return self.age + other
        else:
            raise TypeError

    def __radd__(self, other):
        return self.__add__(other)

    def __iter__(self):
        return self

# for val in vasya.name:
#   print(val)

    def __next__(self):
        try:
            self.__getattribute__('_key')
        except:
            self.__setattr__('_key', ['name', 'email', 'age'])

        if self._key:
            key = self._key[0]
            del self.key[0]
            return self.__getattribute__(key)
        else:
            del self._key
            raise StopIteration

#   for val in vasya:
#       print(val)

    # 2 - Конструктор
    def __init__(self, name, email):
        self.email = email
        self.name = name.title()
    #   self.city = 'Minsk'
        self.all.append(self)
        self.info()
        self.change_city()

    def info(self):
        return f'{self.email=} {self.name=} {self.city=}'

    @classmethod
    def change_city(cls, new_city):
        cls.city = new_city.title()
        # cls - указатель на наш класс

    @classmethod
    def all_info(cls):
        for user in cls.all:
            print(user.name)

vasya = Person(name='vasya', email='vasya@info.com')
petya = Person(name='petya', email='petya@info.com')
Person.change_city('SPB')
print(vasya.info())
print(petya.info())
# Значение атрибута только для Вася
# vasya.age = 34

# Дополнение, теперь атрибут класса и атрибут объекта
# vasya.city = 'SPB'

# Обращение к классу, чтобы изменить значение атрибута класса
# Person.city = 'SPB'




