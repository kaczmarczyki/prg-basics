def f(expression):
    result = int(expression[0])

    for i in range(1,len(expression),2):
        sign = expression[i]
        digit = int(expression[i+1])

        if sign == "+":
            result += digit
        else: 
            result -= digit

    return result
        