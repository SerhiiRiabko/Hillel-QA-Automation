import re
'''
my_str = "python"  # or ''
# python is present as tuple ('p','y'....)
print(my_str[0:4])
# last element
print(my_str[-1])
# every 2d element from the end  [from: to: step]
print(my_str[::2])

# reverse string
print(my_str[::-1])

# string methods functs
name = '     Griffin   '
float_n = '34,09'
int_n = '6'
binary = '00101'
bool_str = 'False'

print(name.find('G'))
print(binary.isdigit()) # true
print(int_n.isdigit()) # true
print(float_n.isdigit()) # false

print(name.rfind("t")) # find index

print(name.count("f")) # count element and how much they
'''
'''
name = 'Griffin Trues'
name2 = 'for'
print(name.lower())
print(name.upper())
print(name.encode('UTF16'))
print(name.encode('UTF16').decode('UTF16'))
# to see file is method push ctrl and click on name

print(name.isnumeric()) # is it digit
print(name2.isidentifier()) # reserve word
print(name.isalpha()) # without spases
print('name Serhii the best'.center(40, '$'))

coockie = 'name-Splinter-Cell-Rat'
print(coockie.split('-'))

coockie = 'name-Splinter-Cell-Rat'
print(coockie.split('-', maxsplit=2))

drinks = ['jin', 'vodka', 'pepsi']

default = '    Gea  Tea   '
print(default.strip()) # lstrip and l.strip spaces removed

new_str = '## Rest ### Api'
print(new_str.replace('#', '$'))

for drink in drinks:
    print(drink.rjust(10,'$'))
'''
# name = 'Lisa'
# surname = 'Simpson'
#
# print(f'name: {name}, surname: {surname}')
# print('name: {0}, surname: {1}'.format(name, surname))
# print('name: %s, surname: %s' % (name, surname))

# Regular expressions

# regex101.com
numbers_phone = '08005556644, 08006667788, 765675675'
pattern = re.compile(r'\d-?\d{3}-?\d{3}-?\d{2}-?\d{2}')
print(pattern.findall(numbers_phone))
