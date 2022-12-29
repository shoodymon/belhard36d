# Реализовать генерацию списка списков рандомных чисел N размера (квадратная матрица)
# N - размер квадратной матрицы

from random import randint

number_n = int(input())
matrix = [[randint(1,100) for j in range(number_n)] for i in range(number_n)]

for i in range(number_n):
    print(matrix[i])
