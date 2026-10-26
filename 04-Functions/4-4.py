# Calculates the sum of the digits in a number
def sum_digits(number):

    number = abs(number)

    string_number = str(number)

    running_total = 0

    for digit in string_number:
        running_total += int(digit)
            
    return running_total

input_number = int(input("Enter your number: "))
sum_value = sum_digits(input_number)

print(f"For number {input_number}, sum of its digits is equal to: {sum_value}")