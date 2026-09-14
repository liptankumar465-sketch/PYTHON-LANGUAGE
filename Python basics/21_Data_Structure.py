
#!----------------Data Structure------------------#
# ? Is a way of organizing and storing data so it can
# ? be used efficiently.
# todo: 1 -> list[] --> (Common)
# todo: 2 -> tuple() --> (No changes!)
# todo: 3 -> set{} --> (unique!)
# todo: 4 -> dict{} --> (key : value)


#! List properties:
# ? Ordered collection of items.
# ? Changeble.
# ? Allows duplicates.

#todo: HOW TO CREATE A LIST.
# ? Creates list manually:
empty = []
print(empty)
print(type(empty))

letters = ['a', 'b', 'c']
print(letters)
print(type(letters))

numbers = [1, 2, 3]
print(numbers)
print(type(numbers))

mixed = [1, 'a', True, None]
print(mixed)
print(type(mixed))

# ? Create lists by list():
# todo: list(value) converts an iterable (sequence)
# todo: into a list.

empty = list()
print(empty)

letters = list('Python')
print(letters)

numbers = list(range(1, 6))
print(numbers)

# ? Create a 2-D list:
matrix = [[1, 2, 3],
          [4, 5, 6]]
print(matrix)

mixed_matrix = [['a', 'b', 'c'],
                [1, 2, 3]]
print(mixed_matrix)
