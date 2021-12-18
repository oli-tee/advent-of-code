from typing import List 
import numpy as np


# We use 3 types of representations for snailfish numbers:
# - sf_string, e.g. '[1,[2, 3]]'
# - sf_list, e.g [1, [2, 3]]
# - sf_itemized, e.g. ["[", "1", ",", "[", "2", ",", "3", "]", "]"]
#

def read_data(file_name):
    rows = open(file_name, 'r'). read().split('\n')
    #rows = [eval(row) for row in rows if row != '']
    rows = [list(row) for row in rows if row != '']
    return rows
    
def explode(sf_itemized: List) -> List:
    last_number_position = None
    nested_level = 0
    i = 0
    number_to_add_to_next_nr = None
    has_already_exploded = False
    
    while i < len(sf_itemized):
        n = sf_itemized[i]
        
        if n.isnumeric() and nested_level == 5 and not has_already_exploded:
            in_a_pair = True

            if last_number_position is not None:
                sf_itemized[last_number_position] = str(int(sf_itemized[last_number_position]) + int(n))

            number_to_add_to_next_nr = sf_itemized[i+2]


            sf_itemized = sf_itemized[:i-1] + ['0'] + sf_itemized[i+4:]
            nested_level -= 1
            has_already_exploded = True

        else:
            if n == '[':
                nested_level += 1
            elif n == ']':
                nested_level -= 1   
            elif n.isnumeric():
                if number_to_add_to_next_nr is not None:
                    
                    sf_itemized[i] = str(int(number_to_add_to_next_nr) + int(n))
                    number_to_add_to_next_nr = None

                last_number_position = i
            i += 1

    return (sf_itemized, has_already_exploded)

def spleet(sf_itemized: List) -> List:
    
    has_already_split = False
    i = 0
    
    while i < len(sf_itemized) and not has_already_split:
        item = sf_itemized[i]
        if item.isnumeric() and int(item) >= 10:
            sf_itemized = sf_itemized[:i] + [
                '[',
                str(int(np.floor(int(item) / 2))),
                ',',
                str(int(np.ceil(int(item) / 2))),
                ']'
            ] + sf_itemized[i+1:]
            i += 4
            has_already_split = True
        i += 1
    
    return (sf_itemized, has_already_split)
       
        
    
def reduce(sf_itemized: List) -> List:
    time_to_stop = False
    
    while not time_to_stop:
        explode_result = explode(sf_itemized)
        spleet_result = spleet(sf_itemized)
        
        if explode_result[1]:
            sf_itemized = explode_result[0]
        elif spleet_result[1]:
            sf_itemized = spleet_result[0]
        else:
            time_to_stop = True
            
    return sf_itemized
            
def add(sf_itemized_1: List, sf_itemized_2: List) -> List:
    temp = ['['] + sf_itemized_1 + [','] +  sf_itemized_2 + [']']
    return reduce(temp)
    

def add_list_of_nr(list_of_itemized: List[List]):
    result = list_of_itemized[0]
    for nr in list_of_itemized[1:]:
        result = add(result, nr)
        
    return result

def get_magnitude(sf_list: List) -> int:
    
    if type(sf_list) == int:
        return sf_list
    else:
        total_magnitude = 3 * get_magnitude(sf_list[0]) + 2 * get_magnitude(sf_list[1])
        return total_magnitude

def get_magnitude_from_itemized(sf_itemized: List) -> int:
    return get_magnitude(eval(''.join(sf_itemized)))

def solve1(list_of_itemized_lists: List[List]) -> int:
    result_as_snailfish_nr_string = add_list_of_nr(list_of_itemized_lists)
    
    return get_magnitude_from_itemized(result_as_snailfish_nr_string)
    
def solve2(list_of_itemized_lists) -> int:
    max_sum_magnitude = -np.inf
    
    for i in range(len(list_of_itemized_lists)):
        for j in range(len(list_of_itemized_lists)):
            if i != j:
                summ = add(list_of_itemized_lists[i], list_of_itemized_lists[j])
                mag = get_magnitude_from_itemized(summ)
                max_sum_magnitude = max(max_sum_magnitude, mag)

    return max_sum_magnitude