def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5 + 1)):
        if number % i == 0:
            return False

    return True

#! User inputs:
n = int(input('Enter the no: '))

if is_prime(n):
    print(f'{n} is prime!')
else:
    print(f'{n} is not a prime!')
