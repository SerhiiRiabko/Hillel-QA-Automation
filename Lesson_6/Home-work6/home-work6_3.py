def is_prime(number):
    if number < 2 or number > 1000:
        return False

    for element in range(2, int(number ** 0.5) + 1):
        if number % element == 0:
            return False

    return True
