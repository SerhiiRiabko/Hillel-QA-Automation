# mutable
# List
my_list = [1, 2, 3, 4]
# next variant
my_list2 = list([1, 2, 3, 4])

# Set
my_set = {1, 2, 3, 4, 4, 5}  # second 4 will not be shown in print

# dictionary
my_dict = {'key1': '5', 6: 7, 'name': 'Serhii'}

# Immutable
my_integer = 5
my_float = 5, 5
my_bool = False
my_tuple = (1, 2, 3, 4)

print(id(my_integer))

my_text = """Big text with space
Paragraph"""  # use 3 """For text with paragraphs """
print(my_text)

cats_name = ['Tyr', 'Filimosha', 'Guru']

print(len(cats_name))
print(cats_name[1])

for index in range(len(cats_name)):
    print(index)
    print(cats_name[index])
    print("Finish iteration")

for cat_name in cats_name:  # For each cycle
    print(cat_name)

count = 0
while True:
    print(cats_name[count])
    count = count + 1

    if count == 2:
        break

person = ('Serhii', 35)
name, age = person  # the same  name = person[0]

persons = {"test": "4", 'name':"Seraphic", "numbers": "7"}
