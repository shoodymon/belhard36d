# TODO In this little assignment you are given a string of space separated numbers,
#  and have to return the highest and lowest number.
numbers = "8 3 -5 42 -1 0 0 -9 4 7 4 -4"

def high_and_low(numbers: str) -> str:
    list_of_numbers = numbers.split(' ')
    high_number = list_of_numbers[0]
    low_number = list_of_numbers[0]

    for element in list_of_numbers:
        if int(element) > int(high_number):
            high_number = element
        elif int(element) < int(low_number):
            low_number = element

    high_and_low = str(high_number + ' ' + low_number)

    return high_and_low

print(high_and_low(numbers))