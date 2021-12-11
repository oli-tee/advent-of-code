import numpy as np

def read_data(file_name):
    return open(file_name).read().split('\n')[:-1]

def parse_row(row:str):
    "'9,4 -> 3,4'"
    temp = row.replace(' ', '').split('->')
    temp = [x.split(',') for x in temp]
    return ((int(temp[0][0]), int(temp[0][1])), (int(temp[1][0]), int(temp[1][1])))

def generate_list_of_int(start, end):
    if end >= start:
        return list(range(start, end+1))
    else:
        return list(range(start, end-1, -1))
    
def generate_list_of_coords(start_coord, end_coord, include_diag=False):
    if start_coord[0] == end_coord[0]:
        common_x = start_coord[0]
        return [(common_x, i) for i in generate_list_of_int(start_coord[1], end_coord[1])]
    elif start_coord[1] == end_coord[1]:
        common_y = start_coord[1]
        return [(i, common_y) for i in generate_list_of_int(start_coord[0], end_coord[0])]
    else:
        if include_diag:
            
            return list(
                zip(generate_list_of_int(start_coord[0], end_coord[0]), generate_list_of_int(start_coord[1], end_coord[1]))
            )
        else:
            return []
    

def get_board_dimension(parsed_rows):
    max_x = np.max([np.max([pr[0][0], pr[1][0]]) for pr in parsed_rows])
    max_y = np.max([np.max([pr[0][1], pr[1][1]]) for pr in parsed_rows])
    return (max_x, max_y)
    
def get_score(matrix):
    temp = [np.sum(np.array(row) > 1) for row in matrix]
    return np.sum(temp)


def solve(data, include_diag=False):
    
    parsed_rows = [parse_row(row) for row in data]
    
    dims = get_board_dimension(parsed_rows)
    matrix = [[0 for i in range(dims[1]+1)] for j in range(dims[0]+1)]

    for line in parsed_rows:
        coords = generate_list_of_coords(line[0], line[1], include_diag)
        # print(coords)
        for coord in coords:
            matrix[coord[0]][coord[1]] = matrix[coord[0]][coord[1]] + 1
    
    # display(matrix)
    return get_score(matrix)


def solve2(data):
    return solve(data, include_diag=True)

def display(matrix):
    for row in matrix:
        print(row)