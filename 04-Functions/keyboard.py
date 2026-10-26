def input_string(message):
    string = input(message)
    return str(string)

def input_integer(message):
    integer = input(message)
    return int(integer)

def input_real(message):
    real = input(message)
    return float(real)

def input_boolean(message):
    boolean = input(message)
    if boolean == 'y' or boolean == 'Y':
        boolean = True
    elif boolean == 'n' or boolean == 'N':
        boolean = False
    return boolean
