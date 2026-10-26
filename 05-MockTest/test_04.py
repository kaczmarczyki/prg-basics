number = int(input("Enter a three-digit number: "))

#calculating the sum of digits
x = number // 10
first_digit = x // 10
second_digit = x % 10
third_digit = number % 10
sum_of_digits = first_digit + second_digit + third_digit

#Reversed number 

print(f'Sum of digits: {sum_of_digits}')
