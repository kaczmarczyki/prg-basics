def f(palindrome):
    # text_backwards = ""
    text_backwards = palindrome[::-1]

    if palindrome == text_backwards:
        return True
    else:
        return False