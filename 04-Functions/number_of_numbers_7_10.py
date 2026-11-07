def f(x,y):
    #range >= x and <= y
# 1. Negative numbers
    sum_of_digits = 0
    for number in range(x,y+1):
        # while number < 0:
        #     if number % 2 == 0:
        #         sum_of_digits += 1
        #     number += 1
        if number < 0 and number % 2 == 0:
            sum_of_digits += 1
        
    return sum_of_digits