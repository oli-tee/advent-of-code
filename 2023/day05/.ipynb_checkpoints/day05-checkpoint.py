from collections import defaultdict
from typing import Tuple, List

def read_data(file_name):
    rows = open(file_name, 'r').read().split('\n')
    rows = [row.strip() for row in rows if row.strip() != '']
    return rows

def parse_maps(rows):
    maps = defaultdict(list)
    i = 0
    while i < len(rows):
        if rows[i].endswith('map:'):
            key = rows[i].replace(' map:', '')
        else:
            numbers = [int(x) for x in rows[i].split(' ')]
            maps[key].append((numbers[0], numbers[1], numbers[2]))
        i += 1
    
    return dict(maps)

def parse_seeds_p1(row):
    seeds = [int(x) for x in row.replace('seeds: ', '').split(' ')]
    return seeds


def parse_seeds_p1(row):
    seeds = [int(x) for x in row.replace('seeds: ', '').split(' ')]
    return seeds

def parse_data_p1(rows):
    seeds = parse_seeds_p1(rows[0])
    maps = parse_maps(rows[1:])
    
    return {'seeds': seeds, 'maps': maps}



def convert(value: int, the_map: Tuple[int, int, int]) -> int:
    if value >= the_map[1] and value < the_map[1] + the_map[2]:
        return value + the_map[0] - the_map[1]
    else:
        return None
    
def convert_multi(value, map_list: List[Tuple[int, int, int]]) -> int:
    result = value
    for the_map in map_list:
        target = convert(value, the_map)
        if target is not None:
            result = target
            
    return result

def end_to_end_convert(value, dict_of_map_lists):
    keys = [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location",
    ]
    
    for key in keys:
        map_list = dict_of_map_lists[key]
        value = convert_multi(value, map_list)
    
    return value

def solve_p1(file_name):
    rows = read_data(file_name)
    data = parse_data_p1(rows)
    
    map_dict = data['maps']
    seeds = data['seeds']
    
    result = min([end_to_end_convert(value, map_dict) for value in seeds])
    
    return result


def convert_to_plain_range(xs):
    return [(x[0], x[0]+x[1]) for x in xs]


def convert_to_plain_map(xs):
    result = [(x[1], x[1] + x[2], x[0]-x[1]) for x in xs]
    starts = [r[0] for r in result]
    sorted_result = [x for _, x in sorted(zip(starts, result))]
    return sorted_result


def parse_data_p2(rows):
    seeds = parse_seeds_p2(rows[0])
    maps = parse_maps_p2(rows[1:])
    
    return {'seed_ranges': seeds, 'maps': maps}

def parse_seeds_p2(row):
    numbers = row.replace('seeds: ', '').split(' ')
    seeds = [(int(numbers[2*i]), int(numbers[2*i]) + int(numbers[2*i+1])) for i in range(int(len(numbers)/2))]
    return seeds


def parse_maps_p2(rows):
    maps = defaultdict(list)
    i = 0
    while i < len(rows):
        if rows[i].endswith('map:'):
            key = rows[i].replace(' map:', '')
        else:
            numbers = [int(x) for x in rows[i].split(' ')]
            maps[key].append((numbers[1], numbers[1] + numbers[2], numbers[0]-numbers[1]))
        i += 1
    
    return dict(maps)


def convert_range(input_range, maps2):
    splits = [map2[0] for map2 in maps2] + [map2[1] for map2 in maps2] + [input_range[0], input_range[1]]
    splits =list(set(splits))
    splits = sorted(splits)
    splits = [s for s in splits if s >= input_range[0] and s <= input_range[1]]
    
    output_ranges_before_offset = [(splits[i], splits[i+1]) for i in range(len(splits)-1)]
    
    result = []
    for output_range in output_ranges_before_offset:
        offset = 0
        for map_range in maps2:
            #print(f"{output_range} / {map_range}")
            if output_range[0] >= map_range[0] and output_range[1] <= map_range[1]:
                offset = map_range[2]

        result.append((output_range[0] + offset, output_range[1] + offset))
        
    return result

def convert_multi_ranges(input_ranges, maps2):
    result = []
    for input_range in input_ranges:
        output_ranges = convert_range(input_range, maps2)
        result += output_ranges
        
    return result

def convert_ranges_end_to_end(input_ranges, dict_of_map_lists):
    keys = [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location",
    ]
    
    for key in keys:
        map_list = dict_of_map_lists[key]
        input_ranges = convert_multi_ranges(input_ranges, map_list)
    
    return input_ranges

def solve_p2(file_name):
    rows = read_data(file_name)
    data = parse_data_p2(rows)
    
    map_dict = data['maps']
    ranges = data['seed_ranges']
    
    final_ranges = convert_ranges_end_to_end(ranges, map_dict)
    score = min([myrange[0] for myrange in final_ranges])
    
    return score