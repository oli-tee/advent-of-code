import numpy as np
from collections import defaultdict
from typing import Dict

def read_data(file_name: str) -> :
    rows = open(file_name).read().split('\n')
    
    return np.array([[int(digit) for digit in row] for row in rows if row != ''])


def solve(data):
    vert_diff = data[1:, :] - data[:-1, :]
    horz_diff = data[:, 1:] - data[:, :-1]

    vert_diff_1 = np.r_[[-np.ones(vert_diff.shape[1])], vert_diff]
    vert_diff_2 = np.r_[vert_diff, [np.ones(vert_diff.shape[1])]]
    horz_diff_1 = np.c_[-np.ones(horz_diff.shape[0]), horz_diff]
    horz_diff_2 = np.c_[horz_diff, np.ones(horz_diff.shape[0])]

    find_mins = (vert_diff_1 < 0) & (vert_diff_2 > 0) & (horz_diff_1 < 0) & (horz_diff_2 > 0)

    return sum(sum(find_mins * (data + 1)))

def solve2(data):
    basin_dict = calculate_basins(data)
    score = find_score_from_basins_definition(basin_dict)
    return score

def calculate_basins(data):
    basin_dict = defaultdict(list)
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            endpoint = find_endpoint(data, (i, j))
            if endpoint is not None:
                basin_dict[endpoint].append((i, j))
    
    return basin_dict

def find_endpoint(data, start_coord, verbose=False):
    if data[start_coord[0], start_coord[1]] == 9:
        return None
 
    current_coord = start_coord
    previous_coord = start_coord
    
    while current_coord is not None:
        previous_coord = current_coord
        current_coord = find_lowest_neighbour(data, current_coord)
    
    return previous_coord


def find_lowest_neighbour(data, origin_coord):
    x = origin_coord
    
    if data[x[0], x[1]] == 9: 
        return None
    
    min_value = np.Inf
    min_coord = None
    if x[0] > 0 and data[x[0]-1, x[1]] < min(min_value, data[x[0], x[1]]):
        min_coord = (x[0]-1, x[1])
        min_value = data[x[0]-1, x[1]]
    if x[0] < len(data)-1 and data[x[0]+1, x[1]] < min(min_value, data[x[0], x[1]]):
        min_coord = (x[0]+1, x[1])
        min_value = data[x[0]+1, x[1]]
    if x[1] > 0 and data[x[0], x[1]-1] < min(min_value, data[x[0], x[1]]):
        min_coord = (x[0], x[1]-1)
        min_value = data[x[0], x[1]-1]
    if x[1] < data.shape[1]-1 and data[x[0], x[1]+1] < min(min_value, data[x[0], x[1]]):
        min_coord = (x[0], x[1]+1)
        min_value = data[x[0], x[1]+1]
    
    return min_coord
        
def find_score_from_basins_definition(basins: Dict):
    sizes = [len(basin) for basin in basins.values()]
    sizes.sort(reverse=True)
    return sizes[0] * sizes[1] * sizes[2]
             
        
        