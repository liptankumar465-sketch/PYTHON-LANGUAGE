# Types:
# type(), str()

name = "liptan"
print(type(name))  # str

age = 18
print(type(age))  # int

age = str(age)
print(type(age))  # str

# Math:

# use of len()

password = "123a"
print(len(password))

if len(password) < 8:
    print("your password is too sort")
else:
    print("your password is correct")

# use of count()

text = """
python is easy to learn.
python is powerful.
Many people love python.
"""
print(text.count("python"), "times")

# Transformations:

# use of replace()

phone = "175-1234-56"
print(phone.replace('-', '/'))

price = "$1243.24"
print(price.replace('$', "").replace('.', ""))
# -------------challenge---------------#
phone = "+49 (176) 123-4567"
print(phone.replace('+', "").replace('-', "").replace(' ',
      "").replace('(', "").replace(')', ""))

# use of 'str' + 'str'

first_name = "liptan"
last_name = "kumar"
full_name = first_name + "-" + last_name
print(full_name)

folder = "c/Users/liptan/"
file = "string.py"
file_path = folder + file
print(file_path)

# use of f{}

name = "Sam"
age = 19
is_student = False

# printing without f{}
print("My name is "+name+", i am " + str(age) +
      " years old, and student status is "+str(is_student) + ".")

# printing with f{}
print(
    f"My name is {name}, i am {age} years old, and student status is {is_student}.")

print(f"2 + 3 = {2+3}")

# use of split()

stamp = "2007-12-07"
print(stamp.split('-'))

adders = "India,Jharkhand,Ramgarh,Teliyatu"
print(adders.split(','))

# use of 'str' * number

print("lalala")
print('la' * 3)

# <Extraction>
# use of str[index]

# Indexes & slicing
text = "Python"

# Extract the first character
print(text[0])
print(text[-6])

# Extract the last character
print(text[5])
print(text[-1])

data = "2026-08-09"
print(data)
# Extract the year
print(data[0:4])
print(data[:4])

# Extract the month
print(data[5:7])

# Extract the data
print(data[-2:])

# Cleaning:

# cleaning whitespaces using
# lstrip(), rstrip(), strip()

text = " Engineering"
print(text.lstrip())

text = "Engineering "
print(text.rstrip())

text = " Engineering ".strip()
print(text)

text = "####ABC#####".strip('#')
print(text)

# find whitespacse in text
text = " Engineering "
print(len(text))
print(len(text.strip()))

nr_of_spaces = len(text) - len(text.strip())
is_clean = len(text) == len(text.strip())

if is_clean:
    print("Is data clean?", is_clean)
else:
    print("nr of spaces: ", nr_of_spaces)

# use of upper(), lower()

text = "python LANGUAGE"
print(text.upper())
print(text.lower())

# case conversions
search = " Email "
true_data = " email"
print(search == true_data)  # false

search = " Email ".lower().strip()
true_data = " email".lower().strip()
print(search == true_data)  # true

# Search:
pone = "+49-176-12345"

# use of startswith()
print(phone.startswith("+49")) # true

# use of endswith()
email = "liptankumar@gmail.com"
print(pone.endswith(".com")) # true

# 'sub' in 'str'
print("@" in email) # true

# use of find()
phone1 = "+43-176-12435"
phone2 = "48-543-23445"
phone3 = "0047-434-23557"
print(phone1[phone1.find('-')+1:]) # 176-12435
print(phone2[phone2.find('-')+1:]) # 543-23445
print(phone3[phone3.find('-')+1:]) # 434-23557

country = "INDIA"
print(country.isalnum())  # true

phone = "543412144333"
print(phone.isnumeric()) # true

phone = " @214345433233"
print(phone.isnumeric()) # false