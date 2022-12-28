# вывести первые n чисел кратные  m  и больше k

number_n = int(input('n = '))
number_m = int(input('m = '))
number_k = int(input('k = '))

# само число K должно делиться на M c остатком 0

while number_n > 0:
    if number_k % number_m == 0:
        print(number_k)
        number_k += number_m
        number_n -= 1
    else:
        number_k += 1