import re

def read_data(file_name):
    rows = open(file_name, 'r').read().split('\n')
    rows = [row.strip() for row in rows if row.strip() != '']
    return rows


def parse_row(row):
    numbers = row.split(' ')
    return [int(x) for x in numbers]


def parse_data(rows):
    return [parse_row(row) for row in rows]


def extrapolate(row):
    if max(row) == 0 and min(row) == 0:
        row = row + [0]
    else:
        diff = [row[i+1] - row[i] for i in range(len(row)-1)]
        extrap_diff = extrapolate(diff)
        row = row + [row[-1] + extrap_diff[-1]]
    return row

def get_next_value(row):
    return extrapolate(row)[-1]

def solve_p1(file_name):
    data = parse_data(read_data(file_name))
    
    extra_values = [get_next_value(row) for row in data]
    return sum(extra_values)



def extrapolate_p2(row):
    if max(row) == 0 and min(row) == 0:
        row = [0] + row
    else:
        diff = [row[i+1] - row[i] for i in range(len(row)-1)]
        extrap_diff = extrapolate_p2(diff)
        row = [row[0] - extrap_diff[0]] + row
    return row


def get_prev_value(row):
    return extrapolate_p2(row)[0]

def solve_p2(file_name):
    data = parse_data(read_data(file_name))
    
    extra_values = [get_prev_value(row) for row in data]
    return sum(extra_values)
