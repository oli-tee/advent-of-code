from typing import List, Tuple, Dict
import numpy as np


def read_data(file_name):
    rows = open(file_name).read().split('\n')
    #matrix = [[int(x) for x in row.strip()] for row in rows if row != '']
    return convert_to_matrix(rows)

def convert_to_matrix(rows: List[str]):
    matrix = np.array([[int(digit) for digit in row] for row in rows if row != ''])
    return matrix

def find_best_path_from_position_x_v1(matrix, start_pos):# -> Tuple(List[Tuple[int, int]], int):
    "this assumes one can only move to the right or bottom"
    
    this_risk = matrix[start_pos[0], start_pos[1]]
    if start_pos == (matrix.shape[0]-1, matrix.shape[1]-1):
        return ([start_pos], this_risk)
    elif start_pos[0] == matrix.shape[0]-1:
        path, risk = find_best_path_from_position_x_v1(matrix, (start_pos[0], start_pos[1]+1))
        
        return (
            [start_pos] + path,
            risk + this_risk
        )
    elif start_pos[1] == matrix.shape[1]-1:
        path, risk = find_best_path_from_position_x_v1(matrix, (start_pos[0]+1, start_pos[1]))
        
        return (
            [start_pos] + path,
            risk + this_risk
        )
    else:
        path_down, risk_down = find_best_path_from_position_x_v1(matrix, (start_pos[0]+1, start_pos[1]))
        path_right, risk_right = find_best_path_from_position_x_v1(matrix, (start_pos[0], start_pos[1]+1))
        
        if risk_down <= risk_right:
            
            return (
                [start_pos] + path_down,
                risk_down + this_risk
            )
        else:
            return (
                [start_pos] + path_right,
                risk_right + this_risk
            )


def make_risk_matrix(matrix):# -> Tuple(List[Tuple[int, int]], int):
    "this assumes one can only move to the right or bottom"
    
    nrow = matrix.shape[0]
    ncol = matrix.shape[1]
    
    risk_matrix = np.array([[None for r in range(ncol)] for c in range(nrow)])
    padded_risk_matrix = pad_matrix(risk_matrix)

    print(padded_risk_matrix)
    # fill in last col
    for col in range(ncol, 0, -1):
        for row in range(nrow, 0, -1):
            if col == ncol and row == nrow:
                padded_risk_matrix[row, col] = matrix[row-1, col-1]
            else:
                risk_right = padded_risk_matrix[row, col+1]
                risk_down = padded_risk_matrix[row+1, col]
                padded_risk_matrix[row, col] = matrix[row-1, col-1] + min(risk_right, risk_down)
            
        
    
                    
    return unpad_matrix(padded_risk_matrix)
    
def solve1_v1(matrix):
    """
    This algorithm assumes that one can only move right or down, which is probably wrong
    """
    
    optimal_path, total_risk = find_best_path_from_position_x_v1(matrix, [0, 0])
    
    print(optimal_path)
    
    return  total_risk - matrix[0, 0]


def solve1_v2(matrix):
    """
    This algorithm assumes that one can only move right or down, which is probably wrong
    No recursion used
    """
    
    risk_matrix = make_risk_matrix(matrix)
    
    return risk_matrix[1, 1] - 1


def pad_matrix(matrix):
    """
    add a column of 0 on either sides, and a row of 0 on either side of the matrix
    """
    new_matrix = np.c_[np.Inf * np.ones(len(matrix)), matrix, np.Inf * np.ones(len(matrix))]
    new_matrix = np.r_[[np.Inf * np.ones(len(new_matrix[0]))], new_matrix, [np.Inf * np.ones(len(new_matrix[0]))]]
    return new_matrix

def unpad_matrix(padded_matrix):
    """
    remove first and last lines and columns of matrix
    """
    return padded_matrix[1:-1, 1:-1]

def generate_graph_from_matrix(matrix) -> Dict[Tuple, List[Tuple]]:
    nrow = matrix.shape[0]
    ncol = matrix.shape[1]
    
    graph = dict()
    for row in range(nrow):
        for col in range(ncol):
            neighbours = [(row+1, col), (row-1, col), (row, col-1), (row, col+1)]
            valid_neighbours = {
                nb: matrix[nb[0], nb[1]]
                for nb in neighbours
                if nb[0] >= 0 and nb[1] >= 0
                and nb[0] <= nrow - 1 and nb[1] <= ncol - 1 
            }
            
            graph[(row, col)] = valid_neighbours
    
    return graph

def dijkstra(matrix, verbose=False):
    graph = generate_graph_from_matrix(matrix)

    nrow, ncol = matrix.shape
    nodes = [
        (row, col) for row in range(matrix.shape[0]) for col in range(matrix.shape[1])
    ]

    dist = dict()
    prev = dict()

    for node in nodes:
        dist[node] = np.inf
        prev[node] = None

    dist[0, 0] = 0

    u = None

    fuse = 1000000
    counter = 0
    while len(nodes) > 0 and u != (nrow-1, ncol-1) and fuse > 0:
        counter +=1
        fuse -= 1

        min_dist = min([dist[d] for d in nodes])
        u = [d for d in nodes if dist[d] == min_dist][0]
        
        nodes.remove(u)
        
        if verbose:
            if counter % 100 == 0:
                print(f"{counter}: {u}. left: {len(nodes)}")

        neighbours = {k:v for k,v in graph[u].items() if k in nodes}

        for v in neighbours:
            alt = dist[u] + neighbours[v]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    print((len(nodes) > 0 , u != (nrow, ncol) , fuse > 0))
    return dist[nrow-1, ncol-1]


def dijkstra_light(matrix, verbose=False):
    graph = generate_graph_from_matrix(matrix)

    nrow, ncol = matrix.shape
    nodes = [
        (row, col) for row in range(matrix.shape[0]) for col in range(matrix.shape[1])
    ]

    dist = dict()
    prev = dict()

    dist[0, 0] = 0

    u = None

    fuse = 1000000
    counter = 0
    while len(nodes) > 0 and u != (nrow-1, ncol-1) and fuse > 0:
        counter +=1
        fuse -= 1
        
        dist_inter_nodes = set(nodes).intersection(set(dist.keys()))
        min_dist = min([dist[d] for d in dist_inter_nodes])
        u = [d for d in dist_inter_nodes if dist[d] == min_dist][0]
        
        nodes.remove(u)
        
        if verbose:
            if counter % 100 == 0:
                print(f"{counter}: {u}. left: {len(nodes)}")

        neighbours = {k:v for k,v in graph[u].items() if k in nodes}

        for v in neighbours:
            alt = dist[u] + neighbours[v]
            if v not in dist or alt < dist[v]:
                dist[v] = alt
    print((len(nodes) > 0 , u != (nrow, ncol) , fuse > 0))
    return dist[nrow-1, ncol-1]


def replicate_data(data):
    full_data = data
    mutating_data = data
    for i in range(4):
        mutating_data = increase(mutating_data)
        full_data = np.c_[full_data, mutating_data]

    mutating_data = full_data
    for i in range(4):
        mutating_data = increase(mutating_data)
        full_data = np.r_[full_data, mutating_data]
    return full_data

def solve2_brute(matrix):
    full_matrix_row1 =  replicate(matrix)
    
    dijkstra(full_matrix_row1, True)
    
def increase(x):
    return ( x % 9 ) + 1