
#! Basic Calculator
# ?----------------------------------------------------------
# ? Create a Basic Calculation Functions
def add(num1, num2):
    return sum(num1, num2)


def sub(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def divi(num1, num2):
    return num1 / num2


def rema(num1, num2):
    return num1 % num2


def pattern():
    print('--------------------------------------------')


while (True):
    pattern()

    # ? Take Inputs Form The Users
    number1 = int(input('Enter First no: '))
    number2 = int(input('Enter second no: '))

    # ? Operations to do
    pattern()
    print('What Operation to do!')
    print('1) Press For Addition')
    print('2) Press For Subtraction')
    print('3) Press For Multiplication')
    print('4) Press For Division')
    print('5) Press For Remainder')

    choice = input('Choose the any one: ')

    # ? proccessing the choice
    pattern()

    match choice:
        case '1':
            print('Addition is: ', add(number1, number2))
        case '2':
            print('Subtraction is: ', sub(number1, number2))
        case '3':
            print('Multiplication is: ', mult(number1, number2))
        case '4':
            print('Division is: ', divi(number1, number2))
        case '5':
            print('Remainder is: ', rema(number1, number2))
        case _:
            print('Worng No Pressed!')

    # ? Diside want more operations or not!
    pattern()
    print('More Operations Type "Yes"')
    print('NO More Operations Type "No"')

    action = input('Type: ')

    if action.strip().lower() == 'yes':
        continue
    elif action.strip().lower() == 'no':
        break
    else:
        print('Please type "yes or no" only!')
