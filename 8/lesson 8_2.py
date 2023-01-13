# 1. Написать класс Student
# Конструктор класса принимает аргументы: first_name: str, group: int, marks: list[int]
# Написать метод __str__ возвращающая форматированную строку с данными об студенте
# Написать функцию (не метод) student_sort принимающая список студентов: students:
# list[Student] и возвращающая список студентов отсортированный по имени
class Student:

    def __init__(self, first_name: str, group: int, marks: list[int]) -> None:
        self.first_name = first_name
        self.group = group
        self.marks = marks
    # Описали конструктор нашего класса (может не быть, если нет атрибутов класса)

    def __str__(self) -> str:
        return f'Student: {self.first_name=} {self.group=} {self.marks=}'

    # Статик - так как функция нужна только в сортировке 'Student' - аннотация типа класса внутри класса только через ' '
    @staticmethod
    def student_sort(student: list['Student']) -> list['Student']:
        student.sort(key=lambda x: x.first_name)
        return student

# Создание объектов
vasya = Student('vasya', 2, [3, 4, 3, 6])
petya = Student('petya', 4, [7, 6, 8])
masha = Student('masha', 1, [9, 8, 6, 5])
students = [vasya, petya, masha]
students = Student.student_sort(students)
# Итерируемся
for student in students:
    print(student.first_name)
