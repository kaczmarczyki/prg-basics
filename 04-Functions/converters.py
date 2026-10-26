def m_to_cm(n):
    result = n*100
    return round(result,2)

def cm_to_m(n):
    result = n/100
    return round(result,2)

def cm_to_inch(n):
    result = n*2.54
    return round(result,2)

def ft_to_cm(n):
    result = n * 30.48
    return round(result,2)

def inch_to_cm(n):
    result = n / 2.54
    return round(result,2)

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'532cm = {cm_to_inch(532)}inch')
    print(f'6ft = {ft_to_cm(6)}cm')
    print(f'27in = {inch_to_cm(27)}cm')

