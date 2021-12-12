from collections import defaultdict, Counter
from typing import List, Dict

def read_data(file_name):
    rows = open(file_name, 'r').read().split('\n')
    return [row.strip() for row in rows if row.strip() != '']

def parse_input(rows: List[str]) -> Dict[str, str]:
    result = defaultdict(list)
    for row in rows:
        start = row.split('-')[0]
        end = row.split('-')[1]
        result[start].append(end)
        result[end].append(start)
    
    return result

def solve1(data):
    edges_dict = parse_input(data)
    paths = recursive_traverser(edges_dict, ['start'])
    return len(paths)

def recursive_traverser(edges_dict: Dict[str, List[str]], path_so_far: List[str]) -> List[List[str]]:
    if path_so_far[-1] == 'end':
        possible_paths = [path_so_far]
    else:
        possible_paths = []
        neighbours = edges_dict[path_so_far[-1]]
        valid_neighbours = [node for node in neighbours if (node.upper() == node) or (node not in path_so_far)]
        for node in valid_neighbours:
            possible_paths += recursive_traverser(edges_dict, path_so_far + [node])
       
    return possible_paths
                
def solve2(data):
    edges_dict = parse_input(data)
    paths = recursive_traverser_2(edges_dict, ['start'])
    return len(paths)


def is_valid_path_2(path: List[str]) -> bool:
    "a path is valid if no more than one small cave is visited twice"
    small_caves = [cave for cave in path if cave.lower() == cave]
    cave_counter = dict(Counter(small_caves))
    
    counter_of_counters = Counter(cave_counter.values())
    
    return (
        counter_of_counters[2] <= 1 
        and set(counter_of_counters.keys()).issubset(set([1, 2]))
        and  cave_counter['start'] == 1
        and ('end' not in cave_counter or cave_counter['end'] == 1)
    )

def recursive_traverser_2(edges_dict: Dict[str, List[str]], path_so_far: List[str]) -> List[List[str]]:
    if path_so_far[-1] == 'end':
        possible_paths = [path_so_far]
    else:
        possible_paths = []
        neighbours = edges_dict[path_so_far[-1]]
        for node in neighbours:
            if is_valid_path_2(path_so_far + [node]):
                possible_paths += recursive_traverser_2(edges_dict, path_so_far + [node])
              
    return possible_paths