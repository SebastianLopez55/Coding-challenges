"""
Function to generate a random number of length intLength
"""

import time as t


def random_num(int_length):
    curr_time = int(t.time_ns())
    curr_time = curr_time // 1000
    selected_ints = 10 ** int_length
    return curr_time % selected_ints


length = 5
print(random_num(length), '\n')

# Convert array of element to a single int
array = [1, 2, 3, 4, 5]
# Convert each array element to string type
map_result = map(str, array)
# Join each element to a single string
single_integer = int(''.join(map_result))
print(single_integer)
