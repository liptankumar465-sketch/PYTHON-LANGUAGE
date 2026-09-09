# Types:

print(True)
print(False)
print(type(True))
print(type(False))

# bool()
# True conditions
print(bool(50))
print(bool("hi"))
print(bool(" "))

# False conditions
print(bool())
print(bool(0))
print(bool(""))
print(bool(None))

# any:

email = ""
phone = "0235-123456"
username = ""
# Allows registration
# if any one is filled

print(any([email, phone, username])) # true

email = ""
phone = ""
username = ""
# Allows registration
# if any one is filled

print(any([email, phone, username])) # false

# Functions and Methods whose return True/False
print(isinstance(123,int)) # True
print(isinstance(123,str)) # False
print(isinstance(True,str)) # False
