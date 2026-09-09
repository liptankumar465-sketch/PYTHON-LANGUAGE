# Membership (in) operator:
# Checks if a value inside another value
# like a string, list, tuple, or other sequences

print("o" in "python") # true
print("o" not in "python") # false

print(3 in [1,2,3,4,5]) # true
print(3 not in [1,2,4,5]) # true

# Security check: ensure the domain is not banned
domain = "gmail.com"
banned_domains = ["spam.com", "fake.org","bot.net"]
print(domain not in banned_domains) # true

domain = "spam.com"
print(domain not in banned_domains) # false

# Identity (is) operator:
# Checks if two variables refer to the same object in memory
# This operator access variable addresses

x = [1,2,3]
y = [1,2,3]
print(x == y) # true
print(x is y) # false

x = 10
y = 10
print(x == y) # true
print(x is y) # true

x = 50
y = x
print(x == y) # true
print(x is y) # true

# Make sure the email exists, and it's not empty.
# first way
email = "barran@.com"
print(email != "" and email != None) # true

email = ""
print(not email == "" and not email == None) # false

# sceond way
email = None
print(email != "" and email is not None) # false


