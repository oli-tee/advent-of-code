from collections import defaultdict
import numpy as np
import re

def read_data(file_name):
    rows = open(file_name, 'r').read().split('\n')
    return [row.strip() for row in rows if row.strip() != '']

def robust_add(array, r, c):
    if r >= 0 and r < len(array) and c >= 0 and c < len(array[0]):
        array[r][c] = 1
    return array


def get_counters(data):
    n_rows = len(data)
    n_cols = len(data[0])
    counters = np.array([np.zeros(n_cols) for i in range(n_rows)])

    for r in range(n_rows):
        for c in range(n_cols):
            #print(f"{r}, {c}")
            if not re.match(r'[\d\.]', data[r][c]):
                counters = robust_add(counters, r-1, c-1)
                counters = robust_add(counters, r-1, c)
                counters = robust_add(counters, r-1, c+1)
                counters = robust_add(counters, r, c+1)
                counters = robust_add(counters, r+1, c+1)
                counters = robust_add(counters, r+1, c)
                counters = robust_add(counters, r+1, c-1)
                counters = robust_add(counters, r, c-1)
    return counters

def validate_part(row, start, end, counters):
    is_valid_part =  max([counters[row][j] for j in range(start, end)])
    return is_valid_part > 0

def solve_p1(data):
    counters = get_counters(data)
    score = 0

    for row in range(len(data)):
        string = data[row]
        pattern = '(\d*)'
        number_positions = [(m.start(0), m.end(0), m.group(0)) for m in re.finditer(pattern, string) if m.end() > m.start()]
    

        for match in number_positions:
            is_valid_part =  validate_part(row, int(match[0]), int(match[1]), counters)
            if is_valid_part:
                score += int(match[2])
    return score

        
def safe_check_star(pos, data):
    i_row = pos[0]
    i_col = pos[1]
    if i_row >= 0 and i_row < len(data) and i_col >= 0 and i_col < len(data[i_row]):
        if data[i_row][i_col] == '*':
            return True
    
    return False
    
def get_gear_index(data):
    gear_index = defaultdict(list)

    for i_row in range(len(data)):
        row = data[i_row]
        pattern = '(\d*)'
        numbers = [{'start': m.start(0), 'end': m.end(0), 'number': int(m.group(0))} for m in re.finditer(pattern, row) if m.end() > m.start()]

        for number in numbers:
            start = number['start']
            end = number['end']
            number_value = number['number']
 
            adjacent_positions = (  
                [(i_row, start-1), (i_row, end)] +
                [(i_row-1, ii) for ii in range(start-1, end+1)] +  
                [(i_row+1, ii) for ii in range(start-1, end+1)] 
            )

            for pos in adjacent_positions:
                is_star = safe_check_star(pos, data)
                if is_star:
                    gear_index[pos].append(number_value)
    return gear_index
    
def solve_p2(data):
    
    gear_index = get_gear_index(data)

    score = 0
    for key in gear_index:
        if len(gear_index[key]) == 2:
            score += gear_index[key][0] * gear_index[key][1]

    return score