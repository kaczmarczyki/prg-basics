###
# A program that calculates the length of the diagonal
# of a rectangle with sides a and b.
#
import math
a = 5
b = int(input("Put a number for second side: "))
diagonal = math.sqrt(a**2+b**2)
print(f"The rectangle with sides a ({a}) and b ({b}) has a diagonal of: {diagonal}")
