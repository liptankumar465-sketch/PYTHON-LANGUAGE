# input() function take inputs from use
# In python by deflut input takes string values

# take surname from the user
name = "liptan"
print("print user full name!")
sur_name = input("Enter your surname:")
print(name, sur_name)
print('-' * 30)

# take two values from the user and add
x = input("Enter first val:")
y = input("Enter secon val:")
print("sum of x and y:", x + y)
print("worng! becouse the defult type of input vari is string")
print('-' * 30)

x = int(input("Enter first val:"))
y = int(input("Enter secon val:"))
print("sum of x and y:", x + y)
print("This is right!")
print('-' * 30)

name = input("Enter your name:")
country = input("Enter your contry:")

print("details!")
print(name, "comes form", country)
