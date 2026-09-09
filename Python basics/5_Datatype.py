""" Data types in python """
"""
    -> In python basically 3 types of data
    1-> No value
        -> none

    2-> Single value/primitive types
        -> int, float, bool, str

    3-> Multi valus/data structrue/collections/container
        -> list, set, tuple, dict
"""
"""
    Key points:
        / python automatically detect data type
        / Dynamic: data types can change any
          time.
"""

a = 5  # int
b = 3.14  # float
c = 'Hi python'  # str
c2 = "Hi python"  # str
c3 = "12345"  # str
d = True  # bool
d2 = False  # bool
i = None  # none
e = [1, 2, 3, 4, 5]  # list
f = {1, 2, 3, 4, 5}  # set
g = (1, 2, 3, 4, 5)  # tuple
h = {'a': 1, 'b': 2, 'c': 3}  # dict


text = "good"
number = 50
# type() -> works for both
print(type(text))
print(type(number))

# len() -> only works for string
print(len(text))
# print(len(number)) -> this error passed

# bit_length() -> only works for integer or float
# print(text.bit_length()) -> this is error pass
print(number.bit_length())

# -------------challenge-----------------#
age = 18
hight = 5.4
name = "liptan"
is_student = True
job = None

print(age)
print(type(age))
print(len(str(age)))
print(hight)
print(type(hight))
print(len(str(hight)))
print(name)
print(type(name))
print(len(name))
print(is_student)
print(type(is_student))
print(len(str(is_student)))
print(job)
print(type(job))
print(len(str(job)))
