import math
import random
# Types:

x = 24
y = 3.14
z = 4 + 7j

print(type(x))
print(type(y))
print(type(z))

# x in string -> int()
x = "24"
x = int(x)
print(type(x))  # int

# y in string -> float()
y = "3.14"
y = float(y)
print(type(y))  # float

# z in real or imaginary -> complex(real,imagin)
r = 4
i = 9
c = complex(r, i)
print(c)
print(type(c))

# Math:

print(5 + 6)
print(5 - 2)
print(2 * 6)
print(9 / 3)
print(9 // 3)
print(7 % 2)
print(2 ** 3)

# Rounding Numbers:

# use of ads()
#   positive -> positive
#   neagtive -> positive

print("distanc: ", 2 - 8)
print("distanc: ", abs(2 - 8))

# use of round()

val = 35.934325
print(val)
print(round(val))  # clogest integer
print(round(val, 3))

# use of floor() -> import math firs

print(math.floor(val))  # lower deci

# use of ceil() -> higer deci

print(math.ceil(val))

# use of trunc() -> remove deci

print(math.trunc(val))
print(int(val))

# Adv Math:

no = 4
print(math.sqrt(no))
print(math.sin(45))
print(math.cos(45))
print(math.log(10))

# Random: -> import random first

print(random.random())  # give random valuse
print(random.randint(1, 6))  # give 1 to 6 random values

# Validation:

# use of is_integer()
val = 7.0
print(val.is_integer())  # true

val = 7.3
print(val.is_integer())  # false

# use of isinstance(val,data_type)
val = 6.2

print(isinstance(val, int))
print(isinstance(val, float))
print(isinstance(val, str))
print(isinstance(val, bool))

# ---------------challenge-----------------#

value = random.randint(1, 100)
if value % 2 == 0:
    print(f"{value} is prime!")
else:
    print(f"{value} is not a prime!")
