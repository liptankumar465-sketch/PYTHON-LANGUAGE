
#!------------------Unpacking-------------------#
# ? Unpacking list 1st way:

person = ['Sita', 24, 'Data Enginerr', 'India']
name = person[0]
age = person[1]
role = person[2]
country = person[3]

print('name: ', name)
print('age: ', age)
print('role: ', role)
print('country: ', country)

# ? Unpacking list 2nd way:
person = ['Ram', 25, 'AI ML Enginerr', 'India']
name, age, role, country = person
#! Order of values are same.

print('name: ', name)
print('age: ', age)
print('role: ', role)
print('country: ', country)

# ? Unpacking list only first ele:
person = ['Ram', 25, 'AI ML Enginerr', 'India']
name, *details = person

print(name)
print(details)

# ? Unpacking list only last ele:
person = ['Ram', 25, 'AI ML Enginerr', 'India']
*details, country = person

print(details)
print(country)

# ? Unpacking list only first and last eles:
person = ['Ram', 25, 'AI ML Enginerr', 'India']
name, *details, country = person

print(name)
print(details)
print(country)

# ? Unpacking list in numbers:
numbers = [1, 2, 3]
first, sec, third = numbers

print(first)
print(sec)
print(third)

# ? Unpacking list only mid eles:
person = ['Ram', 25, 'AI ML Enginerr', 'India']
_, age, role, _, = person
#! (_) Underscore use for ignore.(Not store in memory)
print(age)
print(role)
print(_)

# ? Unpacking list only first and last eles:
# ? And ignore the else.
person = ['Ram', 25, 'AI ML Enginerr', 'India']
name, *_, country = person

print(name)
print(country)
print(*_)