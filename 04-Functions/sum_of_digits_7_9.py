def f(number,even):
    str_number = str(number)
    digits_sum = 0
    # for digit in str_number:
    #     test = int(digit)
    #     digits_sum += test

    for digit in str_number:
        int_digit = int(digit)
        if even:
            if int_digit % 2 == 0:
                digits_sum += int_digit
            else:
                digits_sum = digits_sum
        elif not even:
            if int_digit % 2 != 0:
                digits_sum += int_digit 
    return digits_sum