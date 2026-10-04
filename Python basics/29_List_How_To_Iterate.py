import pattern
#! How To Iterate A List
# ?------------------------------------------------------------------
#! Iterate in Iterables:
letters = list([1, 2, 3, 4, 5])
print(type(letters))
for letter in letters:
    print(letter)

pattern.line()
values = tuple((12, 54, 32, 45, 64))
print(type(values))
for i in values:
    print(i)

pattern.line()
marks = set({54, 76, 23, 86, 28, 95})
print(type(marks))
for i in marks:
    print(i)

pattern.line()
name_and_age = dict({'ram': 23, 'manoj': 34, 'kumar': 19})
print(type(name_and_age))
for name, age in name_and_age.items():
    print(f'key --> {name}: value --> {age}')


pattern.line()
# ! enumerate(data_structure, start_idx) --> It returns the position(nr + value)
fruits = ['apple', 'coconat', 'banana', 'mango', 'lichi']
index_and_fruit = list(enumerate(fruits))
print('Original fruits: ', fruits)
print('After enumerate: ', index_and_fruit)

print('iterate : index --> value')
for index, value in enumerate(fruits, 1):
    print(f'index: {index} --> fruit: {value}')


pattern.line()
#! map(function, data_struc) --> Also a iterater
map_list = ['a', 'b', 'c']
upper_list = list(map(str.upper, map_list))
print('Original list: ', map_list)
print('After map: ', upper_list)

print('itreate : lower cases:')
for i in map(str.lower, upper_list):
    print(i)


pattern.line()
#! filter(function, data_struc) --> Also a iterater
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, number_list))
print('Original list: ', number_list)
print('After filter: ', even_numbers)

print('iterate : even no:')
for i in filter(lambda x: x % 2 == 0, number_list):
    print(i)


pattern.line()
#! reversed() --> It returns an iterator that filps the data order
original = [1, 2, 3, 4, 5]
reverse = list(reversed(original))
print('Original list: ', original)
print('After reversed: ', reverse)

print('iterate : reversed')
for i in reversed(reverse):
    print(i)


pattern.line()
#! zip(list1 , list2) --> Combines two or more data structures into pair
names = ['ram', 'sita', 'liptan', 'kumar']
ages = [19, 17, 23, 16]
grades = ['B', 'A', 'C', 'A+']

ditails = list(zip(names, ages, grades))
print(f'ditails: {ditails}')

print('iterate : name , age , grade')
for name, age, grade in zip(names, ages, grades):
    print(f'{name} --> {age} --> {grade}')
