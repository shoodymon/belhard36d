# TODO 3. Реализовать класс Category
#  Создать атрибут класса categories
#  3.1 Написать метод класса add принимающий на вход название категории, если такой
#  категории в атрибуте класса categories нет, добавить данную категорию в список и вернуть
#  индекс вхождения новой категории в списке. Если такая категория уже есть, вызвать
#  исключение ValueError
#  3.2 Написать метод класса get принимающий индекс и возвращающий категорию из списка
#  категорий на этом индексе, если нет элемента на таком индексе, вызвать исключение
#  IndexError
#  3.3 Написать метод класса delete принимающий индекс категории в списке категорий и
#  удаляющий элемент из списка категорий на этом индексе, если нет элемента на таком
#  индексе, ничего не делать, метод ничего возвращать не должен
#  3.4 Написать метод класса update принимающий индекс категорий и новое название
#  категории, если нет элемента на таком индексе, то новая категория должна добавляться с
#  учетом того, что имена категорий уникальны, если новое имя категории нарушает
#  уникальность в списке категорий, вызвать исключение ValueError

# TODO 4. Изменить класс выше, список категорий должен содержать не просто имена категорий, а
#  словари с данными о каждой категории (name: str, is_published: bool), а так же изменить
#  методы add, get, delete, update для работы с списком словарей
#  4.1 Добавить метод make_published принимающий индекс категории и меняющий значение
#  ключа is_published на True, если такого индекса нет, вызвать исключение IndexError
#  4.2 Добавить метод make_unpublished принимающий индекс категории и меняющий
#  значение ключа is_published на False, если такого индекса нет, вызвать исключение
#  IndexError

class Category(object):

    categories: list[dict] = []

    @classmethod
    def add(cls, category_name: str, is_published: bool) -> int:
        category_name = category_name.title()
        category = tuple(filter(lambda x: x['name'] == category_name, cls.categories))
        if category:
            raise ValueError('category is not unique')
        cls.categories.append(
            {
                'name': category_name,
                'is_published': is_published
            }
        )
        return len(cls.categories) - 1

    @classmethod
    def get(cls, index: int) -> dict:
        try:
            return cls.categories[index]
        except IndexError as e:
            raise ValueError(e)

    @classmethod
    def delete(cls, index: int) -> None:
        if index in range(len(cls.categories)):
            del cls.categories[index]

    @classmethod
    def update(cls, index: int, new_category_name: str) -> None:
        new_category_name = new_category_name.title()
        category = tuple(filter(lambda x: x['name'] == new_category_name, cls.categories))
        if category:
            raise ValueError('category is not unique')
        try:
            cls.categories[index]['name'] = new_category_name
        except IndexError:
            cls.add(category_name=new_category_name, is_published=False)

    @classmethod
    def make_published(cls, index: int) -> None:
        try:
            cls.categories[index]['is_published'] = True
        except IndexError as e:
            raise ValueError(e)

    @classmethod
    def make_unpublished(cls, index: int) -> None:
        try:
            cls.categories[index]['is_published'] = False
        except IndexError as e:
            raise ValueError(e)

print(Category.add('Food', True))
print(Category.add('Drink', True))
print(Category.add('food', False))
