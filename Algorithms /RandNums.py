"""
Function to generate a random number of length intLength
"""

import time


def random_num(int_length):
    # Get the current time in milliseconds
    current_time_ms = int(time.time() * 1000)
    # Set the seed by extracting the last `length` digits from the current time
    seed = current_time_ms % (10 ** int_length)
    # Generate a random number within the specified range
    min_value = 10 ** (int_length - 1)
    max_value = (10 ** int_length) - 1
    random_number = (current_time_ms * seed) % (max_value - min_value + 1) + min_value
    return random_number


def int_list_to_num(array):
    # Convert each array element to string type
    map_result = map(str, array)
    # Join each element to a single string
    single_integer = int(''.join(map_result))
    print(single_integer)
    return single_integer


# Rand number function call
length = 4
print(random_num(length), '\n')

# List to num call
array0 = [1, 2, 3, 4, 5]
int_list_to_num(array0)


array1 = [0, 4, 3, 4, 5]
int_list_to_num(array1)
