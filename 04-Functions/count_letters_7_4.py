def count(letter,text):
    total = 0
    for i in text:
        if letter == i:
            total += 1
    return total