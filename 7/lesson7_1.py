# На вход функции поступает простейшая химическая формула, например c2h5oh
# вернуть словарь, где ключами выступают название элементов, а значение:
# количество молекул данного вещества ({"C": 2, "H": 6, "O": 1,})


def elements_count(formula: str) -> dict[str, int]:
    # проверка на последний элемент - является ли он буквой
    formula += '1' if formula[-1].isalpha() else ''
    formula = list(formula)
    i = 0
    while i < len(formula) - 1:
        if formula[i].isalpha() and formula[i+1].isalpha():
            formula.insert(i+1, '1')
            # для меньшего количества итераций
            i += 1
        i += 1
    # formula = list(map(lambda x: int(x) if x.isdigit() else x, formula)) тогда без int в цикле
    data = {}
    for i in range(0, len(formula), 2):
        if formula[i] not in data:
            data[formula[i]] = int(formula[i+1])
        else:
            data[formula[i]] += int(formula[i+1])
    return data

print(elements_count('C2H5OH'))
