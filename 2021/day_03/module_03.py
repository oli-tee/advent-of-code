def read_data(file_name):
    data = open(file_name, 'r').read().split('\n')[:-1]
    return data 

def get_most_common_bits(data):
    import numpy as np
    n = len(data[0])
    result = ''
    for i in range(n):
        inputs = [int(x[i]) for x in data]
        if np.mean(inputs) > 0.5:
            result += '1'
        else:
            result += '0'
    return result
    
def get_least_common_bits(data):
    mcb = get_most_common_bits(data)
    
    return ''.join([str(1-int(x)) for x in mcb])


def get_epsilon(data):
    return int(get_most_common_bits(data), 2)
    
def get_gamma(data):
    return int(get_least_common_bits(data), 2)

def solve(data):
    n = len(data[0])
    epsilon = get_epsilon(data)
    return epsilon * (2**n - 1- epsilon)



def get_oxygen(data):
    import numpy as np
    i = 0
    valid_inputs = data

    counter = 0

    while (len(valid_inputs) > 1) & (i <= len(data[0]) - 1):
        counter += 1
        print(valid_inputs)
        values_at_i = [int(x[i]) for x in valid_inputs]
        if np.mean(values_at_i) >= 0.5:
            to_keep = '1'
        else:
            to_keep = '0'
        
        valid_inputs = [x for x in valid_inputs if x[i] == to_keep]
        i += 1
        
    if len(valid_inputs) == 1:

        return int(valid_inputs[0], 2)
    
    else:
        print(valid_inputs)
        raise ValueError


def get_co2(data):
    import numpy as np
    i = 0
    valid_inputs = data

    counter = 0

    while (len(valid_inputs) > 1) & (i <= len(data[0]) - 1):
        counter += 1
        print(valid_inputs)
        values_at_i = [int(x[i]) for x in valid_inputs]
        if np.mean(values_at_i) >= 0.5:
            to_keep = '0'
        else:
            to_keep = '1'
        
        valid_inputs = [x for x in valid_inputs if x[i] == to_keep]
        i += 1
        
    if len(valid_inputs) == 1:

        return int(valid_inputs[0], 2)
    
    else:
        print(valid_inputs)
        raise ValueError


def solve2(data):
    
    return get_oxygen(data) * get_co2(data)
    
def run_tests():
    assert get_most_common_bits(['1011', '1000', '0100']) == '1000'
    
    assert get_least_common_bits(['1011', '1000', '0100']) == '0111'
    print('all tests passed')

    assert get_epsilon(['1011', '1000', '0100']) == 8
    assert get_gamma(['1011', '1000', '0100']) == 7
    result = solve(['1011', '1000', '0100'])
    print(result)
    assert result == 56
run_tests()