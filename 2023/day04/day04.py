import re
import numpy as np

def read_data(file_name):
    rows = open(file_name, 'r').read().split('\n')
    return [row.strip() for row in rows if row.strip() != '']

def parse_row(row_string):
    row_string = row_string.replace('  ', ' ')
    row_string = re.sub('Card[ ]*\d*: ', '', row_string)
    nr_lists = [item.strip().split(' ') for item in row_string.split('|')]
    return nr_lists

def get_intersection(nr_lists):
    return [item for item in nr_lists[0] if item in nr_lists[1]]
    
def get_score_for_row(row_string):
    inters = get_intersection(parse_row(row_string))
    if len(inters) > 0:
        return 2 ** (len(inters) - 1)
    else:
        return 0
    
def solve_p1(data):
    print([get_score_for_row(row) for row in data])
    return sum([get_score_for_row(row) for row in data])



def solve_p2(data):
    counter = np.ones(len(data))
    for i in range(len(counter)):
        row_string = data[i]
        inters = get_intersection(parse_row(row_string))
        count_winning_nrs = len(inters)
        for j in range(i+1, i+1+count_winning_nrs):
            counter[j] += counter[i]
    
    print(counter)
    return sum(counter)