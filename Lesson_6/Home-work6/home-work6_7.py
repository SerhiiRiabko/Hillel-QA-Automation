import os
def remove_vowels():
    vowels = "aeiouAEIOU"  # Define a string containing all vowels
    result = ""
    text = input('Add text please')
    if text == '':
        text = input('Insert absolute path to file at PC')

        while not os.path.isfile(text):
            text = input('Invalid file path. Please enter a valid file path: ')
        with open(text, 'r') as file:
            text = file.read()
    for char in text:
        if char not in vowels:
            result += char
    return result
