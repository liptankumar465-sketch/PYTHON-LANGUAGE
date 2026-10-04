
#! ADVANCE CALCULATOR:
# ?-----------------------------------------------------------------------
# todo: Create a Calculator module/function:

def calculator(a: int, b: int, c: str) -> int:
    match c:
        case 'addition':
            result = a+b
        case 'subtraction':
            result = a - b
        case 'multiplication':
            result = a*b
        case 'division':
            try:
                result = a/b
                print('This will be not print!')
            except ZeroDivisionError:
                print('zero not divisivble!')
        case 'floor division':
            result = a//b
        case 'remainder':
            result = a % b
    return result


num1 = int(input('Enter first no: '))
num2 = int(input('Enter second no: '))
operation = input('Entet the operation ').lower().strip()

result = calculator(num1, num2, operation)
print(f'{operation} of {num1} & {num2}: {result}')
