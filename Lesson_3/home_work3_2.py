import operator

value_num = 2
value_num_res1 = value_num / 2
value_num_res2 = operator.truediv(value_num, 2)
value_num /= 2

value_num_1 = 2
value_num_1_res1 = value_num_1 * 2
value_num_1_res2 = operator.mul(value_num_1, 2)
value_num_1 *= 2

print(value_num_res2)
print(value_num_res1)
print(value_num)

print(value_num_1_res2)
print(value_num_1_res1)
print(value_num_1)
# I had troubles with bin values
# bin_value = bin(2)
# number_2 = bin(2)
# result_bin1 = operator.truediv(bin_value, number_2)
# result_bin2 = operator.mul(bin_value, number_2)
# print(bin(result_bin1))
# print(bin(result_bin2)
