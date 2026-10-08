from functools import reduce
import operator

#! Using max():
def max_element(arr):
    res = max(arr)
    print(f'max element: {res}')

#! Using iteration:
def max_item(arr):
    res = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > res:
            res = arr[i]
    print(f'max element: {res}')


#! Using reduce() function:
def max_elements(arr):
    res = reduce(max, arr)
    print(f'max element: {res}')

#! Using sort():
def max_items(arr):
    arr.sort()
    res = arr[-1]
    print(f'max element: {res}')


#! Using operator.gt():
def maximum_item(arr):
    res = 0

    for i in arr:
        if operator.gt(i, res):
            res = i
    print(f'max element: {res}')


#! Take user input:
array = [23, 64, 12, 86, 36, 0, 3, 76, 45, 81, 57]

max_element(array)
max_elements(array)
max_item(array)
max_items(array)
maximum_item(array)
