def f(number1,number2,operator):
    if operator == "+":
        return number1+number2
    elif operator == "-":
        return number1-number2
    elif operator == "%":
        if number2 != 0:
            return number1 % number2
        else:
            return "Second number cant be equal to 0!"
    elif operator == "**":
        return number1 ** number2
    elif operator == "*":
        return number1 * number2
    else:
        return "Wrong operator typed!"
    