###
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
#
# Bank Code (4 characters)
#Country Code (2 characters)
#Location Code (2 characters)
#Branch Code (3 characters - optional)
swift = input('Please Enter your SWIFT: ')
print(f'Bank Code: {swift[0:4]}')
print(f'Country Code: {swift[4:6]}')
print(f'Location Code: {swift[6:8]}')
print(f'Branch Code: {swift[8:]}')