def area(a, h):
    triangle_area = 0.5 * a * h
    return triangle_area

a = int(input("Enter a: "))
h = int(input("Enter h: "))

area_value = area(a,h)
print(f'Area of triangle with base = {a} and height = {h} is: {int(area_value)}')