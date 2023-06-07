import re
import os
import shutil

file_address = input('Insert absolute path to file at PC')


def remove_numbers_from_file(file_address):
    with open(file_address, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        modified_line = re.sub(r'\d+', '', line)
        modified_lines.append(modified_line)

    with open('./output/output.txt', 'w') as file:
        file.writelines(modified_lines)
