import count_letters_7_4 as count_letters

text = 'You never get a second chance to make a first impression'
letter = str(input('What letter the number have to count?: '))

total = count_letters.count(letter, text)

print(f"The number of letter '{letter}': {total} ")