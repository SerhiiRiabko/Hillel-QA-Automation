import random
import os
import pickle

# my_list = [(random.randint(1, 100), random.randint(1, 100), random.randint(1, 3)) for _ in range(100)] - see this the
# same action - Is it correct?
my_list = []

for _ in range(100):
    tuple_element = (random.randint(1, 100), random.randint(1, 100), random.randint(1, 3))
    my_list.append(tuple_element)

print(my_list)
os.chdir('./..')
os.makedirs('./test/data directory tree')
with open('./test/data directory tree/array_of_tuples.txt', 'w+b') as file:
    data_of_file = pickle.dumps(my_list)
    file.write(data_of_file)
