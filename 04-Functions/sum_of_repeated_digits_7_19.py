def f(number):
    total = 0
    str_number = str(number)
    for digit in str_number:
        int_digit = int(digit)
        if str_number.count(digit) > 1:
            total += int_digit
    return total