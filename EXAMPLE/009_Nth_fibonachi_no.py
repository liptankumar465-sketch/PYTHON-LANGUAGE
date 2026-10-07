def fibonachi(number):
    if number <= 1:
        return number

    return fibonachi(number - 1) + fibonachi(number - 2)


#! User inputs:
n = int(input('Enter the no: '))
fibo = fibonachi(n)
print(f'{n}th fibonachi no is: {fibo}')
