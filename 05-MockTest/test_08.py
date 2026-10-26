###
# Simple calculator
#
number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))
operator = input('Enter operator (+,-,*,/): ')

if number2 == 0 and operator == '/':
    print('Division by zero!!')
elif operator == '+':
    result = number1 + number2
    print(f'{number1} {operator} {number2} = {result}')
elif operator == '-':
    result = number1 - number2
    print(f'{number1} {operator} {number2} = {result}')
elif operator == '*':
    result = number1 * number2
    print(f'{number1} {operator} {number2} = {result}')
elif operator == '/':
    result = number1 / number2
    print(f'{number1} {operator} {number2} = {result}')
else:
    print('Wrong symbol!')

# print(f'{number1} {operator} {number2} = {result}')
