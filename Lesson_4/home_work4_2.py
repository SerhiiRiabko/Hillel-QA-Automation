camel_case_names = ["FirstItem", "FriendsList", "MyTuple"]
snake_case_names = []
for name in camel_case_names:
    snake_case_name = name[0].lower()
    for part in range(1, len(name)):
        if name[part].isupper():
            snake_case_name += '_'
        snake_case_name += name[part].lower()
    snake_case_names.append(snake_case_name)
print(snake_case_names)