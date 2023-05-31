def even_squares(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            yield num ** 2


# For example
start_num = 0
end_num = 1000000000

squares = even_squares(start_num, end_num)

for square in squares:
    print(square)
