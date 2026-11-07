import range_7_5

number = int(input('Enter your number: '))
x_range = int(input("Start of range: "))
y_range = int(input("End of range: "))

check = range_7_5.is_in_range(number,x_range,y_range)

print(f'Number {number} in range <{x_range},{y_range}>: {check}')

    