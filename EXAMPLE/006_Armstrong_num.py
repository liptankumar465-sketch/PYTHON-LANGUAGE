
#! Using Math:
def is_armstrong_no(number):
    lenght = len(str(number))
    temp = number
    sum_of_digits = 0

    while temp != 0:
        digit = temp % 10
        sum_of_digits += pow(digit, lenght)
        temp //= 10

    if sum_of_digits == number:
        print(f'{number} is Armstorng!')
    else:
        print(f'{number} is not Armstrong!')

#! Using string:
def is_armstrong(num):
    l = len(str(num))
    s = sum(int(d) ** l for d in str(num))

    if s == num:
        print(f'{num} is Armstorng!')
    else:
        print(f'{num} is not Armstrong!')

#! Using map():
def armstromg(n):
    l = len(str(n))
    s = sum(map(lambda d: int(d) ** l, str(n)))

    if s == n:
        print(f'{n} is Armstorng!')
    else:
        print(f'{n} is not Armstrong!')


n = int(input('Enter the no: '))
is_armstrong_no(n)
is_armstrong(n)
armstromg(n)
