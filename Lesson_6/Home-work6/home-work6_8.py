def display_box(width: int, height: int, character="*"):
    if width < 2 or height < 2:
        print("Width and height must be at least 2.")
        return

    print(character * width)

    for _ in range(height - 2):
        middle_line = character + " " * (width - 2) + character
        print(middle_line)

    print(character * width)
