def cube_sum_of_no(number):
    cube_sum = 0
    for i in range(1, number+1):
        cube_sum += pow(i, 3)

    return cube_sum


#! User input:
n = int(input('Enter the no: '))
result = cube_sum_of_no(n)
print(f'cube sum of {n}th natural no is: {result}')
