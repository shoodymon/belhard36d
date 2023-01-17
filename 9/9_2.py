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
class Category(object):

    categories: list[str] = []

    @classmethod
    def add(cls, category: str):
        if category.title() not in cls.categories:
            cls.categories.append(category.title())
            return cls.categories.index(category.title())
        raise ValueError('argument category is not unique')

    @classmethod
    def get(cls, i: int) -> str:
        return cls.categories[i]

    @classmethod
    def delete(cls, i: int) -> None:
        # VAR 1
        if i in range(len(cls.categories)):
            del cls.categories[i]
        # VAR 2
        # try:
        #     del cls.categories[i]
        # except IndexError:
        #     pass

    @classmethod
    def update(cls, i: int, category: str) -> None:
        if i not in range(len(cls.categories)):
            cls.add(category)
        elif category.title() not in cls.categories:
            cls.categories[i] = category.title()
        else:
            raise ValueError('argument category is not unique')

new_list = Category()
new_list.add('first')
new_list.add('second')
new_list.add('third')
new_list.add('forth')
new_list.update(4, 'six')
print(new_list.get(4))