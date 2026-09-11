# 1 Email must not be empty
# 2 Email must contain a '.' and '@'
# 3 Email must contain exactly one '@'symbol
# 4 Email must end with ".com",".org", or ".net"
# 5 Email must not be longer than 254 characters
# 6 Email must start and end with a letter or digit

# email = "liptan465@gmail.com"
# is_valid = True
# # 1 Email must not be empty

# email = email.strip()
# if email == "":
#     print("Email cannot be empty.")
#     is_valid = False
# # 2 Email must contain a '.' and '@'

# if not ('.' in email and '@' in email):
#     print("Email must contain . and @")
#     is_valid = False
# # 3 Email must contain exactly one '@'symbol

# if email.count('@') != 1:
#     print("Email must contain exactly 1 '@'")
#     is_valid = False
# # 4 Email must end with ".com",".org", or ".net"

# if not email.endswith((".com", ".org", ".net")):
#     print("Email must end with '.com','.org' and '.net'")
#     is_valid = False
# # 5 Email must not be longer than 245 characters

# if len(email) > 254:
#     print("Email length is grater than 245")
#     is_valid = False
# # 6 Email must start and end with a letter or digit

# if not (email[0].isalnum() and email[-1].isalnum()):
#     print("Email must be start and end with a letter or digit")
#     is_valid = False

# if is_valid:
#     print("Email is valid!")

# --------------Challenge-----------------#
# 1: Must not be empty
# 2: Must be at least 8 characters
# 3: Must include at least 1 uppercase
# 4: Must include at least 1 lowercase
# 5: Must not be same as the Email
# 6: Must not contain any spaces
# 7: Must start and end with a letter or digit

password = "Liptan12345@.com"
is_valid = True

# First clean the password
password = password.strip()

# 1: Must not be empty
if password == "":
    print("Must not be empty")
    is_valid = False

# 2: Must be at least 8 characters
if len(password) < 8:
    print("Must be at lest 8 characters")
    is_valid = False

# 3: Must include at least 1 uppercase
if not(password.count(password.upper()) < 1):
    print("Must include at least 1 uppercase")
    is_valid = False

# 4: Must include at least 1 lowercase
if not(password.count(password.lower()) < 1):
    print("Must include at least 1 1owercase")
    is_valid = False

# 5: Must not be same as the Email

# Email 1 password must not contain a '.' and '@'

if ('.' in password and '@' in password):
    print("password must not contain . and @")
    is_valid = False

# Email 2 password must no end with ".com",".org", or ".net"

if password.endswith((".com", ".org", ".net")):
    print("password must not end with '.com','.org' and '.net'")
    is_valid = False
# Email 3 password must not be longer than 245 characters

if len(password) > 254:
    print("password length is grater than 245")
    is_valid = False

# 6: Must not contain any spaces
if password.count(" "):
    print("Must not contain any spaces")
    is_valid = False

# 7: Must start and end with a letter or digit
if not(password[0].isalnum() and password[-1].isalnum()):
    print("Must start or end with letter or digit")
    is_valid = False


if is_valid:
    print("Password is valid!")

