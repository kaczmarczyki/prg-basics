def f(product_code):
    first_digit = int(product_code[0])
    second_digit = int(product_code[1])
    third_digit = int(product_code[2])
    total = first_digit + second_digit + third_digit
    reminder = total % 7

    if reminder == int(product_code[3]):
        return True
    return False
