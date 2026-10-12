import math
price = float(input("Enter price: "))
discount = int(input("Enter discount (%): "))/100
discounted_price = price * (1.0-discount)
discounted_price = round(discounted_price,2)
reduction = price - discounted_price
reduction = round(reduction,2)
print(f"Price with discount: {discounted_price}")
print(f"Reduction: {reduction}")