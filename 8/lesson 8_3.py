# 3. Написать класс Numbers
# Конструктор класса принимает список чисел numbers: list[int]
# Написать метод average — возвращающий среднее арифметическое между всеми числами
# Написать метод max_count — возвращающий число из списка, которое чаще встречается,
# если таких чисел несколько, вывести среднее арифметическое среди таких чисел

class Numbers:
    def __init__(self, numbers: list[int]) -> None:
        self.numbers = numbers

    def average(self, numbers) -> float:
        """ Нахождение среднего арифметического списка чисел

        :param numbers: список чисел
        :return: среднее арифметическое чисел
        """
        return sum(self.numbers) / len(self.numbers)

    def max_count(self) -> int | float:
        from collections import Counter
        numbers_counter = Counter(self.numbers)
        max_count_number = numbers_counter.most_common(n=1)[0][1] # n - количество встреч
        numbers = []
        for key, val in numbers_counter.items():
            if val == max_count_number:
                numbers.append(key)
        return sum(numbers) / len(numbers)

numbers = [1, 3, 5, 5, 23, 2, 45, 2, 5, 2, 4, 12, 34]
numbers = Numbers(numbers)
print(numbers.max_count())
