###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
volume = 2*(a*b + a*c + b*c)
surface_area= a*b*c
print(f"Cuboid with sides: {a}, {b}, {c}")
print(f"Volume of the cuboid: {volume}")
print(f"Surface Area of the cuboid: {surface_area}")
