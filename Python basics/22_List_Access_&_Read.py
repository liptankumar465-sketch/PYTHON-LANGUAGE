
#!----------------List---------------------#
# todo: How to Access & Read in list.

lis = ['a', 'b', 'c', 'd', 'e']
print(lis)

# ? Access by index:
print('Print idx first ch: ', lis[0])
print('Print idx last ch: ', lis[-1])
print('Print idx last sec ch: ', lis[-2])
print('Print idx 2 ch: ', lis[2])

matrix = [
    #!Col  0,  1,   2
    ['a', 'b', 'c'],  # ! Row 0
    ['d', 'e', 'f'],  # ! Row 1
    ['g', 'h', 'i']]  # ! Row 2

print('All elements: ', matrix)
print('Print first Row: ', matrix[0])
print('Print first Row first ele: ', matrix[0][0])
print('Print mid Row: ', matrix[1])
print('Print mid Row mid ele: ', matrix[1][1])
print('Print last Row: ', matrix[-1])
print('Print  last Row last ele: ', matrix[-1][-1])


# todo: Slicing a list:
letters = list('Python')

print('slicing first to last: ', letters[:])
print('slicing first to sec last: ', letters[:-1])  # ! starting 0 is defualt.
print('slicing sec to last: ', letters[1:])  # ! last index is defualt.

matrix = [
    #!Col  0,  1,   2
    ['a', 'b', 'c'],  # ! Row 0
    ['d', 'e', 'f'],  # ! Row 1
    ['g', 'h', 'i']]  # ! Row 2

print('slicing first to last Row: ', matrix[:])
print('slicing fist Row: ', matrix[:1])  # ! ya only 0
print('slicing mid Row: ', matrix[1:2])  # ! ya only 1
print('slicing last Row: ', matrix[2:])  # ! ya only 2
print('slicing last Row firt to las ele: ', matrix[2][:2])
print('slicing first Row sec to las ele: ', matrix[0][1:])
print('slicing mid Row mid ele: ',matrix[1][1:2])