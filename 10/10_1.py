# TODO Написать класс KeyboardButton, на вход конструктора постапают аргументыЖ
#  text: str, request_contact: bool, request_location: bool
#  Перед определением атрибутов объекта на основании аргументов, произвести валидацию
#  значение аргументов по типу данных
#  Написать метод объекта dict, возвращающий словарь с атрибутами объекта и их значениями
#  Написать класс KeyboardMarkup, конструктор класса принимает аргументы:
#  keyboard: list[list[KeyboardButton]], resize_keyboard: bool, one_time_keyboard: bool
#  Перед определением атрибутов объекта на основании аргументов, произвести валидацию
#  значение аргументов по типу данных
#  Написать магический serialize, возвращающий представление объекта в виде словаря
#  с атрибутами и их значениями, пример:
#  {'resize_keyboard': True, 'one_time_keyboard': False, 'keyboard': [[{'text': 'Button1',
#  'request_contact': False, 'request_location': False}]]


class KeyboardButton:

    def __init__(self, text: str,  request_contact: bool = False, request_location: bool = False) -> None:
        if not isinstance(text, str):
            raise TypeError('argument `text` must be string')
        if not isinstance(request_contact, bool):
            raise TypeError('argument `request_contact` must be boolean')
        if not isinstance(request_location, bool):
            raise TypeError('argument `request_location` must be boolean')
        if request_contact and request_location:
            raise ValueError

        self.text = text
        self.request_contact = request_contact
        self.request_location = request_location

    def dict(self) -> dict:
        return {
            'text': self.text,
            'request_contact': self.request_contact,
            'request_location': self.request_location
        }


class KeyboardMarkup:

    def __init__(
            self,
            keyboard: list[list[KeyboardButton]],
            resize_keyboard: bool = True,
            one_time_keyboard: bool = False
    ) -> None:
        if not isinstance(resize_keyboard, bool):
            raise TypeError('argument `resize_keyboard` must be boolean')
        if not isinstance(one_time_keyboard, bool):
            raise TypeError('argument `one_time_keyboard` must be boolean')
        if not isinstance(keyboard, list):
            raise TypeError('argument `keyboard` must be list')
        for line in keyboard:
            if not isinstance(line, list):
                raise TypeError
            for button in line:
                if not isinstance(button, KeyboardButton):
                    raise TypeError

        self.keyboard = keyboard
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard

    def serialize(self) -> dict:
        return {
            'resize_keyboard': self.resize_keyboard,
            'one_time_keyboard': self.one_time_keyboard,
            'keyboard': [
                [
                    button.dict()
                    for button in line
                ]
                for line in self.keyboard
            ]
        }


markup = KeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='button1'),
            KeyboardButton(text='button2'),
        ],
        [
            KeyboardButton(text='button3'),
            KeyboardButton(text='button4'),
        ]
    ]
)
print(markup.serialize())