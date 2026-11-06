import range

number = int(input('Enter your number: '))
x_range = int(input("Start of range: "))
y_range = int(input("End of range: "))

check = range.is_in_range(number,x_range,y_range)

print(f'Number {number} in range <{x_range},{y_range}>: {check}')

    