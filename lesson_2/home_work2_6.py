group_of_people = ["John", "Rebecca", "Alessandro", "Melena", "John"]
uniq_names = []
for names in group_of_people:
    if names not in uniq_names:
       uniq_names.append(names)
print(uniq_names)
