###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# Pobranie Wartości od uzytkownika
# Przekonwertowanie na kelvin i fahrenheity
# Przekazanie uzytkownikowi obliczonej temperatury

celsius_degrees = float(input("Enter temperature in degrees Celsius: "))

kelvins = celsius_degrees + 273.15
farenheits = (celsius_degrees * (9/5)) + 32

print(f"Temperature in Celsius: {celsius_degrees} C")
print(f"Temperature in kelvins: {kelvins} K")
print(f"Temperature in farenheits: {farenheits} F")