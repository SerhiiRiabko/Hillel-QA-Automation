import math


def calculate_sum_arg(*args):
    total_sum_arg = sum(args)
    return total_sum_arg


def calculate_sum(*numbers):
    total_sum = 0
    for num in numbers:
        total_sum += num
    return total_sum
