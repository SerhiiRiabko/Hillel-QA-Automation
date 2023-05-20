import os
import re

with open('./../text_files/text.txt') as file:
    text = file.read()
    text_s = text.lower()
    text_without_symb = re.sub(r'\W', '', text_s)
letters_count = {}
for letter in text_without_symb:
    if letter in letters_count:
        letters_count[letter] += 1
    else:
        letters_count[letter] = 1
for letter, count in letters_count.items():
    print(f'{letter} {count}')

