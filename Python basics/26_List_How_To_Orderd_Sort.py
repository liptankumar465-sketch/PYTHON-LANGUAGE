import pattern
#! How TO Orderd / Sort A list?
# ?-------------------------------------------------------
# ! Create a Unsorted List 1D
unsorted_data = [6, 4, 8, 3, 9, 1, 5, 2, 7]
print('1D list')
print(type(unsorted_data))
print(unsorted_data)


# ? sort() -> Sort The Unsorted data in (low -> high)
pattern.line()
print('Use of sort()')
unsorted_data.sort()
print(unsorted_data)


# ? sort(reverse = True) -> Sort The Unsorted Data in (high -> low)
pattern.line()
print('Use of sort(reverse=True)')
unsorted_data.sort(reverse=True)
print(unsorted_data)


# ? sorted(list) -> Returns The Sorted list (low -> high)
pattern.line()
print('Use of sorted()')
sorted_data_accen = sorted(unsorted_data)
print(sorted_data_accen)


# ? Create a string list
pattern.line()
print('String list "python"')
my_list = list('python')
print(my_list)

# ? reverse() -> Reverse The Whole list items
pattern.line()
print('Use of reverse()')
my_list.reverse()
print(my_list)


# ? reversed() -> Returns The Reversed List items
pattern.line()
print('Use of reversed()')
reversed_list = reversed(my_list)
print(my_list)


#! Create A 2D Unsorted List
pattern.line()
print("Matrix List")
matrix = [[3, 5, 1, 6],
          [4, 7, 2, 8]]
print(matrix)

# ? sort() -> Sort The Unsorted data in (low -> high)
pattern.line()
print('Use of sort()')
matrix.sort()
print(matrix)

print('Use of [0].sort()')
matrix[0].sort()
print(matrix)

# ? sort(reverse = True) -> Sort The Unsorted Data in (high -> low)
pattern.line()
print('Use of sort(reverse=True)')
matrix.sort(reverse=True)
print(matrix)

print('Use of [-1].sort(reverse=True)')
matrix[-1].sort(reverse=True)
print(matrix)

# ? sorted(list) -> Returns The Sorted list (low -> high)
pattern.line()
print('Use of sorted()')
sorted_matrix = sorted(matrix)
print(sorted_matrix)

print('Use of [0].sorted()')
sorted_matrix_ft_row = sorted(matrix[0])
print(sorted_matrix_ft_row)

# ? reverse() -> Reverse The Whole list items
pattern.line()
print('Use of reverse()')
matrix.reverse()
print(matrix)

print('Use of [-1].reverse()')
matrix[-1].reverse()
print(matrix)

# ? reversed() -> Returns The Reversed List items
pattern.line()
print('Use of reversed()')
reversed_matrix = reversed(matrix)
print(list(reversed_matrix))

print('Use of [0].reversed()')
reversed_matrix = reversed(matrix[0])
print(list(reversed_matrix))
