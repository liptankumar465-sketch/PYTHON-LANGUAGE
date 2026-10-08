
#! Using single pass:
def is_monotonic(array):
    n = len(array)
    incr = any(array[i] <= array[i+1] for i in range(n-1))
    decr = any(array[i] >= array[i+1] for i in range(n-1))

    if incr or decr:
        print(f'{array} --> is monotonic')
    else:
        print(f'{array} --> is not monotonic')

#! Using sorted() method:


def is_monotoinc_arr(array):
    incr = sorted(array) == array
    decr = sorted(array, reverse=True) == array

    if incr or decr:
        print(f'{array} --> is monotonic')
    else:
        print(f'{array} --> is not monotonic')


# todo: Take user inputs:
arr = [6, 5, 4, 4]
is_monotonic(arr)
is_monotoinc_arr(arr)
