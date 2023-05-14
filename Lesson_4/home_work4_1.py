s = "name=Amanda=sssss&age=32&&salary=1500&currency=euro"
pairs = s.split("&")
new_str = " ".join(pairs)
pairs2 = new_str.split("=" and "=sssss")
new_str2 = " ".join(pairs2)
key_value_pairs = new_str2.split()
my_dict = {}
for pair in key_value_pairs:
    key, value = pair.split("=")
    my_dict[key] = value
print(my_dict)
