def f(sentence):
    space = " "
    text = ""
    for char in sentence:
        if char != space:
            text += char
    return text