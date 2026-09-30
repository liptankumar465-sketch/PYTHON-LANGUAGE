
#! Authentication System
# ?-----------------------------------------------
# ? Simple Authenticatiion System Those Check
# ? User naem And password

# ? User name and password
user_name = 'liptan'
user_password = '775411'

name = input('Enter your name: ')

if name.strip().lower() == user_name:
    pasword = input('Enter your password: ')
    if pasword.strip() == user_password:
        print('User Authentication Completed!')
    else:
        print('Worng password entered!')
else:
    print('Worng name entered!')
