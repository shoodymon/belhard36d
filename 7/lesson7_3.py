# На вход функции поступает N целое положительное число
# вернуть N первых простых чисел больших 0, в виде кортежа

def get_prime_numbers(n: int) -> tuple[int]:
    prime_numbers = []
    number = 2
    while len(prime_numbers) < n:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                break
        else:
            prime_numbers.append(number)
        number += 1
    return tuple(prime_numbers)

print(get_prime_numbers(20))

