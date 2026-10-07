def nth_multi_no_fibo(no_of_times, no_of_divible):
    fib = [0, 1]
    count = 0

    while True:
        fib.append(fib[-1] + fib[-2])
        if fib[-1] % no_of_divible == 0:
            count += 1
            if count == no_of_times:
                return fib[-1]


#! Uers inputs:
n = int(input('Enter the no of times: '))
m = int(input('Enter the no of divisble: '))

result = nth_multi_no_fibo(n, m)
print(f'{n}th multiple of a num in fibo: {result}')
