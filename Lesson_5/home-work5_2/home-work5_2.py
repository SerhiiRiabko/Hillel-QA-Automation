import os
import pickle

with open('./../text_files/array_of_tuples.txt', 'r+b') as file:
    text_byte = file.read()

result_text = pickle.loads(text_byte)
print(result_text)
answers = []
for elements in result_text:
    number_1 = elements[0]
    number_2 = elements[1]
    math_func = elements[2]
    if math_func == 1:
        answer = number_1 + number_2
        symbol_el = '+'
    elif math_func == 2:
        answer = number_1 - number_2
        symbol_el = '-'
    elif math_func == 3:
        answer = number_1 * number_2
        symbol_el = '*'
    else:
        answer = None
        symbol_el = None
    answers.append(f'{number_1} {symbol_el} {number_2} = {answer}')
print(answers)
