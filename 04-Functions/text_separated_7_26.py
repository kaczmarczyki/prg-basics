def f(text):
    text_expanded = ""
    for char in text:
        if text_expanded == "":
            text_expanded += char
        else: 
            text_expanded += "-" + char
    return text_expanded