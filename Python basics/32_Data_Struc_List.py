import pattern
#! DATA STRUCTURE LIST:
# todo: List is a mutable ordered calection of items.

my_list = ['ram', 'sita', 'lakshman', 'hira']

pattern.line()
print('1. List is Ordered:')
print(my_list)
print('my_list[0] = ', my_list[0])
print('my_list[2] = ', my_list[2])
print('my_list[-1] = ', my_list[-1])

pattern.line()
print('2. List is Mutable:')
upper_list = [name.upper() for name in my_list]
print(upper_list)
# my_list[0] = 'RAM'
# my_list[1] = 'SITA'
# my_list[2] = 'LAKSHMAN'
# my_list[3] = 'HIRA'


pattern.line()
print('3. List Adding Operations:')
print('Before: ', my_list)
my_list.append('LIPTAN')
my_list.insert(3, 'KUMAR')
my_list.extend(['GOTAM', 'SUMIT'])
print('After: ', my_list)

pattern.line()
print('4. List Removing Operations:')
print('Before: ', my_list)
my_list.remove('ram')
my_list.pop(3)
del my_list[1]
# ? Also use clear() --> list all items are cleaned
my_list.clear()
print('After: ', my_list)
