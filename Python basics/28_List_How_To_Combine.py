import pattern
#! How To Combine A List?
# ?------------------------------------------------------------
# ! Create A Two Lists(1D):
list1 = list('liptan')
list2 = list('kumar')
print('list1: ', list1)
print('list2: ', list2)

pattern.line()
# todo: Simplest Way To Combine (+):
print('Use of (+)')
combine_list = list1 + list2
print(f'Combine list: {combine_list}')

pattern.line()
# todo: Nested Lists But Keep Them Seoerated:
print('Nested The Lists')
nested_matrix = [list1, list2]
print(f"Nested List: {nested_matrix}")

pattern.line()
# todo: extend() -> Extend List By Another List Without Creating New one
print('Use Of extend()')
list1.extend(list2)
list1.extend('mahto')
print('list1: ', list1)

pattern.line()
# todo: zip(list1,list2) -> Pair Two Lists in tuple
print('Use Of zip()')
names = ['ram', 'sita', 'karan']
ages = [18, 17, 19]
print('Names: ', names)
print('ages: ', ages)

combine_data = zip(names, ages)
print('Combines Data: ', list(combine_data))

# ! Matric part(2D):
pattern.line()
# todo: Create A Two Lists(2D):
print('Matrix Combination')
matrix1 = [[1, 2],
           [3, 4]]
matrix2 = [[5, 6],
           [7, 8]]
print('Matrix1: ', matrix1)
print('Matrix2: ', matrix2)


pattern.line()
# todo: Simplest Way To Combine (+):
print('Use of (+)')
combine_matrix = matrix1 + matrix2
print(f'Combine Matrix: {combine_matrix}')


pattern.line()
# todo: Nested Lists But Keep Them Seoerated:
print('Nested The Lists')
nested_matrix = [matrix1, matrix2]
print(f"Nested List: {nested_matrix}")


pattern.line()
# todo: extend() -> Extend List By Another List Without Creating New one
print('Use Of extend()')
matrix1.extend(matrix2)
matrix1[0].extend([22])
print(matrix1)


pattern.line()
# todo: zip(list1,list2) -> Pair Two Lists in tuple
print('Use Of zip()')
names = [['ram', 'sita'],
         ['liptan', 'kumar']]
ages = [[14, 15],
        [19, 12]]
print('Names: ', names)
print('ages: ', ages)

combine_data = zip(names, ages)
print('Combines Data: ', list(combine_data))
