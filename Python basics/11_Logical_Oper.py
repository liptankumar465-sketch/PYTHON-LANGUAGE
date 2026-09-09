"""
    Logical Operators
    (and | or)
    Used to combine multiple boolean expressions
"""
# AND:
# Both conditions will be True => True
# If one conditions will be False => False

print(3 > 1 and 5 < 7)
print(3 > 1 and 5 < 3)

# OR:
# Both conditions will be True => True
# Both conditions will be False => False
# If one conditions will be True => True

print(5 > 2 or 5 < 6)
print(5 < 2 or 5 < 6)
print(5 < 2 or 5 > 6)

# Checks if the system is under pressure
cpu_usage = 95
memory_usage = 60
print(cpu_usage > 90 or memory_usage > 90)

cpu_usage = 55
memory_usage = 70
print(cpu_usage > 90 or memory_usage > 90)

# Check user credentials before login
email = True
password = False
print(email and password)

email = True
password = True
print(email and password)

# NOT:
# True change into False
# False change into True

print(not True)
print(not False)
print(not not True)
print(not not False)


print(3 > 2)
print(not 3 > 2)

print(3 > 7)
print(not 3 > 7)

# In python by defualt and presition is greater
# than or
print(5 == 5 or 8 > 5 and 6 < 4)

# Change presition
print(5 == 5 or (8 > 5 and 6 < 4))

# Change presition
print((5 == 5 or 8 > 5) and 6 < 4)

# Allow access only if the user is logged in
# or they are a guest
# but they must not be banned

is_logged_in = True
is_guest = False
is_banned = True

print(is_logged_in or (is_guest and not is_banned))

is_logged_in = True
is_guest = False
is_banned = True

print((is_logged_in or is_guest) and not is_banned)

# -------------challenges---------------#

""" Check if a users name is not empty and the age
is greater than or equal to 18 """

name = ""
age = 18
print(name and age >= 18)  # false

name = "liptan"
age = 18
print(name and age >= 18)  # true

""" Check if the password is at least 8
characters long and dose not contain spaces """

password = "12345678"
print(len(password) >= 8 and not " " in password)  # true

password = " 12345678"
print(len(password) >= 8 and not " " in password)  # false

password = "12345"
print(len(password) >= 8 and not " " in password)  # false

""" Check if a users email is not empty,
contains '@', and ends with '.com' """

email = "liptankumar@.com"
print(not email == "" and ('@' in email and email.endswith(".com")))  # true

email = "liptankumar.com"
print(not email == "" and ('@' in email and email.endswith(".com")))  # false

email = "liptankumar@.text"
print(not email == "" and ('@' in email and email.endswith(".com")))  # false

""" Check if a username is a string, is not None,
and is longer than 5 characters """

name = "liptan"
print(len(name) > 5 and not name == '') # true

name = "lipta"
print(len(name) > 5 and not name == '') # false

name = ""
print(len(name) > 5 and not name == '') # false

