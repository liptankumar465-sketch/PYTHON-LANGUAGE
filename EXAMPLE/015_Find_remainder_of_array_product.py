
#! Using navie multiplication:
def arr_product_remainder(remainder, array):
    product = 1
    for i in array:
        product *= i
    res = product % remainder
    print(f'arr{array} product remainder: {res}')

#todo: Take user inputs:
arr = [100, 10, 5, 25, 35, 14]
remainder_no = 11
arr_product_remainder(11,arr)