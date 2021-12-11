from typing import List
from collections import Counter


def read_data(file_name):
    rows = [row for row in open(file_name).read().split('\n') if row != '']
    return rows

def parse_row(row):
    return (row.split('|')[0].strip().split(' '), row.split('|')[1].strip().split(' '))

def solve1(data):
    total = 0
    for row in data:
        parsed_row = parse_row(row)
        display = parsed_row[1]
        unique_segment_counts = [2, 3, 4, 7]
        total += sum([len(digit) in unique_segment_counts for digit in display])
    
    return total

def solve2(data):
    total = 0
    for row in data:
        parsed_row = parse_row(row)
        this_number = resolve_one_line(parsed_row)
        total += this_number
    
    return total

def get_segments_that_appear_n_times(digit_definitions: List[str], n: int):
    segment_activation_count = dict(Counter(''.join(digit_definitions)))
    return [x for x in segment_activation_count if segment_activation_count[x] == n]

def get_numbers_that_have_n_segments(digit_definitions, n):
    return [digit for digit in digit_definitions if len(digit) == n]

def get_digit_from_positions_on(list_of_positions_on: List[int]):
    if list_of_positions_on == [0, 1, 2, 4, 5, 6]:
        return 0
    elif list_of_positions_on == [2, 5]:
        return 1
    elif list_of_positions_on == [0, 2, 3, 4, 6]:
        return 2
    elif list_of_positions_on == [0, 2, 3, 5, 6]:
        return 3
    elif list_of_positions_on == [1, 2, 3, 5]:
        return 4
    elif list_of_positions_on == [0, 1, 3, 5, 6]:
        return 5
    elif list_of_positions_on == [0, 1, 3, 4, 5, 6]:
        return 6
    elif list_of_positions_on == [0, 2, 5]:
        return 7
    elif list_of_positions_on == [0, 1, 2, 3, 4, 5, 6,]:
        return 8
    elif list_of_positions_on == [0, 1, 2, 3, 5, 6]:
        return 9
    

def get_mapping_from_line(parsed_row):
    from collections import Counter
    """
    position 4: 4 times 
    position 1: 6 times
    position 5: 9 times


    position 0 & 2: 8 times
    position 0 can be deduced from digits 7 (3 on) and 1 (2 on)

    position 3 & 6 : 7 times
    position 3 is present in digit 4 (4 on)
    """
    mapping = [None for i in range(7)]

    digits = parsed_row[0]
    segment_activation_count = dict(Counter(''.join(digits)))

    # position 4: 4 times 
    mapping[4] = get_segments_that_appear_n_times(digits, 4)[0]
    # position 1: 6 times
    mapping[1] = get_segments_that_appear_n_times(digits, 6)[0]

    # position 5: 9 times
    mapping[5] = get_segments_that_appear_n_times(digits, 9)[0]


    # position 0 can be deduced from digits 7 (3 on) and 1 (2 on)
    seven = get_numbers_that_have_n_segments(digits, 3)[0]
    one = get_numbers_that_have_n_segments(digits, 2)[0]

    mapping[0] = [x for x in seven if x not in one][0]
    eighters = get_segments_that_appear_n_times(digits, 8)
    eighters
    mapping[2] = [x for x in eighters if x != mapping[0]][0]

    # position 3 & 6 : 7 times
    # position 3 is present in digit 4 (4 on)

    seveners = get_segments_that_appear_n_times(digits, 7)
    four = get_numbers_that_have_n_segments(digits, 4)[0]
    mapping[3] = [x for x in seveners if x in four][0]
    mapping[6] = [x for x in seveners if x not in four][0]

    print(mapping)
    inverse_mapping = dict()
    for i in range(len(mapping)):
        inverse_mapping[mapping[i]] = i
    
    return inverse_mapping


def resolve_one_line(parsed_row):
    inv_map = get_mapping_from_line(parsed_row)
    four_digits = parsed_row[1]
    
    #for i, digit in enumerate(four_digits):
    #rint(sorted([inv_map[x] for x in digit]))
    result_as_list_of_int = [get_digit_from_positions_on(sorted([inv_map[x] for x in digit])) for digit in four_digits] 
    return result_as_list_of_int[0] * 1000 + result_as_list_of_int[1] * 100 + result_as_list_of_int[2] * 10 + result_as_list_of_int[3]
    