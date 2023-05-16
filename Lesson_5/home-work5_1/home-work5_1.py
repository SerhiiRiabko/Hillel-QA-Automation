import random
# my_list = [(random.randint(1, 100), random.randint(1, 100), random.randint(1, 3)) for _ in range(100)] - see this the
# same action - Is it correct?
my_list = []

for _ in range(100):
    tuple_element = (random.randint(1, 100), random.randint(1, 100), random.randint(1, 3))
    my_list.append(tuple_element)

print(my_list)
