from collections import defaultdict, Counter

def read_data(file_name):
    temp = open(file_name).read().split(',')
    return [int(x) for x in temp]

def transform_1_day(start_state):
    n = len(start_state)
    for i in range(n):
        if start_state[i] == 0:
            start_state[i] = 6
            start_state.append(8)
        else:
            start_state[i] = start_state[i] - 1
            
    return start_state
            
    
def solve_expo(data, ndays, verbose=False):
    state = data[:]
    for i in range(ndays):
        state = transform_1_day(state)
        if verbose:
            print(state)
    if verbose:
        print(state)
    return len(state)

def solve_linear(data, ndays, verbose=False):
    state = dict(Counter(data[:]))
    
    for i in range(ndays):
        state = transform_1_day_dict(state)
        if verbose:
            print(state)
    if verbose:
        print(state)
    return sum(state.values())

   
def transform_1_day_dict(old_index: defaultdict):
    new_index = defaultdict(int)
    for key in old_index:
        if key in [1, 2, 3, 4, 5, 6, 7, 8]:
            new_index[key-1] += old_index[key]
        if key == 0:
            new_index[8] = old_index[key]
            new_index[6] += old_index[key]
    
    return new_index
    