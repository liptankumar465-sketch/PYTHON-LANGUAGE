letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
rotate = letter[2:] + letter[:2]
print(rotate)
#! Using slicing:


def rotation(d, arr):
    arr[:] = arr[d:] + arr[:d]
    print(arr)

#! Using reverse() method:


def rotation_func(d, arr):
    n = len(arr)
    arr.reverse()

    arr[:n] = arr[:n][::-1]
    arr[n:] = arr[n:][::-1]

    print(arr)

arr = [1, 2, 3, 4, 5, 6, 7]
d = 2

#! Using reversed():
# Reverse first d elements
arr[:d] = reversed(arr[:d])

# Reverse remaining elements
arr[d:] = reversed(arr[d:])

# Reverse entire array
arr.reverse()
print(arr)


#! Take user input:
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rotation(3, array)
rotation_func(3, array)

