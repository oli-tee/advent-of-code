import re

def read_data(file_name):
    rows = open(file_name, 'r').read().split('\n')
    rows = [row.strip() for row in rows if row.strip() != '']
    return rows

def parse_data(rows):
    turns = rows[0]
    graph = {}
    for row in rows[1:]:
        
        strings = re.match(r"(...) = \((...), (...)\)", row).groups()
        graph[strings[0]] = {'L': strings[1], 'R': strings[2]}
        
    return {'turns': turns, 'graph': graph}


def solve_p1(file_name, verbose=False):
    data = parse_data(read_data(file_name))
    turns = data['turns']
    graph = data['graph']
    
    counter = 0
    fuse = 1e9
    current_node = 'AAA'
    while current_node != 'ZZZ' and counter < fuse:
        if verbose:
            print(current_node)
        turn = turns[counter % len(turns)]
        current_node = graph[current_node][turn]
        counter += 1
    
    return counter


def is_finished(nodes):
    return min([k[2]=='Z' for k in nodes])

def solve_p2_brute_force(file_name, verbose=False):
    data = parse_data(read_data(file_name))
    turns = data['turns']
    graph = data['graph']
    
    counter = 0
    fuse = 1e9
    current_nodes = [k for k in graph if k[2] == 'A']
    
    while not is_finished(current_nodes) and counter < fuse:
        if verbose or counter < 10:
            print(current_nodes)
        turn = turns[counter % len(turns)]

        current_nodes = [graph[current_node][turn] for current_node in current_nodes]
        counter += 1
    
    
    return counter


def find_next_zs(node, graph, turns, n):
    current_node = node
    list_z = []
    for i in range(n):
        current_node = graph[current_node][turns[i % len(turns)]]
        if current_node[2] == 'Z':
            list_z.append((i+1, current_node))
            
    
    return list_z

def find_next_z(node, data):
    current_node = node
    i = 0
    while current_node[2] != 'Z':
        current_node = data['graph'][current_node][data['turns'][i % len(data['turns'])]]
        i += 1
            
    
    return i

def solve_p2_smart(file_name, verbose=False):
    data = parse_data(read_data(file_name))
    
    list_a = [k for k in data['graph'] if k[2]=='A']
    
    cycle_sizes = [find_next_z(a, data) for a in list_a]
    score = find_common_multiple_iter(cycle_sizes)
    
    return score


def find_common_multiple_2numbers(n1, n2):
    i = 1
    while (n1 * i) % n2 != 0:
        i += 1 
    return n1 * i

def find_common_multiple_iter(numbers):
    cm_so_far = find_common_multiple_2numbers(numbers[0], numbers[1])
    for i in range(2,len(numbers)):
        cm_so_far = find_common_multiple_2numbers(cm_so_far, numbers[i])
        
    return cm_so_far