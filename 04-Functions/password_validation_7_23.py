from count_letters_7_4 import count

def f(password):
    password_length = len(password)

    if password_length < 6:
            return False
    
    for letter in password:
        total = count(letter,password)
        if total > 1:
            return False
    
    return True

    