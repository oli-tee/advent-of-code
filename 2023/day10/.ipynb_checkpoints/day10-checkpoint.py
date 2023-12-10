import re
from collections import defaultdict

def read_data(file_name):
    rows = open(file_name, 'r').read().split('\n')
    rows = [row.strip() for row in rows if row.strip() != '']
    return rows


def connect_up(row, col, data, graph):
    if row > 0 and data[row-1][col] in ['F', '7', '|', 'S']:
        graph[(row, col)].append((row-1, col))
    # return graph

def connect_left(row, col, data, graph):
    if col > 0 and data[row][col-1] in ['F', 'L', '-', 'S']:
        graph[(row, col)].append((row, col-1))
    # return graph

def connect_down(row, col, data, graph):
    if row < len(data)-1 and data[row+1][col] in ['L', 'J', '|', 'S']:
        graph[(row, col)].append((row+1, col))
    # return graph


def connect_right(row, col, data, graph):
    if col < len(data[row])-1 and data[row][col+1] in ['J', '7', '-', 'S']:
        graph[(row, col)].append((row, col+1))
    # return graph

def parse_graph(data):
    graph = defaultdict(list)
    for row in range(len(data)):
        for col in range(len(data[row])):
            char = data[row][col]
            #print(char)
            if char == 'L':
                connect_up(row, col, data, graph)
                connect_right(row, col, data, graph)
            elif char == 'J':
                connect_left(row, col, data, graph)
                connect_up(row, col, data, graph)
            elif char == '7':
                connect_left(row, col, data, graph)
                connect_down(row, col, data, graph)
            elif char == 'F':
                connect_right(row, col, data, graph)
                connect_down(row, col, data, graph)
            elif char == '-':
                connect_left(row, col, data, graph)
                connect_right(row, col, data, graph)
            elif char == '|':
                connect_up(row, col, data, graph)
                connect_down(row, col, data, graph)
            elif char == 'S':
                connect_up(row, col, data, graph)
                connect_down(row, col, data, graph)
                connect_right(row, col, data, graph)
                connect_left(row, col, data, graph)
                
    return graph


def find_s(data):
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == 'S':
                return (row, col)
            
def explore_graph(graph, start_pos):   
    distances = dict()

    queue = [(start_pos, 0)]

    while len(queue) > 0:
        node_tuple = queue[0]
        node = node_tuple[0]
        distance = node_tuple[1]
        next_nodes = graph[node]
        for a_node in next_nodes:
            if a_node not in distances:
                queue.append((a_node, distance + 1))

        distances[node] = distance
        queue = queue[1:]
        
    return distances


def solve_p1(file_name, verbose=False):
    data = read_data(file_name)
    
    graph = parse_graph(data)
    start_pos = find_s(data)
    distances = explore_graph(graph, start_pos)
    
    if verbose:
        show_path(data, distances, False)
    
    max_distance = max([distances[k] for k in distances])
    return max_distance


def show_path(data, distances,show_numbers=True):
    matrix = ""
    n_rows = len(data)
    n_cols = len(data[0])
    for row in range(n_rows):
        # line = ""
        for col in range(n_cols):
            if (row, col) in distances:
                if show_numbers:
                    matrix += str(distances[(row, col)])
                else:
                    #matrix += 'o'
                    matrix += data[row][col]
            else:
                matrix += ('.')
        matrix += ('\n')
    print(matrix)