def read_input(file_name):
    data = open(file_name, 'r').read().split('\n')
    return [int(x) for x in data if x != '']


def solve(numbers, window_size):
    import numpy as np
    numbers_array = np.array(numbers)
    diffs = numbers_array[window_size:] - numbers_array[:-window_size]
    return sum(diffs > 0)

assert solve([1, 2, 3], 1) == 2
assert solve([4, 3, 2], 1) == 0
assert solve([1, 3, 4, 2, 1], 2) == 1

print('all tests passed')

    