digit_list = [1, 2, 3, 4, 5, 6, 7, 8]
odd_tuples = []
even_tuples = []

for numer, value in enumerate(digit_list):
    if numer % 2 == 0:
        odd_tuples.append((numer, value))
    else:
        even_tuples.append((numer, value))

print("Odd Tuples:", odd_tuples)
print("Even Tuples:", even_tuples)
