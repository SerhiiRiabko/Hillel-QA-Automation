def square_of_even_numbers():
    return (x ** 2 for x in range(1000000001) if x % 2 == 0)


squares = square_of_even_numbers()
print(next(squares))
print(next(squares))
